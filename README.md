# Rubric-Based Comparison of ChatGPT and Gemini

A small project on writing and testing rubric items for AI response evaluation. It uses 20 test prompts, each with a rubric of yes/no items. Every item was checked for quality, and the rubric was then used to grade answers from ChatGPT (GPT 6) and Gemini (Hydrogen).

I designed this evaluation: I chose the quality criteria, reviewed and revised the prompts and rubric items, ran both models, and graded the answers.

**Tested:** 2026-11-15 · **Prompts:** 20 · **Rubric items:** 78 · **Graded answer-item pairs:** 156

## Why a rubric instead of a score out of 10

A rating like "8/10" cannot be checked. A rubric item such as "The answer contains exactly 4 sentences" can: two reviewers with the answer in front of them reach the same result. The point of this project is the quality of the items, so most of the work went into writing and checking them.

## Item quality criteria

Every item was checked against four criteria.

| Criterion | Level | The item passes if... |
| --- | --- | --- |
| Atomicity | Item | It checks exactly one requirement |
| Objectivity | Item | Two careful reviewers would give the same yes or no |
| Self-containment | Item | It can be graded from the item text and the answer alone |
| Completeness | Whole rubric | Together the items cover every explicit requirement in the prompt |

Full definitions, good and bad examples, and the procedure are in [`RUBRIC_GUIDE.md`](RUBRIC_GUIDE.md).

## Files

| File | What it holds |
| --- | --- |
| `prompts.csv` | The 20 prompts, categories, reference notes, both answers, model versions and test date |
| `rubric_items.csv` | The 78 items, their quality checks, first drafts of revised items, and the grades |
| `audit.py` | Checks both files for problems and computes every number below |
| `results_summary.md` | Output of `audit.py` |
| `CHANGES_TO_RESPONSES.md` | Every formatting fix made to the pasted answers |
| `RUBRIC_GUIDE.md` | The rules I followed |

Run the audit with `python audit.py` (needs `pandas`).

## Method

1. **Prompts.** 20 prompts in seven categories: constraint-heavy (6), ambiguous (4), edge case (3), counting (2), multi-step (2), reasoning (2) and factual (1). They were chosen to be hard enough that the two models would not give the same answer, and they were fixed before any of them was run. They include letter limits, word counts, a date calculation, a false premise, a play that does not exist, and an impossible request.
2. **Items.** I reviewed, edited and approved every item. About 4 items per prompt, each a statement that is true or false about an answer. Numbers, names and limits are written into the item so it stands alone. Items that would make the answer wrong if they failed are marked `critical` (51 of 78).
3. **Quality check.** Each item was checked for atomicity, objectivity and self-containment. Items that failed were rewritten, and the first draft is kept in the `draft_text` column with the reason in `what_failed`. Completeness was checked once per prompt (`rubric_complete` in `prompts.csv`).
4. **Collecting answers.** Each prompt went into a new chat with default settings, pasted exactly as written, with no retries. Both models got the same prompts on the same day. Model A is always ChatGPT and model B is always Gemini.
5. **Grading.** Each answer was graded Y or N against each item. Counting items (words, sentences, characters, letters) were checked by script and facts were checked against sources. I reviewed every grade and decided the judgement calls myself.

## Results

| | ChatGPT (GPT 6) | Gemini (Hydrogen) |
| --- | --- | --- |
| Items passed | 68 / 78 (87%) | 69 / 78 (88%) |
| Critical items failed | 6 / 51 | 5 / 51 |

The totals are almost the same, but the models fail in different places. They scored differently on 11 of the 20 prompts, and both failed only one item (P02-I2, the poem with no letter "e").

| Category | Items | ChatGPT | Gemini |
| --- | --- | --- | --- |
| Constraint-heavy | 26 | 85% | 92% |
| Ambiguous | 16 | 88% | 94% |
| Multi-step | 10 | 100% | 90% |
| Edge case | 9 | 67% | 67% |
| Counting | 8 | 88% | 100% |
| Reasoning | 5 | 100% | 100% |
| Factual | 4 | 100% | 50% |

The Factual and Reasoning rows rest on only 4 and 5 items, so they show where to look, not a finding.

### What stood out

- **False premise (P18).** Asked to summarise Shakespeare's non-existent play *The Merchant of Verona*, Gemini wrote a full plot as if the play existed (0/3). ChatGPT said no such play exists and suggested *The Merchant of Venice* (3/3).
- **Impossible request (P20).** Asked for a 3-word sentence that is at least 10 words long, ChatGPT wrote a sentence and presented it as meeting the condition (0/3). Gemini said the request is contradictory (3/3).
- **Hard limits.** ChatGPT broke several exact limits: it used the word "cool" in a refrigerator answer that banned it (P08), wrote a 49-word description when 50 were asked for (P09), and said 7 words had four letters when the answer is 4 (P06).
- **Under-specified prompts (P12).** Gemini gave a detailed answer that names the factors and conditions behind renting versus buying. ChatGPT asked what was being rented or bought and listed no factors.
- **Letter constraint (P02).** Neither poem avoided the letter "e". ChatGPT's poem also contains a Cyrillic "е" that looks identical to the Latin one, so a plain text search for "e" would miss it.
- **Factual (P01).** Gemini gave 68°C as its standard figure (it offered 71°C as an alternative), while the correct value is about 70–71°C. ChatGPT gave 70°C.

## Rubric quality findings

- 77 items were drafted before any answer was seen. 19 of them (25%) failed at least one criterion and were rewritten before grading.
- The most common first-draft failure was **objectivity** (14 items), then **atomicity** (3) and **self-containment** (2). Typical objectivity failures were vague phrases such as "close equivalent", "a sea-related noun" and "only one analogy". These were replaced with closed lists or counts.
- Some items were also **over-specific**: they would have marked a correct answer wrong, for example by requiring a particular method for a maths answer. These were rewritten to check the result.
- One item (P07-I4) was changed **after** grading. It required "3 pm" in every version, including the casual one, and ChatGPT's casual version said "at 3". I judged this over-strict for a casual message and loosened it, so ChatGPT's grade on that item changed from N to Y. Because it was changed after seeing the answer, it is marked in `what_failed` as a post-grading revision.
