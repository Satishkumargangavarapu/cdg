#multiple members
from calculator import add, sub  # Output: no output; imports add and sub.
from physics import newtonsfirst, newtonssecond  # Output: no output; imports both Newton-law functions.
from biology import dna  # Output: no output; imports dna.

print(add(20,10))  # Output: 30
print(sub(20,10))  # Output: 10
# print(calculator.sub(20,10))  # If uncommented: NameError because calculator was not imported as a module.
# print(mul(20,10))  # If uncommented: NameError because mul was not imported.


print(newtonsfirst())  # Output: First Law: Intertia: Objects remain at rest or in uniform motion unless acted on by an external force.
print(newtonssecond())  # Output: Second Law: (F = ma): Acceleration is proportional to force and inversely proportional to mass.
# print(physics.newtonssecond())  # If uncommented: NameError because physics was not imported as a module.
# print(newtonsthird())  # If uncommented: NameError because newtonsthird was not imported or defined.


print(dna())  # Output: DNA: Carries genetic information.
# print(biology.dna())  # If uncommented: NameError because biology was not imported as a module.
# print(genes())  # If uncommented: NameError because genes was not imported.
