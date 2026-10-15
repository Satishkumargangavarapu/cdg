#multiple import 
import biology, physics, calculator  # Output: no output; imports the three modules.

# #members are not imported
# print(dna())  # If uncommented: NameError because dna was not imported directly.
# b = Biology()  # If uncommented: NameError because Biology was not imported directly.
# print(b1)  # If uncommented: NameError because b1 was not imported directly.
# print(add(20,10))  # If uncommented: NameError because add was not imported directly.
# c = Calculator()  # If uncommented: NameError because Calculator was not imported directly.
# print(c1)  # If uncommented: NameError because c1 was not imported directly.
# print(newtonsfirst())  # If uncommented: NameError because newtonsfirst was not imported directly.
# p = Physics()  # If uncommented: NameError because Physics was not imported directly.
# print(p1)  # If uncommented: NameError because p1 was not imported directly.

#modules are imported 
print(biology.dna())  # Output: DNA: Carries genetic information.
b = biology.Biology()  # Output: no output; creates a Biology object.
print(biology.b1)  # Output: DNA
print(calculator.add(20,10))  # Output: 30
c = calculator.Calculator()  # Output: no output; creates a Calculator object.
print(calculator.c1)  # Output: 101
print(physics.newtonsfirst())  # Output: First Law: Intertia: Objects remain at rest or in uniform motion unless acted on by an external force.
p = physics.Physics()  # Output: no output; creates a Physics object.
print(physics.p1)  # Output: Einstein
