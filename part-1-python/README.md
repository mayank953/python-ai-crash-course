# Part 1: Python

44 lessons in video order. Each lesson folder holds the whiteboard PDF, a theory notebook, a code notebook and sometimes exercises, plus a README with the video timestamps and three small tasks.

Legend: 📄 whiteboard notes (PDF) · 📘 theory notebook · 💻 code notebook · ✏️ exercises · *extra* = no chapter of its own in the video

### Setup & Basics

| # | Lesson | What you learn | Video | Files |
|---|--------|---------------|-------|-------|
| 01 | [Introduction to Python](01-introduction-to-python/) | Why programming exists, what makes Python a good first language, and where it is used in the real world. | [`0:00`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=0s) | [📄](01-introduction-to-python/whiteboard-notes.pdf "Whiteboard notes (PDF)") |
| 02 | [Installing Python & Setting Up Jupyter](02-installing-python/) | Install Python, run it from the terminal and IDLE, and set up Anaconda with Jupyter notebooks. | [`14:22`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=862s) | [📄](02-installing-python/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](02-installing-python/code.ipynb "Code notebook") |
| 03 | [Built-in Functions, print(), Modules, Errors & Identifiers](03-print-input-modules/) | Built-in functions, `print()` with `sep` and `end`, importing modules such as `math`, telling syntax errors from runtime errors, and the rules for naming things. | [`29:18`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=1758s) | [📘](03-print-input-modules/theory.ipynb "Theory notebook") [💻](03-print-input-modules/code.ipynb "Code notebook") |

### Data Types, Strings & Type Casting

| # | Lesson | What you learn | Video | Files |
|---|--------|---------------|-------|-------|
| 04 | [Data Types](04-data-types/) | How Python classifies data, why variables can change type, and why integers have no fixed size. | [`51:57`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=3117s) | [📄](04-data-types/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](04-data-types/theory.ipynb "Theory notebook") [💻](04-data-types/code.ipynb "Code notebook") |
| 05 | [Numeric Types: int, float, complex](05-numeric-data-types/) | The three numeric types: `int`, `float` and `complex`, including float precision surprises. | [`51:57`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=3117s) | [📄](05-numeric-data-types/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](05-numeric-data-types/theory.ipynb "Theory notebook") [💻](05-numeric-data-types/code.ipynb "Code notebook") |
| 06 | [Boolean Data Type](06-boolean/) | What `True` and `False` really are, and which values Python treats as truthy or falsy. | [`1:06:20`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=3980s) | [📄](06-boolean/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](06-boolean/theory.ipynb "Theory notebook") [💻](06-boolean/code.ipynb "Code notebook") |
| 07 | [Strings Basics](07-strings/) | Creating strings with different quotes, escape sequences, and why strings cannot be edited in place. | [`1:12:28`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=4348s) | [📄](07-strings/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](07-strings/theory.ipynb "Theory notebook") [💻](07-strings/code.ipynb "Code notebook") |
| 08 | [String Indexing (Positive & Negative)](08-indexing/) | Picking single characters from a string with positive and negative positions. | [`1:19:04`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=4744s) | [📄](08-indexing/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](08-indexing/theory.ipynb "Theory notebook") [💻](08-indexing/code.ipynb "Code notebook") |
| 09 | [Concatenation, Repetition & Slicing](09-concatenation-slicing/) | Joining and repeating strings, slicing with `start:stop`, and using a step to skip or reverse. | [`1:27:35`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=5255s) | [📄](09-concatenation-slicing/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](09-concatenation-slicing/code.ipynb "Code notebook") [💻](09-concatenation-slicing/code-step-in-slicing.ipynb "Code notebook") |
| 10 | [Type Conversion & Type Casting](10-type-casting/) | Automatic (implicit) conversion versus explicit casting with `int()`, `float()`, `str()` and `bool()`. | [`2:01:13`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=7273s) | [📄](10-type-casting/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](10-type-casting/theory.ipynb "Theory notebook") [💻](10-type-casting/code.ipynb "Code notebook") |

### Operators & String Formatting

