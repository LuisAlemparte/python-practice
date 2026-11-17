# Revision — Weeks 0–7 (Sat 14 Nov)

Rules: answer each question out loud or on paper *before* looking at the answers at the bottom.
Mark each ✅ / ❌. Anything ❌ goes into log.md as a line to revisit. 30 questions, ~90 minutes.

## C (weeks 1–5)
1. What does `#include <stdio.h>` do, and what happens if you call `printf` without it?
2. `int x = 5 / 2;` — what is `x`, and why? How do you get 2.5? 
3. Write the `do … while` 
4. What is the difference between `=` and `==`? What does `if (x = 5)` 
5. A string in C is really what? What ends it? 
6. What does `&x` give you, and what does `*p` give you? *p 
7. Why does `malloc` need `free`? What tool tells you if you forgot? 
8. What is a struct? Write one for a tenant with name and rent. 
9. In `speller`, why did we use a hash table instead of a linked 
10. Recursion: what two things does every recursive function need? 

## Python (week 6 + PCC)
11. `input()` returns what type? How do you turn it into a number, and what can go wrong? whatever the person writtes in you can off coursr use the argv to check if its numbers or letters
12. `try / except ValueError` replaces which C pattern? 
13. What is a dict? Write one for a tenant, then print its rent. 
14. What does `for i, d in enumerate(reversed(digits))` give you each loop? 
15. `[int(d) for d in number]` — say in words what this does.
16. What does `sum(c.isalpha() for c in text)` count, and why does it work?
17. `csv.DictReader` gives you what per row? What type are the values?
18. What does `"a" * 3 + "b"` produce?
19. Why must a function be defined above the line that calls it?
20. What does `with open(...) as f:` do that plain `open()` doesn't?

## SQL (week 7)
21. Write a query: names of all tenants whose expected rent is over 1000.
22. What does `GROUP BY` do, and when do you need `HAVING` instead of `WHERE`?
23. Difference between `JOIN` and `LEFT JOIN`. When did we need LEFT JOIN?
24. What is a foreign key? Give the example from movies.db.
25. What does `WITH x AS (...)` do, and why did we use it?
26. In sqlite3: what's the difference between the `$` prompt and the `sqlite>` prompt?

## The flats project
27. The script matches transfers to tenants by IBAN, not name. Why?
28. A payment on the 30th counts for which month, and why?
29. What is an eval? What were the two kinds of misses we found in ours?
30. In two sentences, what does `rent_check.py` do and what does `classify_emails.py` do? (This is your interview answer.)

---

## Answers (don't peek first)
1. Tells the compiler about printf etc. Without it: implicit declaration warning/error, or undefined behaviour.
2. `x` is 2: integer division truncates. `5 / 2.0` or `(float) 5 / 2` gives 2.5.
3. `do { n = get_int("n: "); } while (n < 1);`
4. `=` assigns, `==` compares. `if (x = 5)` assigns 5 to x and is always true.
5. An array of `char` ending in `'\0'`. `string` is `char *`.
6. `&x` = the address of x. `*p` = the value at the address p points to.
7. Memory you malloc stays yours until freed; leaks otherwise. `valgrind`.
8. A bundle of named fields: `typedef struct { string name; int rent; } tenant;`
9. Hash table: ~O(1) lookup (compute bucket, walk a short chain). A single linked list is O(n) per lookup — 143k words × every word in the text.
10. A base case (when to stop) and a recursive case that moves toward it.
11. A string. `int(...)`; raises `ValueError` if it's not a number.
12. The `do … while` + re-prompt loop with `get_int`.
13. `t = {"name": "Braun", "rent": 508}` then `print(t["rent"])`.
14. A pair: position `i` from the right (0, 1, 2…) and the digit `d`.
15. For each character in `number`, convert to int, collect them in a list.
16. Letters. `isalpha()` is True/False; True counts as 1 in `sum`.
17. A dict per row, keys = header; every value is a string.
18. `"aaab"`.
19. Python runs top to bottom; a name doesn't exist until its line has run.
20. Closes the file automatically, even if an error happens inside.
21. `SELECT tenant FROM tenants WHERE expected > 1000;`
22. Collapses rows that share a value into one row so aggregates (SUM, COUNT) apply per group. `HAVING` filters *after* grouping (on the aggregate); `WHERE` filters rows before.
23. JOIN keeps only matching pairs; LEFT JOIN keeps every left row, with NULLs when there's no match. Needed to show tenants with no payment (MISSING).
24. A column that refers to another table's primary key. `stars.movie_id` → `movies.id`.
25. Names a sub-result (CTE) you can use below, like a temporary table. Kept the rent-check query readable: `active`, `rent`, then the final SELECT.
26. `$` is the shell (cd, ls, python, check50). `sqlite>` is inside the database (SELECT, .schema, .quit).
27. Payers differ from tenants (partners, relatives, a different surname); the IBAN is stable.
28. The next month: people pay at month-end for the month ahead. (`day >= 29` → month + 1.)
29. A labelled set + a script that scores predictions against it. Misses were label errors (fix the data) and prompt errors (fix the prompt).
30. `rent_check.py` reads the bank export, matches every transfer to a tenant by IBAN, and reports per month who paid, how late, and what's missing, as CSV and a German one-page report. `classify_emails.py` classifies tenant emails with Claude into repair/payment/question/other, keeps a ticket list, and drafts replies in the owner's voice, scored against a 30-email labelled set.
