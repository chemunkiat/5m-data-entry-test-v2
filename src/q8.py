"""
Question 8 — Python: Find and Fix the Bug  [Short Answer — Write Code]

The function below is SUPPOSED to count how many even numbers are in a list.
It runs without crashing, but it returns the wrong answer.

    def count_evens(numbers):
        count = 0
        for n in numbers:
            if n % 2 == 1:      # <-- something here is wrong
                count = count + 1
        return count

    # Expected: 4  (the evens are 2, 4, 6, 8)
    print(count_evens([1, 2, 3, 4, 5, 6, 8]))

------------------------------------------------------------------
Task
------------------------------------------------------------------

(a) What does the buggy version actually return for [1, 2, 3, 4, 5, 6, 8], and why?

    Answer: The code will return count of 3, because it counts odd numbers of [1,3,5]

(b) Fix the bug. Write the corrected function below.
    (A one-character change is enough, but you must understand why.)
"""

def count_evens(numbers):
    # your corrected code here
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count = count + 1
    return count
print(count_evens([1, 2, 3, 4, 5, 6, 8]))

"""
(c) In one sentence, explain in plain English what `n % 2 == 0` checks.

    Answer: The original coding error n % 2 == 1 checks n divide by 2 has remainder of 1, this is when n is a odd number. 
    Correction to n % 2 == 0 will check if dividing n has remainder of 0, meaning n is an even number.

@chemunkiat ➜ /workspaces/5m-data-entry-test-v2 (main) $ python
Python 3.14.2 (main, Oct 28 2026, 19:03:49) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> def count_evens(numbers):
...     # your corrected code here
...     count = 0
...     for n in numbers:
...         if n % 2 == 0:
...             count = count + 1
...     return count
... print(count_evens([1, 2, 3, 4, 5, 6, 8]))
... 
4
"""
