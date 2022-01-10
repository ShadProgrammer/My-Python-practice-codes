#This is Rushi's program.
'''
Using OOPs :
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
