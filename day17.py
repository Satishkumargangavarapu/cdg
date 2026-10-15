def add(x, y):         
    return x + y  # Return value: the sum of x and y.
print(add(10,20))  # Not reached: the file contains a SyntaxError below.
print(type(add))  # Not reached: the file contains a SyntaxError below.

a = lambda x,y : x + y   
print(a(10,20))  # Not reached: the file contains a SyntaxError below.
print(type(a))  # Not reached: the file contains a SyntaxError below.

b = lambda (x,y) : x + y  # Error before execution: SyntaxError - lambda parameters cannot be parenthesized.
print(b(10,20))  # Not reached: the file cannot be parsed.

c = lambda x,y : return x + y  # Also invalid: SyntaxError - lambda cannot contain return.
print(c(10,20))  # Not reached: the file cannot be parsed.

# lambda function to return the sum of two numbers
# lambda function to return the square of a number
# lambda function to return the second element of a sequence

#tricky
a = lambda x : print(x+10), print(200), print(300)  # Not reached: the file cannot be parsed.
print(a)  # Not reached: the file cannot be parsed.
print(type(a))  # Not reached: the file cannot be parsed.

#map 
a = [1,2,3,4,5,6]
m = map(lambda x : x**2, a) 
print(m)  # Not reached: the file cannot be parsed.
print(type(m))  # Not reached: the file cannot be parsed.
l = list(m)     #1 4 9 16 25 36
print(l)  # Not reached: the file cannot be parsed.

#filter 
a = [1,2,3,4,5,6]
f = filter(lambda x : x % 2 == 0, a)
print(f)  # Not reached: the file cannot be parsed.
print(type(f))  # Not reached: the file cannot be parsed.
l = list(f)
print(l)  # Not reached: the file cannot be parsed.

#reduce 
import functools 
l = [1,2,3,4,5]
r = functools.reduce(lambda x,y : x+y, l) 
print(r)  # Not reached: the file cannot be parsed.
print(type(r))  # Not reached: the file cannot be parsed.
