## Checks
- No missing cells, duplicates or invalid values.
- Heuristic only: 14 item(s) contain 'and' or 'or' in the text; re-read them for atomicity: P01-I1, P01-I4, P02-I2, P03-I4, P05-I3, P06-I2, P07-I4, P11-I2, P11-I5, P12-I2, P12-I4, P18-I3, P19-I3, P20-I2

## Pass rate per model
- ChatGPT (GPT 6): 68/78 items passed (87%)
- Gemini (Hydrogen): 69/78 items passed (88%)

## Pass rate by category
| Category | Items | ChatGPT (GPT 6) | Gemini (Hydrogen) |
| --- | --- | --- | --- |
| Constraint-heavy | 26 | 85% | 92% |
| Ambiguous | 16 | 88% | 94% |
| Multi-step | 10 | 100% | 90% |
| Edge case | 9 | 67% | 67% |
| Counting | 8 | 88% | 100% |
| Reasoning | 5 | 100% | 100% |
| Factual | 4 | 100% | 50% |

## Critical items failed
- ChatGPT (GPT 6): 6 of 51 critical items failed (P02-I2, P06-I1, P08-I3, P09-I1, P20-I1, P20-I3)
- Gemini (Hydrogen): 5 of 51 critical items failed (P01-I1, P02-I2, P05-I2, P18-I1, P18-I2)

## Prompts where the models differ
- P01: ChatGPT 4/4 vs Gemini 2/4
- P03: ChatGPT 5/5 vs Gemini 4/5
- P05: ChatGPT 5/5 vs Gemini 4/5
- P06: ChatGPT 2/3 vs Gemini 3/3
- P08: ChatGPT 4/5 vs Gemini 5/5
- P09: ChatGPT 3/4 vs Gemini 4/4
- P11: ChatGPT 4/5 vs Gemini 5/5
- P12: ChatGPT 2/4 vs Gemini 4/4
- P13: ChatGPT 5/5 vs Gemini 4/5
- P18: ChatGPT 3/3 vs Gemini 0/3
- P20: ChatGPT 0/3 vs Gemini 3/3
- 11 of 20 prompts differ; 9 give equal scores.
- Items both models failed: 1 (P02-I2)

## Rubric item quality (drafting stage)
- Drafted items: 77; rewritten after my review before grading: 19 (25%).
- First-draft failures by criterion: atomic 3, objective 14, self_contained 2
- Items changed after grading (disclosed): 1 (P07-I4).

## Model versions and date
- A: ChatGPT (GPT 6); B: Gemini (Hydrogen); tested 2026-11-15.
