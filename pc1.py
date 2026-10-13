#1
#1 2
#1 2 3
#1 2 3 4
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#1
#2 1
#3 2 1
#4 3 2 1
n=int(input())
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

# 1
# 1 1
# 1 1 1
# 1 1 1 1 
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(1,end=" ")
    print()

#    1
#   1 2
#  1 2 3
# 1 2 3 4
n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()


#    1
#   2 3
#  4 5 6
# 7 8 9 10
n=int(input())
count=1
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(count,end=" ")
        count+=1
    print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
n=int(input())
count=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(count,end=" ")
        count+=1
    print()


# a
# a b
# a b c
# a b c d
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
# A
# B A 
# C B A 
# D C B A 
n=int(input())
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(chr(64+j),end=" ")
    print()



