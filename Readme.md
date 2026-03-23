# Python Learning Repository

## 📌 About
This repository contains my daily Python practice code.  
Currently, I am in the learning phase and continuously improving my Python skills by writing code every day.

The goal of this repository is:
- To maintain consistency in coding
- To track my progress
- To practice Python concepts step by step
- To build a strong foundation in programming

I push code daily as part of my learning routine.

---

## 📂 Folder Structure
Each file in this repository represents practice code related to:
- Main.py (contains the material of tbe first unit) 
- Unit-2
- Unit -3
- Unit -4
- Unit -5

More topics will be added as I learn.

---

## ⚙️ Installation Process

Follow these steps to run the code on your system.

### 1. Install Python

Download Python from the official website:

https://www.python.org/downloads/

After installation, check version:
python --version

---


##  Running instructions 
### 1. open teminal 
### 2. set the correct path of the terminal 
### 3. python filename.py 
### 4. you can view your result 



# Python Crash Course – Revision Notes Chapter wise

-----------------------------------------
CHAPTER 1 — Getting Started
-----------------------------------------

• Python is a programming language used for web, AI, ML, automation, etc.
• Install Python from python.org
• Check installation:
    python --version

• First program:
    print("Hello World")

• Run file:
    python filename.py

• Use text editor / IDE:
    VS Code / Sublime / PyCharm

• Terminal is used to run programs

Key Points:
- Install Python
- Write code in .py file
- Run using terminal
- Fix errors carefully


-----------------------------------------
CHAPTER 2 — Variables and Simple Data Types
-----------------------------------------

Variable:
    name = "Suraj"

Rules:
- No spaces
- Cannot start with number
- Use lowercase

Strings:
    "hello"
    'hello'

String methods:
    name.title()
    name.upper()
    name.lower()

f-string:
    f"Hello {name}"

Numbers:
    int → 5
    float → 5.2

Operations:
    +  -  *  /  **  %

Constants:
    MAX_VALUE = 100

Comments:
    # this is comment

Zen of Python:
    import this


-----------------------------------------
CHAPTER 3 — Introducing Lists
-----------------------------------------

List:
    names = ["a", "b", "c"]

Access:
    names[0]

Last element:
    names[-1]

Modify:
    names[0] = "new"

Add:
    append()
    insert()

Remove:
    del
    pop()
    remove()

Sort:
    sort()
    sorted()

Reverse:
    reverse()

Length:
    len(list)

Important:
Index starts from 0


-----------------------------------------
CHAPTER 4 — Working with Lists
-----------------------------------------

Loop:
    for x in list:
        print(x)

Indentation is important

range():
    range(5)

Create numbers:
    list(range(1,6))

Statistics:
    min()
    max()
    sum()

List comprehension:
    squares = [x**2 for x in range(5)]

Slice:
    list[0:3]

Copy list:
    new = old[:]

Tuple (cannot change):
    t = (1,2,3)

Style:
- Use 4 spaces
- Keep code clean


-----------------------------------------
CHAPTER 5 — if Statements
-----------------------------------------

Condition:
    if x == 5:

Comparison:
==  !=  >  <  >=  <=

Check in list:
    if x in list

Boolean:
    True / False

if:
    if x == 5:
        print()

if-else:
    if x:
        ...
    else:
        ...

if-elif-else:
    if:
    elif:
    else:

Multiple conditions:
    and
    or

Check empty list:
    if list:

Good practice:
Keep indentation correct


-----------------------------------------
CHAPTER 6 — Dictionaries
-----------------------------------------

Dictionary:
    person = {"name": "suraj", "age": 20}

Access:
    person["name"]

Add:
    person["city"] = "Delhi"

Modify:
    person["age"] = 21

Remove:
    del person["age"]

Loop keys:
    for k in dict:

Loop values:
    for v in dict.values()

Loop both:
    for k,v in dict.items():

get():
    person.get("name")

Nesting:
list in dict
dict in list
dict in dict

Example:
users = [
    {"name": "a"},
    {"name": "b"}
]


-----------------------------------------
REVISION RULE
-----------------------------------------

Read daily
Practice daily
Write code daily

Goal:
Strong Python Basics