#single import
import calculator  # Output: no output; imports the calculator module.

# #members are not imported
# #functions
# print(add(20,10))  # If uncommented: NameError; add must be called as calculator.add.
# print(sub(20,10))  # If uncommented: NameError; sub must be called as calculator.sub.
# print(mul(20,10))  # If uncommented: NameError; mul must be called as calculator.mul.
# print(div(20,10))  # If uncommented: NameError; div must be called as calculator.div.
# #classes
# c = Calculator()  # If uncommented: NameError; Calculator must be called as calculator.Calculator.
# #objects 
# print(c1)  # If uncommented: NameError; c1 must be accessed as calculator.c1.
# print(c2)  # If uncommented: NameError; c2 must be accessed as calculator.c2.

#module is imported
#functions
print(calculator.add(20,10))  # Output: 30
print(calculator.sub(20,10))  # Output: 10
print(calculator.mul(20,10))  # Output: 200
print(calculator.div(20,10))  # Output: 2.0
#classes
c = calculator.Calculator()  # Output: no output; creates a Calculator object.
#objects 
print(calculator.c1)  # Output: 101
print(calculator.c2)  # Output: 201

 