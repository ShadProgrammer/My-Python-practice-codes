User_name=input('Enter your name,User:')                                                                       #Welcoming Statement
print("Welcome dear "+User_name+"\n\n1.Please guess the following patterns and check their answers below.")

Question_1=['_','25','125','625']       #Question1                                                        #Question1
print(Question_1)
ans1=input("Enter your answer: ")
Question_1.remove("_")
Question_1.insert(0,ans1)
print(Question_1)                    #Answer of Question1 entered by User

if Question_1==['5','25','125','625'] :  #If/else statement on User's answer
    print("It's true.")
else:
    print("Your answer is False.")
print("Correct answer is: ['5','25','125','625']")     #Correct Answer printed
print(input("Press Enter\n"))


Question_2=['7','21','35','49','_','77','91','_','119']   #Question2
print(Question_2)                                                                                 #Question2
ans2=input("Enter your 1st answer: ")
ans2_2=input("Enter your 2nd answer: ")
Question_2.remove("_")
Question_2.remove("_")
Question_2.insert(4,ans2)
Question_2.insert(7,ans2_2)
print(Question_2)                  #Answer of Question2 entered by User

if Question_2==['7','21','35','49','56','77','91','105','119']:  #If/else statement
    print("Answer is True.")
else:
    print("Your answer is False.")
print("Correct answers is: ['7','21','35','49','56','77','91','105','119']")     #Correct answer printed
print(input("Press Enter\n"))


Question_3=['10','90','170','250']          #Question3
print(Question_3)                                                                                   #Question3
ans3=input("Enter the number coming after 250: ")
Question_3.append(ans3)
print(Question_3)                      #Answer of Question3 entered by User

if Question_3==['10','90','170','250','330']:       #If/else statement
    print("Your answer is True.")
else:
    print("Your answer is not True.")
print("Correct answer is: ['10','90','170','250','330']")    #Correct answer printed


input("Press 'Enter' key to go for 2nd part.")     #2nd set of Questions


print("\n\n2.Change the gender in the following sentences:-")
Sentence_1=['A','boy','is','eating','his','apple.']     #Sentence1                                       #Sentence1
print(Sentence_1)
Ans1_1=(input("Enter where is to be corrected: "))
Ans1_2=(input("Enter corrected word: "))
if Ans1_1=="boy" or "his":                   #if/else statement
    if Ans1_2=="girl" or "her":              #Nested if
        print("Your answer is correct.")
else:
    print("Your answer is not correct.")
print("Correct answer is: ['A','girl','is','eating','her','apple.']\n")  #Correct answer printed


Sentence_2=['An','apple','is','eaten','by','him.']      #Sentence2                                       #Sentence2
print(Sentence_2)
Ans2_1=(input("Enter where is to be corrected: "))
Ans2_2=(input("Enter corrected word: "))
if Ans2_1=="him":                                 #if/else statement
    if Ans2_2=="her":              #Nested if
        print("Your answer is correct.")
else:
    print("Your answer is not correct.")
print("Correct answer is: ['An','apple','is','eaten','by','her.']\n")   #Correct answer printed

Sentence_3=['An','apple','was','given','to','him','by','his','father.']  #Sentence3                  #Sentence3
print(Sentence_3)
Ans3_1=(input("Enter where is to be corrected: "))
Ans3_2=(input("Enter corrected word: "))
if Ans3_1=="him" or "his":                  #If/else statement
    if Ans3_2=="her":                        #Nested if
        print("Your answer is correct.")
else:
    print("Your answer is not correct.")
print("Correct answer is: ['An','apple','was','given','to','her','by','her','father.']\n")  #Correct answer printed


print("\n\n\t\tThank You "+User_name+' for attending this questions.')           #Program ends.





