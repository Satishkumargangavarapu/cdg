#terminates the program, no alternate action
print('1')  # Output: 1
print('2')  # Output: 2
a = 4 / 0  # Raises ZeroDivisionError; no value is assigned to a.
print('3')  # Not reached because the previous line raises ZeroDivisionError.
print('4')  # Not reached because the previous line raises ZeroDivisionError.

# # performs alternate action and continues the program
print('1')  # Output: 1
print('2')  # Output: 2
try:
    a = 4 / 0
except ZeroDivisionError:
    print("message: Zero Division Error has occured")  # Output: message: Zero Division Error has occured
print('3')  # Output: 3
print('4')  # Output: 4

try:
    print('Examples of syntax errors')  # Not reached: the file has syntax errors before execution.
    a = (1,2,3))     #unmatched paranthesis
    s = "rakesh""    #unmatched quotes
    5 = x            #invalid assignment
    l = [1 2 3]      #missing comma 
    if = 21          #using keywords
    a = 10 
        b = 20       #incorrect indentation
    if 10            #missing colon
        print(True)  # Not reached: the file has syntax errors before execution.
except:
    print('except suite')  # Not reached: syntax errors are not caught by try/except.



a = 10 / 0
try:
    print("Examples of runtime errors")  # Output if this section is run independently: Examples of runtime errors
    x = 10 / 0 
    print(y)  # Not reached: x = 10 / 0 raises ZeroDivisionError first.
    a = [1, 2, 3]; print(a[5])  # Not reached: x = 10 / 0 raises ZeroDivisionError first.
    d = {"a": 1}; print(d["b"])  # Not reached: x = 10 / 0 raises ZeroDivisionError first.
    int("abc")                   
    "a" + 10                    
    import abcdef                
except IndexError:
    print(1)  # Output: 1
except IndexError:
    print(2)  # Unreachable duplicate handler.
except KeyError as ke:
    print(3, ke)  # Output: 3 followed by the KeyError message.
except (ValueError, TypeError):
    print(4)  # Output: 4
# except (ValueError as ve, TypeError as te):
#     pass 
except (ValueError, TypeError) as e:
    pass
except ZeroDivisionError:
    print(5)  # Output: 5
#catch-all
except Exception as e:
    print(6)  # Output: 6
except:
    print(7)  # Output: 7
except as e:
    pass



#not handling error
try:
    a = 10 / 0 
except IndexError:
    print(1)  # Not reached: ZeroDivisionError is not handled here.
except ModuleNotFoundError:
    print(2)  # Not reached: ZeroDivisionError is not handled here.
print(3)  # Not reached: the exception escapes the try/except statement.
print(4)  # Not reached: the exception escapes the try/except statement.



# else and finally
try:
    a = 10 / 4 
except IndexError:
    print(1)  # Not reached: division by 4 succeeds.
except ZeroDivisionError:
    print(2)  # Not reached: division by 4 succeeds.
else:
    print(3)  # Output: 3
finally:
    print(4)  # Output: 4



try:
    a = 10 / 0
except IndexError:
    print(1)  # Not reached: ZeroDivisionError is handled below.
except ZeroDivisionError:
    print(2)  # Output: 2
else:
    print(3)  # Not reached: the except block runs.
finally:
    print(4)  # Output: 4
    



# #finally
try:
    a = 10 / 0 
except IndexError:
    print(1)  # Not reached: ZeroDivisionError is not an IndexError.
except ModuleNotFoundError:
    print(2)  # Not reached: ZeroDivisionError is not a ModuleNotFoundError.
finally:
    print(3)  # Output: 3
print(4)  # Output: 4









# #Handle child error before parent error
try:
    10 % 0 
except ArithmeticError:
    print('Arithmetic Error')  # Output: Arithmetic Error
except ZeroDivisionError:
    print('Zero Division Error')  # Unreachable: ZeroDivisionError is an ArithmeticError.


# # reorder
try:
    10 % 0 
except ZeroDivisionError:
    print('ZeroDivisionError')  # Output: ZeroDivisionError
except ArithmeticError:
    print('ArithmeticError')  # Unreachable: the ZeroDivisionError handler runs first.


# #User defined excecption and raise 
# #simple UDE
class StudentAlreadyExists(Exception):
    pass 
raise StudentAlreadyExists('Student with rollno 23 already exists')
print(1)  # Not reached: the previous raise stops execution.
raise StudentAlreadyExists('Student with rollno 22 already exists')
print(2)  # Not reached: the previous raise stops execution.




# #Parameterized UDE
class StudentNotFound(Exception):
    def __init__(self, rollno, name):
        self.rollno = rollno 
        self.name = name 
        #if this is not there, when object is printed prints tuple of all passed values
        super().__init__(f'Student rollno: {rollno} with name {name} is not found')




# raise StudentNotFound(1, 'rakesh')
# raise StudentNotFound(2, 'adhithya')
try:
    raise StudentNotFound(1, 'rakesh')
except StudentNotFound as snf:
    print(snf)  # Output: Student rollno: 1 with name rakesh is not found
    print(snf.rollno)  # Output: 1
    print(snf.name)  # Output: rakesh
