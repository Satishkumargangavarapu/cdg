Types of programming languages
1. Procedural programming Language (procedure -> order)
it is based on functions and step by step instructions. 
e.g. C
2. Object oriented programming language
Code is arranged in the form of classes and objects. 
e.g. Java, Python, C++
3. Functional programming language
Code is arranged in the form of functions
e.g. C, C++, Python
4. Modular programming language
Code is arranged in the form of modules
e.g. Modula3, python
5. Scripting Programming language
Code is without any functions and classes. sequence of steps mainly used in automation
e.g. bash, python
6. Declarative (declare)
you only tell what you want and not how to do it(no logic)
e.g. html, sql


Based on human understanding, programming languages can be divided into 3 types:
1. High Level: 
difficult for human to understand and communicates with the computer hardware directly
e.g. binary(e.g. 010010111), assembly(e.g. 8088 8002 2200)

2. Mid Level
easy for human to understand and also communicates with the computer hardware directly
e.g. C, C++

3. Low level
easy for human to understand but hides the communication with computer hardware
e.g. Python, Java


History of Python
Guido van Rossom started implementation in 1989 in NRI(national research institute), Netherlands and released in the year 1991. it is based on C, ABC, Module languages.

What does python support
1. Functional programming: you can write code in functions
2. Object oriented programming: you can write code in classes and objects
3. Modular programming: you can write code in modules 
4. scripting programming: you can write code without any functions and classes

features of python:
1. dynamically typed language:
in statically typed language we declare every datatype. It decides the datatypes at compiletime
in dynamically typed language we don't declare any datatype, they are decided by the interpreter when running the code at runtime
5
5.8
'rakesh'
2. interpreted language:
line by line translation and execution.

drawbacks of python:
slow in execution because of interpreted nature. Every time we run the program, it translates and executes
Whereas in java, only one time translation as a .class file, and every time we run the program .class file is executed skipping translation

different flavors of python:
jpython, cpython, rubypython, etc


token: smallest independent unit
e.g.
a = 10   #a is one token, = is one token, 10 is one token
statement: one line of instruction
a = 10   #a = 10 combinedly called one statement
NOTE: python statements can be separated by comma(,) and semicolon(;) also

Indentation: statements belonging to one suite(block) must be in same column
e.g. statements belonging to for loop, all must be in one column
     statements belonging to if must be in column 

identifiers: 
names given to functions, classes, objects etc (same like names of humans) 
naming rules:
1. identifiers can contain only alphabet, numbers and underscore
2. identifier cannot start with numbers
3. identifiers cannot be keywords
4. identifiers are case sensitive (a is not same as A)

keywords:
keywords are the reserved in a programming language, they have special meaning and purpose. e.g. 'while' is used for loop, 'if' is used for condition, 'try' is used for exception
prog:
import keyword
print(keyword.kwlist)      #prints all keywords
print(len(keyword.kwlist)) #35  


variables:
variable refers to an object
e.g. a = 10 (a refers to 10)
     a = 'rakesh'  (a refers to 'rakesh')

initialisation vs assignment:
declaration: declaring a variable
int a;        #not possible python
initialisation: giving initial value to the variable
a = 10        #10 is the first value given to a
assignment: assigning a variable to a object (assigning bodyguard to modi)
a = 10
re-assignment: changing the already available value to a different value
a = 10   #assignment
a = 20   #re-assignment

Multiple assignment:
a, b, c = 10, 20, 30  (assigning multiple variables to multiple values)
a = b = c = 10        (assigning multiple variables to single value)

Deleting the variable:
del variablename 
e.g.
a = b = c = 10
del a  #varaible a is deleted not 10
del b  #varaible b is deleted not 10
del c  #varaible c is, now all variable pointing to 10 is deleted so 10 also deleted

#NOTE: when variable is deleted only variable is deleted not the object, object is deleted automatically when no variables is pointing to it

Swapping the variables: 
a = 10
b = 20
a, b = b, a

interview question:
swapping two variables without third variable:
a = 10 
b = 20
1. 
a = a + b  (30)
b = a - b  (b = 30 - 20 = 10)
a = a - b  (a = 30 - 10 = 20)
2. 
a = a * b  (200)
b = a / b  (b = 200 / 20 = 10)
a = a / b  (a = 200 / 10 = 20)
3. 
a = a ^ b 
b = a ^ b  (b = (a^b)^b = a ^ b ^ b = a ^ 0 = a)
a = a ^ b  (a = (a^b)^a = a ^ b ^ a = 0 ^ b = b)
XOR properties:
A ^ A = 0 
A ^ 0 = A




