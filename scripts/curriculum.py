"""Single source of truth for the course layout.

Each Lesson maps one folder in the repo to:
  * the YouTube chapters it covers (timestamp, title)
  * the original files in the source folder ("Hello Python") and their new names

`build.py` reads this to copy files, generate READMEs and validate links.
Timestamps come from `docs/youtube-chapters.txt`. The class -> chapter mapping
is inferred from titles/contents, so spot-check it against the video.
"""
from dataclasses import dataclass, field

# kind -> (filename suffix used in repo, human label)
THEORY = "theory"
CODE = "code"
EXERCISE = "exercise"
PDF = "pdf"
SCRIPT = "script"


@dataclass
class Lesson:
    num: str                      # "01" ... "44"
    slug: str                     # folder name suffix
    title: str
    section: str                  # grouping used in the README tables
    chapters: list = field(default_factory=list)   # [(timestamp, title)]
    files: list = field(default_factory=list)      # [(source_rel, dest_name, kind)]
    note: str = ""

    @property
    def folder(self):
        # Lessons live at python/NN-<slug>
        return f"{self.num}-{self.slug}" if self.num[0].isdigit() else self.slug


def L(num, slug, title, section, chapters, files, note=""):
    return Lesson(num, slug, title, section, chapters, files, note)


WB = "whiteboard-notes.pdf"

# ---------------------------------------------------------------- Python lessons 01-44
SEC_SETUP = "Setup & Basics"
SEC_TYPES = "Data Types, Strings & Type Casting"
SEC_OPS = "Operators & String Formatting"
SEC_FLOW = "Conditionals & Loops"
SEC_DS = "Data Structures"
SEC_FUNC = "Functions & Functional Programming"
SEC_MORE = "Error Handling & OOP"

