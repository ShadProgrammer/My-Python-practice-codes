print("This is phonebook of my friends.")
dict={
    "Diraq":"96438 XXXXX",
    "Dhruvik":"87993 XXXXX",
    "Dhruv":"98243 XXXXX",
    "Rushi":"82006 XXXXX",
    "Bhagya":"99041 XXXXX",
    "Pragya":"91403 XXXXX",
    "Dai":"63560 XXXXX",
    "Laxmita":"63560 XXXXX",
    "Bansi":"70160 XXXXX",
    "Taniya":"82005 XXXXX",
    "Viddhi":"82385 XXXXX"
}

print("Phonebook contains numbers of following names.")
print(dict.keys())

var_1=input("Enter name: ")
print(dict.get(var_1))
