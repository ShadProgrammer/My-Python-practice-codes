#This is Rushi's program.
'''
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=input("Enter the operator: ")
n=0

def plus(a,b):
    global n
    n=a+b
    print(n)

def minus(a,b):
    global n
    n=a-b
    print(n)

def multiply(a,b):
    global n
    n=a*b
    print(n)

def divide(a,b):
    global n
    n=a/b
    print(n)

if a%2==0:
    pass
else:
    a+=1

if b%2==0:
    b+=1

print(a)
print(b)

if c=="+":
    d=a+b
    plus(a,b)
elif c=="-":
    d=a-b
    minus(a,b)
elif c=="x" or "X":
    d=a*b
    multiply(a,b)
elif c=="/":
    d=a/b
    divide(a,b)
else:
    print("Input correct operator.")

if d==n:
    print("I did correct.")
elif d!=n:
    print("Oops, I didn't got right answer. Sorry for that, I am closing off.")


Problems:
1. Divide operator doesn't works properly.
2. Calculator last sentence is printed all time no matter if it's calculation is right.
'''

a=int(input("Enter 1st no.: "))
b=int(input("Enter 2nd no.: "))
p,q,m,n=0,0,0,0

p=a ; q=b

l=["+","-","x or X","/"]
print("Your options are: ",l)

c=input("Enter the operator: ")

 #Causing error in calculator LOLs
a=a+1
b=b+1

class Calculator:
    if c=="+":
        def add(self):
            m=a+b
            n=p+q
            print(m)
            print(n)

    if c=="-":
        def min(self):
            m=a-b   
            n=p-q
            print(m)

    if c=="x" or "X":
        def multiply(self):
            m=a*b   
            n=p*q
            print(m)

    if c=="/":
        def divide(self):
            m=a/b   
            n=p/q
            print(m)
    

one=Calculator()
if c=="+":
    one.add()
elif c=="-":
    one.min()
elif c=="x" or "X":
    one.multiply()
elif c=="/":
    one.divide()

print("Oops, I didn't got right answer. Sorry for that, I am closing off.")