PART1 = [
    L("01", "introduction-to-python", "Introduction to Python", SEC_SETUP,
      [("0:00", "Intro: Master Python + AI"), ("2:38", "Why Do We Need Programming?"),
       ("6:45", "What Is Python & Where It's Used"), ("11:10", "Key Features of Python")],
      [("Class 1 - Introduction to Python/Introduction To Python.pdf", WB, PDF)]),
    L("02", "installing-python", "Installing Python & Setting Up Jupyter", SEC_SETUP,
      [("14:22", "Installing Python"), ("16:18", "Running Python in Terminal & IDLE"),
       ("20:31", "Anaconda & Jupyter Notebook Setup")],
      [("Class 2 - Installing python/How to Run python on your system.pdf", WB, PDF),
       ("Class 2 - Installing python/Installing Python.ipynb", "code.ipynb", CODE)]),
    L("03", "print-input-modules", "Built-in Functions, print(), Modules, Errors & Identifiers", SEC_SETUP,
      [("29:18", "Built-in Functions & print()"), ("35:42", "Python Modules (math, import)"),
       ("38:20", "Errors: Syntax vs Runtime"), ("43:59", "Identifiers & Naming Rules")],
      [("Class 3 - Print, Input and introdcution to Module/Module Print and Input.ipynb", "theory.ipynb", THEORY),
       ("Class 3 - Print, Input and introdcution to Module/Live Class Codes.ipynb", "code.ipynb", CODE)],
      note="No whiteboard PDF exists for this class."),
    L("04", "data-types", "Data Types", SEC_TYPES,
      [("51:57", "Data Types & Integers")],
      [("Class 4 - Data Types/Data Types in Python.pdf", WB, PDF),
       ("Class 4 - Data Types/Data Types Notes.ipynb", "theory.ipynb", THEORY),
       ("Class 4 - Data Types/Data Type In Python.ipynb", "code.ipynb", CODE)]),
    L("05", "numeric-data-types", "Numeric Types: int, float, complex", SEC_TYPES,
      [("51:57", "Data Types & Integers"), ("1:00:14", "Float Data Type"), ("1:03:13", "Complex Numbers")],
      [("Class 5  - Numeric Data Type/Numeric Data Type Copy.pdf", WB, PDF),
       ("Class 5  - Numeric Data Type/Numeric Data Type Explanation.ipynb", "theory.ipynb", THEORY),
       ("Class 5  - Numeric Data Type/Numeric Data Type.ipynb", "code.ipynb", CODE)]),
    L("06", "boolean", "Boolean Data Type", SEC_TYPES,
      [("1:06:20", "Boolean Data Type")],
      [("Class 6 - Bool Data Type/Bool Data Type Copy.pdf", WB, PDF),
       ("Class 6 - Bool Data Type/Bool Notes.ipynb", "theory.ipynb", THEORY),
       ("Class 6 - Bool Data Type/Boolean Data Type.ipynb", "code.ipynb", CODE)]),
    L("07", "strings", "Strings Basics", SEC_TYPES,
      [("1:12:28", "Strings Basics")],
      [("Class 7 - String Data Type/String Data.pdf", WB, PDF),
       ("Class 7 - String Data Type/String Notes.ipynb", "theory.ipynb", THEORY),
       ("Class 7 - String Data Type/String Data Type.ipynb", "code.ipynb", CODE)]),
    L("08", "indexing", "String Indexing (Positive & Negative)", SEC_TYPES,
      [("1:19:04", "String Indexing"), ("1:23:35", "Negative Indexing")],
      [("Class 8 - Indexing in python/Indexing In Python Copy.pdf", WB, PDF),
       ("Class 8 - Indexing in python/Indexing Notes.ipynb", "theory.ipynb", THEORY),
       ("Class 8 - Indexing in python/Indexing In Python.ipynb", "code.ipynb", CODE)]),
    L("09", "concatenation-slicing", "Concatenation, Repetition & Slicing", SEC_TYPES,
      [("1:27:35", "String Concatenation & Repetition"), ("1:33:40", "String Slicing"),
       ("1:50:14", "Slicing with Step Value")],
      [("Class 9 - Slicing In Python/Slicing In Python Copy.pdf", WB, PDF),
       ("Class 9 - Slicing In Python/concatenation and slicing in python.ipynb", "code.ipynb", CODE),
       ("Class 9.5 - Step in Slicing/Step in Python.ipynb", "code-step-in-slicing.ipynb", CODE)]),
    L("10", "type-casting", "Type Conversion & Type Casting", SEC_TYPES,
      [("2:01:13", "Type Conversion: Implicit"), ("2:07:12", "Explicit Type Casting")],
      [("Class 10 - Type Casting/Type Casting Copy.pdf", WB, PDF),
       ("Class 10 - Type Casting/Type Casting Notes.ipynb", "theory.ipynb", THEORY),
       ("Class 10 - Type Casting/Type Casting In Python.ipynb", "code.ipynb", CODE)]),
    L("11", "arithmetic-operators", "Operators Overview & Arithmetic Operators", SEC_OPS,
      [("2:15:50", "Operators in Python: Overview"), ("2:17:59", "Arithmetic Operators")],
      [("Class 11 - Operators in Python/Operators + Arithematic.pdf", WB, PDF),
       ("Class 11 - Operators in Python/Opeartors Notes.ipynb", "theory.ipynb", THEORY),
       ("Class 11 - Operators in Python/Operators in Python.ipynb", "code.ipynb", CODE)]),
    L("12", "relational-operators", "Relational Operators", SEC_OPS,
      [("2:26:08", "Relational Operators")],
      [("Class 12 - Relational Operators/Relational Operator.pdf", WB, PDF),
       ("Class 12 - Relational Operators/Relational Operators.ipynb", "theory.ipynb", THEORY),
       ("Class 12 - Relational Operators/Relational Operators Class Codes.ipynb", "code.ipynb", CODE)]),
    L("13", "logical-assignment-identity", "Logical, Assignment & Identity Operators", SEC_OPS,
      [("2:43:46", "Logical Operators"), ("2:53:03", "Assignment Operators"),
       ("2:58:11", "Identity Operators (is vs ==)")],
      [("Class 13 - Logical Assignment & Identity/Logical Assignment Identity.pdf", WB, PDF),
       ("Class 13 - Logical Assignment & Identity/Logical Membership & Identity.ipynb", "theory.ipynb", THEORY),
       ("Class 13 - Logical Assignment & Identity/Logical Assignment and Identity.ipynb", "code.ipynb", CODE)]),
    L("14", "membership-binary", "Membership & Binary (Bitwise) Operators", SEC_OPS,
      [],
      [("Class 14 - Membership & Binary/Membership + Binary.pdf", WB, PDF),
       ("Class 14 - Membership & Binary/Explanation - Membership + Binary.ipynb", "theory.ipynb", THEORY),
       ("Class 14 - Membership & Binary/Membership and Binary.ipynb", "code.ipynb", CODE)],
      ),
    L("15", "precedence-associativity", "Operator Precedence & Associativity", SEC_OPS,
      [("3:06:08", "Operator Precedence & Associativity")],
      [("Class 15 - Associativity and Precedence in Operator/Associativity + Precedance.pdf", WB, PDF),
       ("Class 15 - Associativity and Precedence in Operator/Associativity and Precedance for Operators.ipynb", "code.ipynb", CODE)]),
    L("16", "string-formatting", "String Formatting & f-Strings", SEC_OPS,
      [("3:13:46", "String Formatting"), ("3:25:07", "Python f-Strings")],
      [("Class 16 - String Formatting/Print Formatting.pdf", WB, PDF),
       ("Class 16 - String Formatting/Explained - String Formatting.ipynb", "theory.ipynb", THEORY),
       ("Class 16 - String Formatting/String Formatting in Python.ipynb", "code.ipynb", CODE)]),
    L("17", "conditionals-if", "Decision Control & the if Statement", SEC_FLOW,
      [("3:28:43", "Decision Control & if Statement")],
      [("Class 17 - Conditionals In Python + If/Conditionals -  Intro + If.pdf", WB, PDF),
       ("Class 17 - Conditionals In Python + If/Explained - Conditionals + If.ipynb", "theory.ipynb", THEORY),
       ("Class 17 - Conditionals In Python + If/Conditionals & IF statement Codes.ipynb", "code.ipynb", CODE)]),
    L("18", "if-else-elif", "if-else & the elif Ladder", SEC_FLOW,
      [("3:41:17", "if-else Statement"), ("3:47:03", "elif Ladder")],
      [("Class 18 - If Else/Conditionals - If Else.pdf", WB, PDF),
       ("Class 18 - If Else/Conditionals - If Else & If elif.ipynb", "code.ipynb", CODE)]),
    L("19", "nested-if", "Nested if Statements", SEC_FLOW,
      [("3:56:24", "Nested if Statements")],
      [("Class 19 - Nested If/Conditionals - Nested If.pdf", WB, PDF),
       ("Class 19 - Nested If/Nested If Explained.ipynb", "theory.ipynb", THEORY),
       ("Class 19 - Nested If/Nested If Codes.ipynb", "code.ipynb", CODE)]),
    L("20", "conditionals-practice", "Conditionals: Practice Questions", SEC_FLOW,
      [("4:04:18", "Conditionals: Practice Questions")],
      [("Class 20 - Conditional Questions/Conditionals - Questions.pdf", WB, PDF),
       ("Class 20 - Conditional Questions/Questions.ipynb", "exercises-questions.ipynb", EXERCISE),
       ("Class 20 - Conditional Questions/Assignment - Conditionals.ipynb", "exercises-assignment.ipynb", EXERCISE)]),
    L("21", "while-loop", "Introduction to Loops & the while Loop", SEC_FLOW,
      [("4:19:50", "while Loop")],
      [("Hello Python - Loops/Class 21 - Introduction to Loops and While Loop/Loops Explained.ipynb", "theory.ipynb", THEORY),
       ("Hello Python - Loops/Class 21 - Introduction to Loops and While Loop/Intro To Loops & While Loop.ipynb", "code.ipynb", CODE)],
      note="No whiteboard PDF exists for this class."),
    L("22", "break-continue-pass", "break, continue & pass", SEC_FLOW,
      [("4:30:49", "break Statement"), ("4:37:52", "continue Statement"), ("4:45:36", "pass Statement")],
      [("Hello Python - Loops/Class 22 - Break Continue Pass/Break Continue Pass Explained.ipynb", "theory.ipynb", THEORY),
       ("Hello Python - Loops/Class 22 - Break Continue Pass/Break Continue Pass.ipynb", "code.ipynb", CODE)]),
    L("23", "for-loop", "The for Loop", SEC_FLOW,
      [("4:48:36", "for Loop")],
      [("Hello Python - Loops/Class 23 - For Loop/For Loops in Python.ipynb", "code.ipynb", CODE)]),
    L("24", "range-function", "The range() Function", SEC_FLOW,
      [("5:00:29", "range() Function"), ("5:15:08", "for Loop with range()")],
      [("Hello Python - Loops/Class 24 - Range Function in Python/Range Function.ipynb", "code.ipynb", CODE)]),
    L("25", "nested-loops", "Nested Loops", SEC_FLOW,
      [("5:20:55", "Nested Loops")],
      [("Hello Python - Loops/Class 25 - Nested Loops/Nested Loops.ipynb", "code.ipynb", CODE)]),
    # ------------------------------------------------ data structures
    L("26", "intro-data-structures", "Introduction to Data Structures", SEC_DS,
      [("5:33:56", "Intro to Data Structures")],
      [("Data Structure/1. Intro To Data Structure/Intro To DS In Python.pdf", WB, PDF),
       ("Data Structure/1. Intro To Data Structure/Intro To Data Structure.ipynb", "theory.ipynb", THEORY)]),
    L("27", "lists", "Lists: Basics & Operations", SEC_DS,
      [("5:43:37", "Lists in Python"), ("5:54:24", "List Operations")],
      [("Data Structure/2. List Data Structure/Intro To List DS.pdf", WB, PDF),
       ("Data Structure/2. List Data Structure/List Data Structure.ipynb", "code.ipynb", CODE)]),
    L("28", "list-functions-methods", "List Functions, Methods & Copying", SEC_DS,
      [("6:01:49", "Built-in List Functions"), ("6:14:35", "List Methods"), ("6:28:20", "Copying Lists")],
      [("Data Structure/3. List - Methods and Functions/Methods & Function In List.pdf", WB, PDF),
       ("Data Structure/3. List - Methods and Functions/Methods and Functions Explained.ipynb", "theory.ipynb", THEORY),
       ("Data Structure/3. List - Methods and Functions/Methods & Fun Of List.ipynb", "code.ipynb", CODE)]),
    L("29", "list-comprehension", "List Comprehension", SEC_DS,
      [("6:33:38", "List Comprehension")],
      [("Data Structure/4. List Comprehension/List Comprehension.pdf", WB, PDF),
       ("Data Structure/4. List Comprehension/List Comprehension Explained.ipynb", "theory.ipynb", THEORY),
       ("Data Structure/4. List Comprehension/List Comprehension.ipynb", "code.ipynb", CODE)]),
    L("30", "tuples", "Tuples", SEC_DS,
      [("6:48:42", "Tuples")],
      [("Data Structure/5. Tuple Data Structure/Intro To Tupple.pdf", WB, PDF),
       ("Data Structure/5. Tuple Data Structure/Tuple Data Structure.ipynb", "code.ipynb", CODE)]),
    L("31", "tuple-functions-methods", "Tuple Functions & Methods", SEC_DS,
      [("6:48:42", "Tuples")],
      [("Data Structure/6. Tuple Functions and Methods/Tupple Function & Methods.pdf", WB, PDF),
       ("Data Structure/6. Tuple Functions and Methods/Function and Methods in Tuple.ipynb", "code.ipynb", CODE)],
      note="Covered inside the single 'Tuples' chapter (6:48:42 - 7:18:01)."),
    L("32", "sets", "Sets", SEC_DS,
      [("7:18:01", "Sets")],
      [("Data Structure/7. Intro To Sets/Intro To Sets.pdf", WB, PDF),
       ("Data Structure/7. Intro To Sets/Intro To Sets.ipynb", "code.ipynb", CODE)]),
    L("33", "set-operations", "Set Operations, Functions & Methods", SEC_DS,
      [("7:28:17", "Set Operations")],
      [("Data Structure/8. Set Methods and Function/Sets Function & Methods.pdf", WB, PDF),
       ("Data Structure/8. Set Methods and Function/Sets Function and Methods.ipynb", "code.ipynb", CODE)]),
    L("34", "dictionaries", "Dictionaries", SEC_DS,
      [("7:48:58", "Dictionaries")],
      [("Data Structure/9. Intro To Dictionary/Intro To Dictionary.pdf", WB, PDF),
       ("Data Structure/9. Intro To Dictionary/Dictionary.ipynb", "code.ipynb", CODE)]),
    L("35", "dictionary-functions-methods", "Dictionary Operations & Methods", SEC_DS,
      [("8:02:44", "Dictionary Operations & Methods")],
      [("Data Structure/10. Dictionary Methods and Functions/Dictionary Methods.pdf", WB, PDF),
       ("Data Structure/10. Dictionary Methods and Functions/Dict Function and Methods.ipynb", "code.ipynb", CODE)]),
    L("36", "string-methods", "Strings Revisited: ord(), chr() & String Methods", SEC_DS,
      [("8:19:30", "Strings Revisited: ord() & chr()"), ("8:26:41", "String Methods")],
      [("Data Structure/11. String in Python/Strings IN Python.pdf", WB, PDF),
       ("Data Structure/11. String in Python/String DS.ipynb", "code.ipynb", CODE)]),
    # ------------------------------------------------ functions
    L("37", "intro-to-functions", "Introduction to Functions", SEC_FUNC,
      [("8:41:36", "Defining Your Own Function"), ("8:48:01", "Return vs Void Functions"),
       ("8:59:32", "Functions: Core Concepts")],
      [("Hello Python - Functions/1. Intro To Functions/Intro To Functions.pdf", WB, PDF),
       ("Hello Python - Functions/1. Intro To Functions/Intro To Functions.ipynb", "code.ipynb", CODE)],
      note="Lessons 37 and 38 together span chapters 8:41:36 - 9:10:11."),
    L("38", "defining-functions", "Defining Your Own Functions", SEC_FUNC,
      [("8:41:36", "Defining Your Own Function"), ("8:48:01", "Return vs Void Functions"),
       ("8:59:32", "Functions: Core Concepts")],
      [("Hello Python - Functions/2. Defining your own function/Defining Our Own Function.pdf", WB, PDF),
       ("Hello Python - Functions/2. Defining your own function/Defining Our Own Function.ipynb", "code.ipynb", CODE)],
      note="Lessons 37 and 38 together span chapters 8:41:36 - 9:10:11."),
    L("39", "argument-types", "Types of Arguments: Positional & Default", SEC_FUNC,
      [("9:10:11", "Positional Arguments"), ("9:13:32", "Default Arguments")],
      [("Hello Python - Functions/3. Types of Arguments /Types Of Argument.pdf", WB, PDF),
       ("Hello Python - Functions/3. Types of Arguments /Types of Arguments Explained.ipynb", "theory.ipynb", THEORY),
       ("Hello Python - Functions/3. Types of Arguments /Arguments Types.ipynb", "code.ipynb", CODE)]),
    L("40", "args-kwargs", "*args and **kwargs", SEC_FUNC,
      [("9:28:51", "Variable-Length Arguments (*args)"), ("9:33:05", "Keyword Arguments (**kwargs)")],
      [("Hello Python - Functions/4. args and kwargs/args and kwargs In Python.pdf", WB, PDF),
       ("Hello Python - Functions/4. args and kwargs/args and kwargs.ipynb", "code.ipynb", CODE)]),
    L("41", "variable-scope", "Variable Scope: Local vs Global", SEC_FUNC,
      [("9:40:20", "Variable Scope: Local vs Global")],
      [("Hello Python - Functions/5. scope of variable/Scope Of Variable.pdf", WB, PDF),
       ("Hello Python - Functions/5. scope of variable/Scope of Variable.ipynb", "code.ipynb", CODE)]),
    L("42", "first-class-functions", "Functions as First-Class Citizens", SEC_FUNC,
      [("9:56:08", "Functions as First-Class Citizens")],
      [("Hello Python - Functions/6. Function are 1st class citizen/Function as 1st Class Citizen + Lambda.pdf", WB, PDF),
       ("Hello Python - Functions/6. Function are 1st class citizen/First Class Behaviour of Funciton.ipynb", "code.ipynb", CODE)]),
    L("43", "lambda-functions", "Lambda Functions", SEC_FUNC,
      [("10:22:04", "Lambda Functions")],
      [("Hello Python - Functions/7. Lambda Function /Lambda Function In Python.pdf", WB, PDF),
       ("Hello Python - Functions/7. Lambda Function /Lambda Explained.ipynb", "theory.ipynb", THEORY),
       ("Hello Python - Functions/7. Lambda Function /Lambda Functions In Python.ipynb", "code.ipynb", CODE)]),
    L("44", "map-filter-reduce", "map(), filter() & reduce()", SEC_FUNC,
      [("10:32:38", "map() Function"), ("10:37:07", "filter() Function"), ("10:43:06", "reduce() Function")],
      [("Hello Python - Functions/8. Map Filter and Reduce/Map Filter And Reduce Function.pdf", WB, PDF),
       ("Hello Python - Functions/8. Map Filter and Reduce/Map Filter Reduce.ipynb", "code.ipynb", CODE)]),
]

