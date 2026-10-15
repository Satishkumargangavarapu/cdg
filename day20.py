# Import required modules
import math
import random
import sys
import platform
import collections
import itertools
from datetime import datetime, date, timedelta

#Math module
print('------------Math Module----------------')  # Output: ------------Math Module----------------
print('Square root of 25:', math.sqrt(25))  # Output: Square root of 25: 5.0
print('Power (2^3):', math.pow(2, 3))  # Output: Power (2^3): 8.0
print('Value of PI:', math.pi)  # Output: Value of PI: 3.141592653589793
print('Ceiling of 4.3:', math.ceil(4.3))  # Output: Ceiling of 4.3: 5
print('Ceiling of -4.3:', math.ceil(-4.3))  # Output: Ceiling of -4.3: -4
print('Floor of 4.8:', math.floor(4.8))  # Output: Floor of 4.8: 4
print('Floor of -4.8:', math.floor(-4.8))  # Output: Floor of -4.8: -5
print('Factorial of 5:', math.factorial(5))  # Output: Factorial of 5: 120
print('GCD of 12 and 18:', math.gcd(12, 18))  # Output: GCD of 12 and 18: 6
print('LCM of 12 and 18:', math.lcm(12,18))  # Output: LCM of 12 and 18: 36
print('Sine of 45 radians:', math.sin(45))  # Output: Sine of 45 radians: 0.8509035245341184
print('Cosine of 45 radians:', math.cos(45))  # Output: Cosine of 45 radians: 0.5253219888177297
print('Tangent of 45 radians:', math.tan(45))  # Output: Tangent of 45 radians: 1.6197751905438615
print('Degrees of 45 radians:', math.degrees(45))  # Output: Degrees of 45 radians: 2578.3100780887044
print('Radians of 45 degrees:', math.radians(45))  # Output: Radians of 45 degrees: 0.7853981633974483
print()  # Output: blank line
print()  # Output: blank line

# Random Module
print('-------------Random Module--------------')  # Output: -------------Random Module--------------
print('Random float between 0 and 1 including:', random.random())  # Output: a random float from 0.0 up to 1.0
# print(random.random(1,10))    #random will not take any argument
print('Random float from x to y including:', random.uniform(1,10))  # Output: a random float from 1.0 to 10.0
print('Random integer from x to y including:', random.randint(1, 100))  # Output: a random integer from 1 to 100
print('Random integer from 1 to 20 insteps of 2:', random.randrange(1,21,2))  # Output: 1, 3, 5, ..., or 19
#random with list
numbers = [10, 20, 30, 40, 50]
print('Random choice:', random.choice(numbers))  # Output: one of 10, 20, 30, 40, or 50
random.shuffle(numbers)
print('Shuffled list:', numbers)  # Output: numbers in a random order
print('Random sample:', random.sample(numbers, 3))  # Output: three randomly selected numbers
print()  # Output: blank line
print()  # Output: blank line


# Sys module
print('----------------Sys Module----------------')  # Output: ----------------Sys Module----------------
print('Python version:', sys.version)  # Output: the installed Python version and build information
print('Python executable:', sys.executable)  # Output: the path to the Python executable
print('Number of command-line arguments:', len(sys.argv))  # Output: 1 when run without extra arguments
print()  # Output: blank line
print()  # Output: blank line

# Platform Module
print('--------------Platform Module--------------')  # Output: --------------Platform Module--------------
print('Operating system:', platform.system())  # Output: the current operating system name
print('Machine:', platform.machine())  # Output: the machine architecture
print('Processor:', platform.processor())  # Output: the processor description
print('Python implementation:', platform.python_implementation())  # Output: CPython
print()  # Output: blank line
print()  # Output: blank line

# Collections Module
print('---------------Collections Module----------------')  # Output: ---------------Collections Module----------------
# Counter
words = ['rakesh', 'adhithya', 'rakesh', 'charan', 'adhithya', 'rakesh']
counter = collections.Counter(words)
print('Word count:', counter)  # Output: Word count: Counter({'rakesh': 3, 'adhithya': 2, 'charan': 1})
# Most common item
print('Most common:', counter.most_common(1))  # Output: Most common: [('rakesh', 3)]
print('Most common:', counter.most_common(2))  # Output: Most common: [('rakesh', 3), ('adhithya', 2)]
print()  # Output: blank line
# # DefaultDict
student_marks = collections.defaultdict(list)
student_marks['Alice'].append(90)
student_marks['Alice'].append(85)
student_marks['Bob'].append(78)
print('Student marks:', dict(student_marks))  # Output: Student marks: {'Alice': [90, 85], 'Bob': [78]}
print()  # Output: blank line
# # NamedTuple
Student = collections.namedtuple('Student', ['name', 'age', 'course'])
student = Student('John', 20, 'Python')
print('Student tuple:', student)  # Output: Student tuple: Student(name='John', age=20, course='Python')
print('Student name:', student.name)  # Output: Student name: John
print('Student age:', student.age)  # Output: Student age: 20
print('Student course:', student.course)  # Output: Student course: Python
print()  # Output: blank line
print()  # Output: blank line

# Itertools module
print('--------------Itertools Module--------------')  # Output: --------------Itertools Module--------------
items = ['A', 'B', 'C']
# Permutations
print('Permutations:')  # Output: Permutations:
permutations = itertools.permutations(items)
print(list(permutations))  # Output: [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
# Combinations
print('Combinations:')  # Output: Combinations:
combinations = itertools.combinations(items, 2)
print(list(combinations))  # Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]
# Product
print('Cartesian product:')  # Output: Cartesian product:
cproduct = itertools.product([1, 2], ['A', 'B'])
print(list(cproduct))  # Output: [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
print()  # Output: blank line
print()  # Output: blank line

# Datetime Module
print('------------------Datetime Module-------------------')  # Output: ------------------Datetime Module-------------------
# Current date and time
now = datetime.now()
print('Current date and time:', now)  # Output: the current date and time
# Current date
today = date.today()
print('Today\'s date:', today)  # Output: today's date
# Format date and time
print('Formatted date:', now.strftime('%d-%m-%Y'))  # Output: the current date in DD-MM-YYYY format
print('Formatted time:', now.strftime('%H:%M:%S'))  # Output: the current time in HH:MM:SS format
# Create a specific date time
birthday = datetime(2000, 5, 15, 19, 50, 50)
print('Example birthday:', birthday)  # Output: Example birthday: 2000-05-15 19:50:50
# Add days
future_date = today + timedelta(days=7)
print('Date after 7 days:', future_date)  # Output: the date seven days after today
# Subtract days
past_date = today - timedelta(days=7)
print('Date 7 days ago:', past_date)  # Output: the date seven days before today
