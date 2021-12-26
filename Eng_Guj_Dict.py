# How to get value of user's demanded word in dictionary.
meme='''Hello,
I am under* water*.
Please help me,
It's so cold* in here.
huuhuhhuu.
'''
print(meme)
gujdict={"under":"નીચે,",
         "water":"પાણી",
         "cold":"ઠંડુ"}
print("Options are:",gujdict.keys())
a=input("Enter word here: ")
print(gujdict.get(a))

# One program completed.
# How to take user's entered numbers in sets.

s1=int(input("Enter 1st number:"))         #Could be better by using loops
s2=int(input("Enter 2nd number:"))
s3=int(input("Enter 3rd number:"))
s4=int(input("Enter 4th number:"))
s5=int(input("Enter 5th number:"))
s6=int(input("Enter 6th number:"))
set1={s1,s2,s3,s4,s5,s6}
print(set1)

# Second program completed
# How to take user's entered numbers in lists.

l1=input("Enter 1st word or number to form a list: ")
l2=input("Enter 2nd word or number to form a list: ")
l3=input("Enter 3rd word or number to form a list: ")
l4=input("Enter 4th word or number to form a list: ")
l5=input("Enter 5th word or number to form a list: ")
l6=input("Enter 6th word or number to form a list: ")
list1=[l1,l2,l3,l4,l5,l6]
print(list1)

# Third program completed
# How to take user's entered numbers in tuples.

t1=input("Enter 1st tuple")
t2=input("Enter 2nd tuple")
t3=input("Enter 3rd tuple")
tuple1=(t1,t2,t3)
print(tuple1)

# All programs completed