Datatypes in python
Datatypes are divided into two types: Non-sequence and sequence. 
non-sequences hold single element, sequences hold multiple elements. 
Non-sequences: int, float, complex, bool, NoneType
Sequences: list, tuple, set, dict, str, range, frozenset, bytes, bytearray, memoryview


list: ordered collection of elements enclosed []. It is Mutable, allows different datatypes, allows duplicates
create: 
empty: [], list()
non-empty: [1,2,3,4]
NOTE: list() is a type conversion function, arg must be seq not separate elements
list(1,2,3,4)  #invalid
list('rakesh') #valid
list((1,2,3))  #valid

tuple: ordered collection of elements enclosed in (), () is optional and , is mandatory if single element. It is Immutable, allows different datatypes, allows duplicates 
create:
empty: (), tuple()
non-empty: (1,2,3,4)
NOTE: tuple() is a type conversion function, arg must be seq not separate elements 
tuple(1,2,3,4)   #invalid
tuple([1,2,3,4]) #valid
tuple('rakesh')  #valid

set: Unordered collection of elements enclosed in {}. It is Mutable(only adding, removing, not modifying), Allows only immutable objects, does not allow duplicates. 
create:
empty: set()  (no {}, {} is for dict)
non-empty: {1,2,3,4}
NOTE: set() is a type conversion function, arg is seq not separate elements
set(1,2,3,4)   #invalid
set('rakesh')  #valid
set([1,2,3,4]) #valid

frozenset: Unordered collection of elements enclosed in frozenset({}). It is same like set, except it is immutable.
empty: frozenset()
non-empty: 
frozenset({1,2,3,4})
frozenset([1,2,3,4])


dict: Ordered collection of key : value pairs enclosed in {}. It is mutable, allows only immutable keys and any values, will not allow duplicate keys.
empty: {}, dict()
non-empty:
{1:'a', 2:'c', 3:'d'}
NOTE: dict is a type conversion function. argument must be a sequence of pairs
dict([ [1,2], [3,4], [5,6] ])

str: Ordered collection of characters enclosed in single, double, triple quotes. single and double can be used interchangeably, triple quotes are used for multi-line string.
create:
a = 'rakesh'
a = "rakesh"
a = '''
line1
line2
line3
'''
NOTE: str() is a type conversion function
str(2)
str(3.5)
str([1,2,3])
str({1,2,3})

range: Ordered collection of integers. syntax: range(start:stop:step). step can only be integer and cannot be zero. It is immutable, allows only integer type and no duplicates


bytes, bytearray, memoryview are needed to work with raw binary data. each index is a byte, combination of bytes are enough to represent anything

In Python, set methods are built-in functions used to manipulate and perform mathematical operations on set objects (unordered collections of unique items).1. Modifying a SetThese methods change the contents of the set directly.add(element): Adds a single element to the set. If the item exists, nothing changes.update(iterable): Adds multiple elements from another collection (list, tuple, set).remove(element): Deletes an element. Raises a KeyError if the element is not found.discard(element): Deletes an element, but does not throw an error if the element is missing.pop(): Removes and returns an arbitrary element. Throws an error if the set is empty.clear(): Removes all elements, leaving an empty set.pythonfruits = {"apple", "banana"}

fruits.add("orange")        # {"apple", "banana", "orange"}
fruits.update(["grape", "mango"]) # Adds multiple items
fruits.discard("pear")      # Safe delete (does nothing since 'pear' isn't there)


Use code with caution.2. Mathematical & Comparison OperationsThese methods allow you to compare sets or find relationships between them. Most of these return a new set unless they end in _update.OperationMethodAlternative OperatorDescriptionUnionsetA.union(setB)setA | setBReturns all items from both sets.IntersectionsetA.intersection(setB)setA & setBReturns only items present in both sets.DifferencesetA.difference(setB)setA - setBReturns items in A that are not in B.Symmetric Diff.setA.symmetric_difference(setB)setA ^ setBReturns items in either A or B, but not both.Is Sub-set?setA.issubset(setB)setA <= setBReturns True if all elements of A are in B.Is Super-set?setA.issuperset(setB)setA >= setBReturns True if A contains all elements of B.Is Disjoint?setA.isdisjoint(setB)NoneReturns True if A and B have zero items in common.pythonset_a = {1, 2, 3}
set_b = {3, 4, 5}

