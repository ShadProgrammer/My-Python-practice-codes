print("This programs contains some questions on Conjuction(Engish Grammer).Fill the below details to attempt the followng test.\n")
name=input('Enter your name:\n')
location={"Diu":"South_West-Gujarat",
          'Kachh':'Upper-Gujarat',
          'Bharuch':'South-Gujarat',
          'Baroda':'Middle-Gujarat'}

print("Options are:",location.keys())
a=input('Enter your location:\n',)
print("Your location:",location.get(a))     #Entering Users location

print("\n\nDetermine the conjuctions used in the sentences and break the sentence in 2 parts:-")


Q1=("I am alone but they are many.")
print(Q1)                                   #Question1
A1=(Q1.partition(input('Enter conjucton:\n')))
print(A1)                               #Answer1
print("Correct ans: ",Q1.partition('but'))                                  

Q2=("She is eating apple and orange")
print(Q2)                                     #Question2
A2=(Q2.partition(input('Enter conjuction:\n')))
print(A2)                               #Answer2
print("Correct ans: ",Q2.partition("and"))          

Q3=("I will learn Python or Chemistry.")
print(Q3)                                    #Question3
A3=(Q3.partition(input('Enter conjuction:\n')))
print(A3)                               #Answer3
print("Correct ans: ",Q3.partition("or"))                      

print("\n\nThanks for attending this questions, dear "+name)