# ---------------------------------------------------------------- Lessons 45-46
# Lessons 45 and 46 (no video chapter)
ERRORS_LESSON = L(
    "45", "exception-handling", "Exception Handling", SEC_MORE,
    [],
    [("Error Handling/Exception Handling Notes.pdf", WB, PDF),
     ("Error Handling/Exception Handling Explained.ipynb", "theory.ipynb", THEORY),
     ("Error Handling/Error handling - Python.ipynb", "code.ipynb", CODE),
     ("Error Handling/Types of Exception.ipynb", "code-types-of-exception.ipynb", CODE),
     ("Error Handling/exception_handling_exercises_5.ipynb", "exercises.ipynb", EXERCISE)],
)

OOP = "OOPS Session/"   # lives next to the Hello Python folder in the source repo
OOP_LESSON = L(
    "46", "object-oriented-programming", "Object-Oriented Programming", SEC_MORE,
    [],
    [(OOP + "OOPS in Python Handwritten.pdf", WB, PDF),
     (OOP + "OOPS in Python.ipynb", "01-classes-and-objects.ipynb", CODE),
     (OOP + "Encapsulation.ipynb", "02-encapsulation.ipynb", CODE),
     (OOP + "Abstraction.ipynb", "03-abstraction.ipynb", CODE),
     (OOP + "Inheritance.ipynb", "04-inheritance.ipynb", CODE),
     (OOP + "Types of Inheritance Explained.ipynb", "05-types-of-inheritance-theory.ipynb", THEORY),
     (OOP + "Types Of Inheritance.ipynb", "05-types-of-inheritance.ipynb", CODE),
     (OOP + "Polymorhism.ipynb", "06-polymorphism-operator-overloading.ipynb", CODE),
     (OOP + "Complex Number Class.ipynb", "exercise-complex-number-class.ipynb", EXERCISE),
     (OOP + "Inheritance Questions.ipynb", "exercise-inheritance.ipynb", EXERCISE),
     (OOP + "Assignment/OOPS Question Set 1.py", "exercises/question-set-1-stack.py", SCRIPT),
     (OOP + "Assignment/OOPS Question 2.py", "exercises/question-set-2-bank-account.py", SCRIPT),
     (OOP + "Assignment/OOPS Snake and Ladder Game.py", "exercises/snake-and-ladder.py", SCRIPT)],
)

PART1.extend([ERRORS_LESSON, OOP_LESSON])   # lessons 45 and 46

# Source files deliberately NOT copied (scratch / artifacts), documented in docs/content-audit.md
EXCLUDED = [
    ("Class 4 - Data Types/Data Type- Reference.ipynb",
     "Pasted AI chat output ('Let's go through your notes...'), not course material."),
    ("Error Handling/Untitled.ipynb", "Scratch cell, duplicates a snippet already in the Error Handling notebooks."),
    ("OOPS Session/OOPS Class.ipynb", "Scratch notebook of half-finished function experiments."),
    ("**/.ipynb_checkpoints/", "Jupyter autosave checkpoints."),
    ("**/.DS_Store, **/Icon", "macOS metadata files."),
    (".claude/logs/", "Local Claude Code session log."),
]

# AI concepts chapter timestamps are defined in ai_terms.py
