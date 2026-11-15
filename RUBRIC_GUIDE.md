# Rubric-Writing Guide

For each prompt you write a small rubric of yes/no items, check your own items against four quality criteria, then grade two chatbot answers against them. The point of the project is the quality of your rubric items, so spend your time there.

## The four quality criteria

Check every rubric item against these before you use it.

| Criterion | Level | The item passes if... | Fails when... |
| --- | --- | --- | --- |
| **Atomicity** | Item | It checks exactly one requirement | It joins checks with "and" or "or", or one fail could mean two different things |
| **Objectivity** | Item | Two careful reviewers would always give the same yes or no | It uses vague words such as "good", "clear", "appropriate" or "enough" |
| **Self-containment** | Item | It can be graded from the item text and the answer alone, with no need to reread the prompt or look anything up | It says "the required format", "the correct answer" or "as asked" without stating what that is |
| **Completeness** | Whole rubric | Together the items cover every explicit requirement in the prompt, and the key correct content | A requirement in the prompt has no item checking it |

Atomicity, objectivity and self-containment are checked per item. Completeness is checked once per prompt, for the whole set of items.

## Examples

**Atomicity**
- Bad: "The answer has exactly 4 sentences and avoids the word 'cool'."
- Good: "The answer has exactly 4 sentences." and "The word 'cool' does not appear."

**Objectivity**
- Bad: "The explanation is clear."
- Good: "The explanation states that the refrigerant absorbs heat inside the fridge."

**Self-containment**
- Bad: "The answer follows the requested word limit."
- Good: "The product description is exactly 50 words long."

**Completeness**
- A prompt that asks for 3 days with 3 activities each and a packing tip needs items for the number of days, the activities per day, the time-of-day labels and the packing tip. Leaving out the packing tip item is a completeness fail.

## How to write the items (about 4 per prompt)

1. Read the prompt and list every explicit requirement and the key content a correct answer must contain.
2. Write one yes/no item per requirement. Phrase each as a statement that is true or false about the answer.
3. Put numbers, names and limits into the item text, so it stands on its own.
4. Mark the items that would make the answer wrong if they failed as `critical` (Y or N).
5. Check each item against atomicity, objectivity and self-containment and mark Y or N in the check columns.
6. If any check is N, rewrite the item and set `revised` to Y. Keep a count: the share of first drafts that needed a rewrite is a real finding for your README.
7. Check the whole set against completeness and mark `rubric_complete` Y or N in `prompts.csv`. Add items until it is Y.

## How to grade

1. Mark `a_pass` and `b_pass` as Y or N for each item, one answer at a time. Grade only what the item says.
2. If you cannot decide Y or N from the item text alone, the item is not objective. Fix the item, set `revised` to Y, then grade.
3. Verify any facts against a reliable source before marking an item.
4. Do not change a grade after you have seen the summary.

## Scores to report

- Pass rate per model = items passed / total items.
- Pass rate by category.
- Critical items failed per model.
- Prompts where the models differ.
- Share of first-draft items rewritten, and which criterion they failed most often.

## Procedure for collecting answers (identical for all 20 prompts)

1. Use a new chat for every prompt, with default settings and no custom instructions or memory.
2. Paste each prompt exactly as written. Do not edit or retry the answer.
3. Paste the answers into `response_a` and `response_b` as the `model_a` and `model_b` columns say.
4. Write the rubric items before you read the answers closely, so the items are not shaped by what the answers happened to say.
5. Record the date and the model versions in the README.

## Limitations to state in the README

- One rater, 20 prompts and two models: a small personal sample, not a benchmark.
- Grading is not blind, because you know which model wrote each answer.
- You wrote the items and graded the answers yourself, so the agreement a second grader would reach is unknown.
- Models change over time, so results only describe the version and date you tested.

## Time plan (about 4.5 to 5 hours)

| Step | Time |
| --- | --- |
| Run the 20 prompts on two chatbots and paste the answers | 60 min |
| Write and self-check about 80 items | 75 min |
| Grade 160 answer-item pairs | 60 min |
| Python audit script and summary | 45 min |
| README, push to GitHub | 30 min |
