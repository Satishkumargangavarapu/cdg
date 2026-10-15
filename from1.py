#single member 
from calculator import add  # Output: no output; imports add.
from biology import genes  # Output: no output; imports genes.
from physics import newtonsfirst  # Output: no output; imports newtonsfirst.

# #module is not imported 
# print(calculator.add(20,10))  # If uncommented: NameError; calculator was not imported as a module.
# print(biology.genes())  # If uncommented: NameError; biology was not imported as a module.
# print(physics.newtonsfirst())  # If uncommented: NameError; physics was not imported as a module.

#written memebers are imported
print(add(20,10))  # Output: 30
print(genes())  # Output: Genes: Units of heredity that control traits.
print(newtonsfirst())  # Output: First Law: Intertia: Objects remain at rest or in uniform motion unless acted on by an external force.

# #other members are not imported
# print(sub(20,10))  # If uncommented: NameError; sub was not imported.
# print(newtonssecond())  # If uncommented: NameError; newtonssecond was not imported.
# print(dna())  # If uncommented: NameError; dna was not imported.