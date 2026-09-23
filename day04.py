# #Arithmetic 

# # + : 
# a = 45 + 4.5 #49.5
# b = True + False #1
# c = 4+5j + 6+7j #10+12j
# d = None + 5 #Type Error
# e = [1,2,3] + [4,5,6] #[1,2,3,4,5,6]
# f = (1,2,3) + (4,5,6) #(1,2,3,4,.5,6)
# g = 'rak' + 'esh'
# h = range(1,4) + range(4,7)
# i = {1,2,3} + {4,5,5}
# j = {1:'a', 2:'b'} + {3:'c', 4:'d'}
# k = [1,2,3] + (1,2,3)
# l = [1,2,3] + 'rak'
# print(a)  # 49.5
# print(b)  # 1
# print(c)  # 10+12j
# print(d)  # TypeError
# print(e)  # [1, 2, 3, 4, 5, 6]
# print(f)  # (1, 2, 3, 4, 5, 6)
# print(g)  # rakesh
# print(h)  # TypeError
# print(i)  # TypeError
# print(j)  # TypeError
# print(k)  # TypeError
# print(l)  # TypeError

# # - : 
# a = 45 - 5.5
# b = 4+5j - 3+2j 
# c = True - False 
# d = [1,2,3] - [2,3]
# e = (1,2,3) - (2,3)
# f = {1,2,3,4} - {2,1}
# g = {1:'a', 2:'b', 3:'c'} - {2:'b', 3:'c'}
# print(a)  # 39.5
# print(b)  # (1+7j)
# print(c)  # TypeError
# print(d)  # TypeError
# print(e)  # TypeError
# print(f)  # {3, 4}
# print(g)  # TypeError

# #* : 
# a = 4 * 5.4
# b = True * False 
# c = (4+5j) * (3+2j)
# d = [1,2,3] * (2,3)
# e = [1,2,3] * 3 
# f = [1,2,3] * 3.0
# g = (1,2,3) * 3 
# h = 'rakesh' * 3 
# i = {1,2,3} * 3 
# j = {1:'a', 2:'b', 3:'c'} * 3
# k = [1,2,3]
# l = range(1,2,3)
# m = (4,5,6)
# print(a)  # 21.6
# print(b)  # 0
# print(c)  # (-2+22j)
# print(d)  # TypeError
# print(e)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# print(f)  # TypeError
# print(g)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)
# print(h)  # rakeshrakeshrakesh
# print(i)  # TypeError
# print(j)  # TypeError
# print(*k)  # 1 2 3
# print(*l)  # 1
# print(*m)  # 4 5 6

# # ** : power 
# a = 5 ** 2 
# b = 3 ** 2.3
# c = (3+4j) ** (1+2j)
# print(a)  # 25
# print(b)  # 12.806248474865697
# print(c)  # (-0.15701416981252564+0.0953008494313114j)

# # / :
# a = 5 / 2     
# print(a)  # 2.5

# # // : 
# a = 5 // 2     
# print(a)   # 2
# a = 5.5 // 2   
# print(a)  # 2.0

# # % : 
# a = 5 % 2 
# print(a)  # 1


# # #Relational Operators 
# print(5 == 6.5)  # False
# print(1 == True)  # True
# print(2 == None)  # False
# print(4+5j == 4+6j)  # False
# print(5 > 6.5)  # False
# print(1 > True)  # False
# print(2 > None)  # TypeError
# print(4+5j > 3+2j)  # TypeError
# print([1,2,3] == [1,2,4])  # False
# print([1,2,3] > [1,3,4])  # False
# print((1,2,3) > (1,3,4))  # False
# print({1,2,3} > {1,2})   # True
# # print({1:2, 2:3} > {3:4, 4:5})
# print({1:2, 2:3} == {1:2, 2:3})  # True
# print([1,2,3] == (1,2,3))  # False
# print([1,2,3] > (1,2,3))    # TypeError

# # #True or False
# print(bool(0))    #False  # False
# print(bool(4.5))  #True  # True
# print(bool(''))   #False  # False
# print(bool('r'))  #True  # True
# print(bool([]))   #False  # False
# print(bool([1]))  #True  # True
# print(bool(None))   # False

# print()  # 
# print()  # 
# # #Logical Operators
print( 4 and 0 and 6 )   #0  
print( 4 and 1 and 6 )   #6  
print( 4 or 0 or 6)      #4  
print(0 or '' or [])     #[]  
#mixed
print(4 or 0 and 6)     # 4
#not reverse the bool value
print(not False)   # True
print(not True)   # False

# #Assignment operator
# a = 10 
# a += 20 #30
# a -= 10 #20
# a *= 2  #40
# a **= 2 #1600
# a /= 2  #800
# a //= 3 #266.0
# a %= 3
# print(a)  # 2.0

# #Identity Operators 
# a = 34 
# b = 34 
# print(a is b)   # True
# a = 3+4j 
# b = 3+4j 
# print(a is b)   # False
# a = [1,2,3]
# b = [1,2,3]
# print(a is b)  # False
# a = 'rakesh'
# b = 'rakesh'
# print(a is b)  # True
# a = range(1,4)
# b = range(1,4)
# print(a is b)  # False
# a = (1,2,3)
# b = (1,2,3)
# print(a is b)  # True
# a = {1,2,3}
# b = {1,2,3}
# print(a is b)  # False
# print()  # 
# print()  # 

# #Membership 
# a = [1,2,3,4]
# b = {1,2,3,4}
# c = 'rakesh'
# d = (1,2,3,4)
# e = {1:'a', 2:'b', 3:'c'}
# f = range(1,4)
# print(5 in a)  # False
# print(3 in b)  # True
# print('r' in c)  # True
# print(4 in d)  # True
# print('b' in e)  # False
# print(3 in e)  # True
# print(4 in f)  # False

# #Walrus operator
# print(a = 4)
# print(a := 4)  # 4
# print(a)  # 4

# #ternary operator 
# a = 5 if 10 > 20 else 6 
# print(a)  # 6
# a = [1,2,3] if 5 < 10 else (1,2,3)
# print(a)  # [1, 2, 3]
