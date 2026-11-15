"""Audit and summarise the rubric-writing project.

Usage: python audit.py [prompts.csv] [rubric_items.csv]
Reads the two CSVs, checks them for problems, and prints the scores for the README.
Also writes results_summary.md.
"""
import sys
import pandas as pd

PROMPTS = sys.argv[1] if len(sys.argv) > 1 else "prompts.csv"
ITEMS = sys.argv[2] if len(sys.argv) > 2 else "rubric_items.csv"

p = pd.read_csv(PROMPTS, dtype=str).fillna("")
o = pd.read_csv(ITEMS, dtype=str).fillna("")
out = []


def say(s=""):
    print(s)
    out.append(s)


# ---- 1. checks ----
problems = []
if not o.item_id.is_unique:
    problems.append("duplicate item_id values: " + ", ".join(o.item_id[o.item_id.duplicated()]))
if o.duplicated(["prompt_id", "item_text"]).any():
    problems.append("duplicate item text within a prompt")
for col in ["critical", "atomic", "objective", "self_contained", "atomic_after",
            "objective_after", "self_contained_after", "a_pass", "b_pass", "revised"]:
    bad = o[~o[col].isin(["Y", "N"])]
    if len(bad):
        problems.append(f"{col}: {len(bad)} cells are not Y or N ({', '.join(bad.item_id[:5])}...)")
missing = set(p.id) - set(o.prompt_id)
if missing:
    problems.append("prompts with no items: " + ", ".join(sorted(missing)))
for pid, g in o.groupby("prompt_id"):
    if len(g) < 2:
        problems.append(f"{pid} has fewer than 2 items")
for c in ["response_a", "response_b", "rubric_complete", "date_tested", "model_a", "model_b"]:
    empty = p[p[c].str.strip() == ""]
    if len(empty):
        problems.append(f"prompts.csv {c} is empty for: " + ", ".join(empty.id))
# an item marked revised must keep its first draft
nodraft = o[(o.revised == "Y") & (o.draft_text.str.strip() == "")]
if len(nodraft):
    problems.append("revised items without draft_text: " + ", ".join(nodraft.item_id))
# after-revision checks must all be Y
notfixed = o[(o.atomic_after != "Y") | (o.objective_after != "Y") | (o.self_contained_after != "Y")]
if len(notfixed):
    problems.append("items still failing a criterion after revision: " + ", ".join(notfixed.item_id))
# heuristic atomicity flag: joined with and/or inside the item
heur = o[o.item_text.str.contains(r"\b(?: and |, and | or )\b", regex=True)]
say("## Checks")
if problems:
    for x in problems:
        say("- PROBLEM: " + x)
else:
    say("- No missing cells, duplicates or invalid values.")
say(f"- Heuristic only: {len(heur)} item(s) contain 'and' or 'or' in the text; "
    "re-read them for atomicity: " + ", ".join(heur.item_id))

# ---- 2. scores ----
cat = p.set_index("id").category
o["category"] = o.prompt_id.map(cat)
for m in ("a", "b"):
    o[m] = (o[f"{m}_pass"] == "Y").astype(int)
names = {"a": p.model_a.iloc[0] + " (" + p.model_version_a.iloc[0] + ")",
         "b": p.model_b.iloc[0] + " (" + p.model_version_b.iloc[0] + ")"}

say("\n## Pass rate per model")
for m in ("a", "b"):
    say(f"- {names[m]}: {o[m].sum()}/{len(o)} items passed ({o[m].mean():.0%})")

say("\n## Pass rate by category")
t = o.groupby("category").agg(items=("item_id", "count"), a=("a", "mean"), b=("b", "mean"))
say("| Category | Items | " + names["a"] + " | " + names["b"] + " |")
say("| --- | --- | --- | --- |")
for c, r in t.sort_values("items", ascending=False).iterrows():
    say(f"| {c} | {int(r['items'])} | {r['a']:.0%} | {r['b']:.0%} |")

say("\n## Critical items failed")
crit = o[o.critical == "Y"]
for m in ("a", "b"):
    f = crit[crit[m] == 0]
    say(f"- {names[m]}: {len(f)} of {len(crit)} critical items failed" +
        (" (" + ", ".join(f.item_id) + ")" if len(f) else ""))

say("\n## Prompts where the models differ")
pr = o.groupby("prompt_id").agg(a=("a", "sum"), b=("b", "sum"), n=("item_id", "count"))
diff = pr[pr.a != pr.b]
for pid, r in diff.iterrows():
    say(f"- {pid}: {names['a'].split()[0]} {int(r.a)}/{int(r.n)} vs {names['b'].split()[0]} {int(r.b)}/{int(r.n)}")
same = pr[pr.a == pr.b]
say(f"- {len(diff)} of {len(pr)} prompts differ; {len(same)} give equal scores.")
both_fail = o[(o.a == 0) & (o.b == 0)]
say(f"- Items both models failed: {len(both_fail)} ({', '.join(both_fail.item_id)})")

say("\n## Rubric item quality (drafting stage)")
post = o.what_failed.str.startswith("post-grading")
pre = o[(o.revised == "Y") & ~post]
firstdraft = o[~o.item_id.isin(["P13-I5"])]  # P13-I5 was created by splitting an item
n_first = len(firstdraft)
flagged = firstdraft[(firstdraft.revised == "Y") & ~firstdraft.what_failed.str.startswith("post-grading")]
say(f"- Drafted items: {n_first}; rewritten after my review before grading: {len(flagged)} ({len(flagged)/n_first:.0%}).")
crit_counts = {"atomic": (firstdraft.atomic == "N").sum(),
               "objective": (firstdraft.objective == "N").sum(),
               "self_contained": (firstdraft.self_contained == "N").sum()}
say("- First-draft failures by criterion: " + ", ".join(f"{k} {v}" for k, v in crit_counts.items()))
say(f"- Items changed after grading (disclosed): {int(post.sum())} ({', '.join(o.item_id[post])}).")

say("\n## Model versions and date")
say(f"- A: {names['a']}; B: {names['b']}; tested {p.date_tested.iloc[0]}.")

open("results_summary.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