# Examples
print(set_a.union(set_b))         # Output: {1, 2, 3, 4, 5}
print(set_a.intersection(set_b))  # Output: {3}
print(set_a.difference(set_b))    # Output: {1, 2}
Use code with caution.3. In-Place UpdatesIf you want to perform a mathematical operation and overwrite the original set instead of creating a new one, use the _update versions:setA.intersection_update(setB)setA.difference_update(setB)setA.symmetric_difference_update(setB)


In Python, dictionary methods are built-in functions used to access, modify, and manage key-value pairs.1. Accessing Keys, Values, and ItemsThese methods let you safely retrieve data or look at the structure of your dictionary.get(key, default): Retrieves the value for a key. Returns None (or a custom default) instead of crashing if the key doesn't exist.keys(): Returns a dynamic view of all keys in the dictionary.values(): Returns a dynamic view of all values in the dictionary.items(): Returns a dynamic view of all key-value pairs as tuples (key, value).pythonuser = {"name": "Alice", "role": "Admin"}

print(user.get("age", "Not Provided"))  # Output: Not Provided (Safe lookup)
print(list(user.keys()))                # Output: ['name', 'role']
print(list(user.items()))               # Output: [('name', 'Alice'), ('role', 'Admin')]
Use code with caution.2. Adding and Modifying DataThese methods help you insert new data or update existing entries.update(iterable): Merges another dictionary or an iterable of key-value pairs into the current one, overwriting existing keys.setdefault(key, default): Returns the value of a key if it exists. If it doesn't, it inserts the key with the specified default value.pythonprofile = {"name": "Bob"}

# Merge data
profile.update({"age": 30, "city": "Mumbai"}) 

# Ensures 'theme' exists without overwriting if it's already there
profile.setdefault("theme", "dark") 
Use code with caution.3. Removing DataThese methods delete specific items or clear out the entire structure.pop(key, default): Removes the key and returns its value. If the key isn't found, it returns the default value (or raises a KeyError if no default is set).popitem(): Removes and returns the last inserted key-value pair as a tuple.clear(): Removes all items, leaving an empty dictionary {}.pythondata = {"id": 101, "status": "active", "temp": True}

status = data.pop("status")  # Removes 'status' and returns 'active'
last_item = data.popitem()   # Removes and returns ('temp', True)
Use code with caution.4. Creating and Copyingcopy(): Returns a shallow copy of the dictionary.fromkeys(iterable, value): A class method that creates a brand new dictionary using elements from an iterable as keys, all set to the same value.python# Create a dictionary with default starting scores
players = ["player1", "player2", "player3"]
scoreboard = dict.fromkeys(players, 0)  # {'player1': 0, 'player2': 0, 'player3':


 

In Python, list methods are built-in functions used to modify, search, and manage ordered sequences of items.

1. Adding ElementsThese methods let you insert new items into a list.


append(element): Adds an item to the very end of the list.

extend(iterable): Appends multiple items from another collection (like a list or tuple) to the end.

insert(index, element): Inserts an item at a specific position.


pythonnumbers = [1, 2]

numbers.append(3)         # [1, 2, 3]
numbers.extend([4, 5])     # [1, 2, 3, 4, 5]
numbers.insert(0, 0)      # [0, 1, 2, 3, 4, 5] (Inserts 0 at the beginning)

Use code with caution.

2. Removing ElementsThese methods delete items from a list based on their value or position.

remove(element): Deletes the first occurrence of a specific value. Raises a ValueError if the item isn't found.

pop(index): Removes and returns the item at a specific position. If no index is given, it removes the last item.

clear(): Removes all items, leaving an empty list [].

pythonletters = ["a", "b", "c", "b"]

letters.remove("b")  # ['a', 'c', 'b'] (Only removes the first 'b')
last = letters.pop() # Removes 'b' and returns it; list is now ['a', 'c']
Use code with caution.

3. Searching and CountingThese methods help you find items or count how many times they appear.

index(element, start, end): Returns the position (index) of the first occurrence of a value.

 Throws an error if missing.
 
 count(element): Returns the total number of times an item appears in the list.
 
 pythonitems = ["apple", "banana", "apple"]

print(items.index("banana")) # Output: 1
print(items.count("apple"))  # Output: 2

Use code with caution.

4. Ordering and CopyingThese methods change the arrangement of the list or duplicate it.

sort(key, reverse): Sorts the list items in-place (changes the original list).

reverse(): Reverses the order of the elements in-place.

copy(): Returns a shallow copy of the list.pythonscores = [10, 50, 20]

scores.sort()     # [10, 20, 50] (Sorted lowest to highest)
scores.reverse()  # [50, 20, 10] (Reversed order)