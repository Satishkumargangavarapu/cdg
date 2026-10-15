#alias
from calculator import add as a  # Output: no output; imports add as a.
from physics import newtonsfirst as nf  # Output: no output; imports newtonsfirst as nf.
from biology import genes as g  # Output: no output; imports genes as g.

# print(add(20,10))  # If uncommented: NameError; add was imported with alias a.
print(a(20,10))  # Output: 30
# print(newtonsfirst())  # If uncommented: NameError; newtonsfirst was imported with alias nf.
print(nf())  # Output: First Law: Intertia: Objects remain at rest or in uniform motion unless acted on by an external force.
# print(genes())  # If uncommented: NameError; genes was imported with alias g.
print(g())  # Output: Genes: Units of heredity that control traits.
