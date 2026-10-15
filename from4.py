#__all__ 
from physics import *  # Output: no output; imports public names from physics.
from calculator import *  # Output: no output; imports public names from calculator.
from biology import *  # Output: no output; imports public names from biology.

#all members of biology module
print(dna())  # Output: DNA: Carries genetic information.
print(genes())  # Output: Genes: Units of heredity that control traits.
b = Biology()  # Output: no output; creates a Biology object.
print(b1)  # Output: DNA
print(b2)  # Output: Protein
print()  # Output: blank line

#all members of physics module
print(newtonsfirst())  # Output: First Law: Intertia: Objects remain at rest or in uniform motion unless acted on by an external force.
print(newtonssecond())  # Output: Second Law: (F = ma): Acceleration is proportional to force and inversely proportional to mass.
print(newtonsthird())  # Output: (Trhid Law: Action-Reaction): Every action has an equal and opposite reaction.
p = Physics()  # Output: no output; creates a Physics object.
print(p1)  # Output: Einstein
print(p2)  # Output: Nikola Tesla
print()  # Output: blank line

#all members of calculator module
print(add(20,10))  # Output: 30
print(sub(20,10))  # Output: 10
print(mul(20,10))  # Output: 200
print(div(20,10))  # Output: 2.0
c = Calculator()  # Output: no output; creates a Calculator object.
print(c1)  # Output: 101
print(c2)  # Output: 201

# change __all__ of calculator(__all__ = ['add', 'c1']) and check