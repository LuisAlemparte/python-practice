   # Learning log

   ## 2026-10-26
   26 Oct was good, getting down the most important parts remembering the correct ways to writte code very important ()=/ etc. Need to revisit until nailed down.
   ## 2026-10-27:
    insane how much easier python is so much more confortable than CS50... very easy and relaxed day with lists and etc pretty intiative.
   ## 2026-10-28 
   Creating lops and making list and (title.) makes everything still pretty resanpbel to understnd
   ## 3 Nov 26
   Created first code for the automatition of 2 buildings! Working good for now waited on the actual tenant informations.
   ## 2026-11-05/06
- Real data in: 15 tenants, MT940 bank export, matched by IBAN not name
- Paper had 2 wrong rents + 1 wrong name; the bank data corrected it
- Fixed 3 rules from the output: valid_from per tenant, late-month payments, rent vs other transfers
- 9 anomalies → 1 (known credit). 3 minutes instead of 2 afternoons
- recover 7/7, pset 4 complete
- Lessons: replace the whole block when indentation drifts; print must sit after the whole if/elif/else; i = di vs i + di
## Mon 9 Nov — Week 5 (Data Structures)
- inheritance: recursion, malloc for each person, random alleles from parents, free bottom-up
- speller: hash table (65536 buckets) of linked lists, hash = sum*31 of lowercase letters, fscanf, strcasecmp, free with tmp pointer, valgrind 0 leaks, 0.06s total
load_dotenv() reads .env and puts ANTHROPIC_API_KEY into the environment. anthropic.Anthropic() finds it there automatically. The key never appears in code.
CATEGORIES — the only four answers we accept.
PROMPT — triple quotes = multi-line string. {text} is a hole that .format(text=...) fills later. “Antworte nur mit dem einen Wort” forces a one-word answer so we can compare it.
client.messages.create(...) — the actual API call. model which Claude (Haiku = cheapest, fastest, enough for this). max_tokens=5 cap on answer length. messages is a list of turns; we send one user turn.
response.content[0].text — the reply text. .strip().lower() cleans spaces and case.
return answer if answer in CATEGORIES else "other" — if Claude says something unexpected, fall back to “other” instead of crashing.
Loop: predicted vs row["category"]; hit is True/False, and correct += hit works because True counts as 1.
{correct / len(rows):.0%} — format as a percentage with 0 decimals.
## Mon 9 Nov Part 2
- CS50 pset 5: inheritance 9/9, speller (hash table, linked lists, valgrind clean, 0.06s)
- rent_check v3: per-tenant due_day + BUFFER, days_late, LATE status. Oct: all on time except Azal (2d) and Oezkaya LKW (16d)
- First Claude API call: classify_emails.py, Haiku, 19/20 on labelled set. Inbox mode → tickets.csv, ticket #1 Braun balcony
- Claude desktop linked to repos; .env for API key## Tue 10 Nov
- classify_emails: inbox dedupe (set), close command (read-modify-rewrite CSV), reply drafter (Sonnet 5.5, system prompt persona, placeholders [Anrede]/[Firma]/[Datum]), drafts saved to output/antworten, eval2 double run
- rent_check: monthly German report Bericht-YYYY-MM.md (Soll/Ist, Auffälligkeiten, offene Anliegen)
- Eval: 20→30 emails. Prompt v2 fixed 2, broke 2 (same 90%) → only the full set shows it. 2 label errors, fixed. 30/30
- Model switch Haiku 4.5→5.5 dropped to 73%: empty answers, thinking ate max_tokens. Silent fallback hid it → always log unexpected output
- Evals are snapshots: same input, different run, different misses. Functions must be defined above where they're called
- git: commit message = what changed, not the commands; filter-branch to rewrite history
## Wed 11 Nov — Week 6 (Python)
- Pset 6 all five submitted before lunch: hello, mario, credit, readability, dna
- Python vs C: no types, no malloc, no \0; input() + int(); try/except ValueError instead of do-while; chained comparisons 1 <= x <= 8
- Strings: " " * n, slicing number[:2], text.split(), c.isalpha(), c in ".!?"
- sum(bool for ...) counts Trues; all(...) true only if every item is; list/dict comprehensions
- dna: csv.DictReader → list of dicts, keys()[1:] for the STR names, int() before comparing CSV strings to ints, return inside loop = found
- Recurring bug: code indented inside a loop that should run after it. Recurring terminal bug: wrong folder, read the prompt

