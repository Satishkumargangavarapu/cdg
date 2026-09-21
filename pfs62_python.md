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







 