| # | Lesson | What you learn | Video | Files |
|---|--------|---------------|-------|-------|
| 11 | [Operators Overview & Arithmetic Operators](11-arithmetic-operators/) | The family of operators, and the seven arithmetic ones including floor division, modulus and power. | [`2:15:50`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=8150s) | [📄](11-arithmetic-operators/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](11-arithmetic-operators/theory.ipynb "Theory notebook") [💻](11-arithmetic-operators/code.ipynb "Code notebook") |
| 12 | [Relational Operators](12-relational-operators/) | Comparing numbers and strings with `==`, `!=`, `<`, `>`, `<=` and `>=`. | [`2:26:08`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=8768s) | [📄](12-relational-operators/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](12-relational-operators/theory.ipynb "Theory notebook") [💻](12-relational-operators/code.ipynb "Code notebook") |
| 13 | [Logical, Assignment & Identity Operators](13-logical-assignment-identity/) | Combining conditions with `and`, `or`, `not`, updating variables with `+=` and friends, and `is` versus `==`. | [`2:43:46`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=9826s) | [📄](13-logical-assignment-identity/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](13-logical-assignment-identity/theory.ipynb "Theory notebook") [💻](13-logical-assignment-identity/code.ipynb "Code notebook") |
| 14 | [Membership & Binary (Bitwise) Operators](14-membership-binary/) | Checking membership with `in`, and working with bits using `&`, `|`, `^`, `~`, `<<` and `>>`. | extra | [📄](14-membership-binary/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](14-membership-binary/theory.ipynb "Theory notebook") [💻](14-membership-binary/code.ipynb "Code notebook") |
| 15 | [Operator Precedence & Associativity](15-precedence-associativity/) | Which operator runs first, and how Python breaks ties when precedence is equal. | [`3:06:08`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=11168s) | [📄](15-precedence-associativity/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](15-precedence-associativity/code.ipynb "Code notebook") |
| 16 | [String Formatting & f-Strings](16-string-formatting/) | Building readable output with `%`, `.format()` and f-strings, including alignment and number formatting. | [`3:13:46`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=11626s) | [📄](16-string-formatting/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](16-string-formatting/theory.ipynb "Theory notebook") [💻](16-string-formatting/code.ipynb "Code notebook") |

### Conditionals & Loops

| # | Lesson | What you learn | Video | Files |
|---|--------|---------------|-------|-------|
| 17 | [Decision Control & the if Statement](17-conditionals-if/) | Making decisions in code with `if`, and why indentation matters in Python. | [`3:28:43`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=12523s) | [📄](17-conditionals-if/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](17-conditionals-if/theory.ipynb "Theory notebook") [💻](17-conditionals-if/code.ipynb "Code notebook") |
| 18 | [if-else & the elif Ladder](18-if-else-elif/) | Choosing between two paths with `else` and between many with an `elif` ladder. | [`3:41:17`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=13277s) | [📄](18-if-else-elif/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](18-if-else-elif/code.ipynb "Code notebook") |
| 19 | [Nested if Statements](19-nested-if/) | Placing an `if` inside another `if` to model decisions that depend on earlier decisions. | [`3:56:24`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=14184s) | [📄](19-nested-if/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](19-nested-if/theory.ipynb "Theory notebook") [💻](19-nested-if/code.ipynb "Code notebook") |
| 20 | [Conditionals: Practice Questions](20-conditionals-practice/) | Practice: solving typical decision-making problems end to end. | [`4:04:18`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=14658s) | [📄](20-conditionals-practice/whiteboard-notes.pdf "Whiteboard notes (PDF)") [✏️](20-conditionals-practice/exercises-questions.ipynb "Exercises") [✏️](20-conditionals-practice/exercises-assignment.ipynb "Exercises") |
| 21 | [Introduction to Loops & the while Loop](21-while-loop/) | Repeating work with `while`, and avoiding the classic infinite loop. | [`4:19:50`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=15590s) | [📘](21-while-loop/theory.ipynb "Theory notebook") [💻](21-while-loop/code.ipynb "Code notebook") |
| 22 | [break, continue & pass](22-break-continue-pass/) | Controlling a loop from the inside: stop it with `break`, skip a round with `continue`, leave a placeholder with `pass`. | [`4:30:49`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=16249s) | [📘](22-break-continue-pass/theory.ipynb "Theory notebook") [💻](22-break-continue-pass/code.ipynb "Code notebook") |
| 23 | [The for Loop](23-for-loop/) | Looping over the items of a string or list with `for`. | [`4:48:36`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=17316s) | [💻](23-for-loop/code.ipynb "Code notebook") |
| 24 | [The range() Function](24-range-function/) | Generating number sequences with `range(stop)`, `range(start, stop)` and `range(start, stop, step)`. | [`5:00:29`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=18029s) | [💻](24-range-function/code.ipynb "Code notebook") |
| 25 | [Nested Loops](25-nested-loops/) | Putting one loop inside another to work with rows and columns. | [`5:20:55`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=19255s) | [💻](25-nested-loops/code.ipynb "Code notebook") |

