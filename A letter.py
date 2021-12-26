print("Q.    Rewrite he following letter in which user can change [Name] ; and write it in proper manner.\n ")

print("Number 46,Marconi Street,Holland,")
print("Hello there,This letter is for NAME")
print("I am here to tell you about the program that the manager of our street")
print("is going to held it by tommorow.If you are going to particiapate in this program please reply")
print("back on this letter with 'YES'. Program is going to held on25November. Thank You.\n\n")

print("Ans.  Here is the letter how it should look like:-\n")

letter='''Number 46,                                                                                                                           
Marconi Street,
Holland\n

Hello there,
\t This letter is for [Name].I am here to tell you about the program that the manager of our street is going
\t to held it by tommorow. If you are going to participate in this program please reply back on this
\t letter with 'YES'. Program is going to held on following date
\t Date:-25 November

Thank You.'''                                                                                                                          #Salutation

print(letter.replace('[Name]',input('Type Name to whom you want to send:')))

b=(len('tommorow'))                 #Extra Strings
c=(letter.endswith('.'))
d=(letter.count('If'))
e=(letter.find('Marconi'))
##print(b)
##print(c)
##print(d)
##print(e)

input("Type Enter key to Exit program.")



