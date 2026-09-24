#if
# n = 1
# if n == 1:
#     print(1) # printing 1 from the if condition
# print(2) # 2
# print()

#if-else 
n = 10
if n == 10:
    print(1)  # printing 1 from the if condition
else:
    print(2) # if condition is true it will not print
print(3) # output is 3 beacause it is outside of the if condition
print()  # empty line for better readability
if n == 20:
    print(1) # if condition is false it will not print
else:
    print(2) # printing 2 from the else condition beacause if condition is false
print(3) # output is 3 beacause it is outside of the if condition
print() # empty line for better readability

#if-elif-else
n = 3
if n == 1:
    print(1) # if condition is false it will not print
elif n == 2:
    print(2) # if condition is false it will not print
elif n == 3:
    print(3) # if condition is true it will print 3
else:
    print(10) # if condition is true it will not print
print(11) # output is 11 beacause it is outside of the if condition
print() # empty line for better readability
n = 5
if n == 1:
    print(1) # if condition is false it will not print
elif n == 2:
    print(2) # if condition is false it will not print
elif n == 3:
    print(3) # if condition is false it will not print
else:
    print(10) # if condition is true it will print 10
print(11) # output is 11 beacause it is outside of the if condition

#nested-if
ch = 'A'  #one char
if ch.isalpha():
    if 65 <= ord(ch) <= 90:
        print('upper case letter') # printing upper case letter
    elif 97 <= ord(ch) <= 122:
        print('lower case letter') # if condition is true it will not print beacause ch is upper case letter
else:
    print('not an letter') # if condition is true it will not print
print(1) # output is 1 beacause it is outside of the if condition

#match case 
day = 5 
match day:
    case 1: 
        print('Sunday') # day is 5 so it will not print
    case 2:
        print('Monday') # day is 5 so it will not print
    case 3:
        print('Tuesday') # day is 5 so it will not print
    case 4:
        print('Wednesday') # day is 5 so it will not print
    case 5:
        print('Thursday') # day is 5 so it will print Thursday
    case 6: 
        print('Friday') # day is 5 so it will not print
    case 7:
        print('Saturday') # day is 5 so it will not print