### Data Structures

| # | Lesson | What you learn | Video | Files |
|---|--------|---------------|-------|-------|
| 26 | [Introduction to Data Structures](26-intro-data-structures/) | Why we need containers, and a map of the four built-in ones: list, tuple, set and dictionary. | [`5:33:56`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=20036s) | [📄](26-intro-data-structures/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](26-intro-data-structures/theory.ipynb "Theory notebook") |
| 27 | [Lists: Basics & Operations](27-lists/) | Creating lists, indexing, slicing, joining, repeating and editing them. | [`5:43:37`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=20617s) | [📄](27-lists/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](27-lists/code.ipynb "Code notebook") |
| 28 | [List Functions, Methods & Copying](28-list-functions-methods/) | The built-in functions and list methods you will use daily, and why `b = a` is not a copy. | [`6:01:49`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=21709s) | [📄](28-list-functions-methods/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](28-list-functions-methods/theory.ipynb "Theory notebook") [💻](28-list-functions-methods/code.ipynb "Code notebook") |
| 29 | [List Comprehension](29-list-comprehension/) | Building a list in one readable line with comprehensions, including conditions. | [`6:33:38`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=23618s) | [📄](29-list-comprehension/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](29-list-comprehension/theory.ipynb "Theory notebook") [💻](29-list-comprehension/code.ipynb "Code notebook") |
| 30 | [Tuples](30-tuples/) | Tuples: ordered, fixed collections, and how unpacking works. | [`6:48:42`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=24522s) | [📄](30-tuples/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](30-tuples/code.ipynb "Code notebook") |
| 31 | [Tuple Functions & Methods](31-tuple-functions-methods/) | The few tuple methods, and handy tricks such as swapping values. | [`6:48:42`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=24522s) | [📄](31-tuple-functions-methods/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](31-tuple-functions-methods/code.ipynb "Code notebook") |
| 32 | [Sets](32-sets/) | Sets: unordered collections of unique items, and why they are fast for membership checks. | [`7:18:01`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=26281s) | [📄](32-sets/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](32-sets/code.ipynb "Code notebook") |
| 33 | [Set Operations, Functions & Methods](33-set-operations/) | Set algebra: union, intersection, difference, subset checks, and safe ways to add or remove. | [`7:28:17`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=26897s) | [📄](33-set-operations/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](33-set-operations/code.ipynb "Code notebook") |
| 34 | [Dictionaries](34-dictionaries/) | Dictionaries: key-value pairs for fast lookup by name instead of by position. | [`7:48:58`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=28138s) | [📄](34-dictionaries/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](34-dictionaries/code.ipynb "Code notebook") |
| 35 | [Dictionary Operations & Methods](35-dictionary-functions-methods/) | Everyday dictionary methods and patterns such as counting and merging. | [`8:02:44`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=28964s) | [📄](35-dictionary-functions-methods/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](35-dictionary-functions-methods/code.ipynb "Code notebook") |
| 36 | [Strings Revisited: ord(), chr() & String Methods](36-string-methods/) | Characters as numbers with `ord()` and `chr()`, plus the string methods used to clean and search text. | [`8:19:30`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=29970s) | [📄](36-string-methods/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](36-string-methods/code.ipynb "Code notebook") |

### Functions & Functional Programming

| # | Lesson | What you learn | Video | Files |
|---|--------|---------------|-------|-------|
| 37 | [Introduction to Functions](37-intro-to-functions/) | What a function is, why we write them, and how to call one. | [`8:41:36`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=31296s) | [📄](37-intro-to-functions/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](37-intro-to-functions/code.ipynb "Code notebook") |
| 38 | [Defining Your Own Functions](38-defining-functions/) | Defining functions properly: parameters, return values, void functions and docstrings. | [`8:41:36`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=31296s) | [📄](38-defining-functions/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](38-defining-functions/code.ipynb "Code notebook") |
| 39 | [Types of Arguments: Positional & Default](39-argument-types/) | Passing values by position and giving parameters default values. | [`9:10:11`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=33011s) | [📄](39-argument-types/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](39-argument-types/theory.ipynb "Theory notebook") [💻](39-argument-types/code.ipynb "Code notebook") |
| 40 | [*args and **kwargs](40-args-kwargs/) | Accepting any number of arguments with `*args` and any number of named ones with `**kwargs`. | [`9:28:51`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=34131s) | [📄](40-args-kwargs/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](40-args-kwargs/code.ipynb "Code notebook") |
| 41 | [Variable Scope: Local vs Global](41-variable-scope/) | Where a variable lives: local, global, and what happens when the names clash. | [`9:40:20`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=34820s) | [📄](41-variable-scope/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](41-variable-scope/code.ipynb "Code notebook") |
| 42 | [Functions as First-Class Citizens](42-first-class-functions/) | Functions are values: store them, pass them around and return them. | [`9:56:08`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=35768s) | [📄](42-first-class-functions/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](42-first-class-functions/code.ipynb "Code notebook") |
| 43 | [Lambda Functions](43-lambda-functions/) | Short anonymous functions with `lambda`, and when not to use them. | [`10:22:04`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=37324s) | [📄](43-lambda-functions/whiteboard-notes.pdf "Whiteboard notes (PDF)") [📘](43-lambda-functions/theory.ipynb "Theory notebook") [💻](43-lambda-functions/code.ipynb "Code notebook") |
| 44 | [map(), filter() & reduce()](44-map-filter-reduce/) | Transforming, filtering and combining sequences with `map()`, `filter()` and `reduce()`. | [`10:32:38`](https://www.youtube.com/watch?v=J9BI0jGOds8&t=37958s) | [📄](44-map-filter-reduce/whiteboard-notes.pdf "Whiteboard notes (PDF)") [💻](44-map-filter-reduce/code.ipynb "Code notebook") |

### Checkpoint assignments

| Checkpoint | After lessons | Problems | Starter | Solutions |
|---|---|---|---|---|
| Setup & Basics | Lessons 01 to 03 | 5 | [notebook](../assignments/A1-setup-and-basics.ipynb) | [solutions](../assignments/solutions/A1-setup-and-basics.ipynb) |
| Data Types, Strings & Type Casting | Lessons 04 to 10 | 5 | [notebook](../assignments/A2-types-strings-casting.ipynb) | [solutions](../assignments/solutions/A2-types-strings-casting.ipynb) |
| Operators & String Formatting | Lessons 11 to 16 | 5 | [notebook](../assignments/A3-operators-formatting.ipynb) | [solutions](../assignments/solutions/A3-operators-formatting.ipynb) |
| Conditionals & Loops | Lessons 17 to 25 | 5 | [notebook](../assignments/A4-conditionals-loops.ipynb) | [solutions](../assignments/solutions/A4-conditionals-loops.ipynb) |
| Data Structures | Lessons 26 to 36 | 6 | [notebook](../assignments/A5-data-structures.ipynb) | [solutions](../assignments/solutions/A5-data-structures.ipynb) |
| Functions & Functional Programming | Lessons 37 to 44 | 6 | [notebook](../assignments/A6-functions.ipynb) | [solutions](../assignments/solutions/A6-functions.ipynb) |

[Course home](../README.md)
