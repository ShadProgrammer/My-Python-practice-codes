
from typing import Optional


name=input("Enter your name: ")
print("Welcome "+name+" to our shopping website, Salecart")
print("Please input the name of groceries below that you want to order.")

groceries={"Sugar":"Uttam sugar & Madhur Sugar",
       "Oil":"Fortune oil, Dhara Kachi Ghani oil & Freedom refined oil",
       "Dryfruits":"Farmely Premium",
       "Wheat":"Desi Choice & Ashirvaad Atta"}
print(groceries.keys()) 
a=(input("Enter grocery name that you are looking for from above list:\n"))

if (a=="Sugar"):
    print("Uttam sugar:1kg\n\t Rs 60\n\t Cheap\n\n"
          "Madhur sugar:1kg\n\t Rs50\n\t Cheap\n\n")
elif (a=="Oil"):
    print("Fortune oil: \nMustard oil\n 1L\n Rs200\n Moderate\n"
         "Dhara Kachi Ghani oil: \nMustard oil\n 1L\n Rs200\n Moderate\n"
         "Freedom Refined oil: \nSunflower oil\n 1L\n fRs150\n Cheap\n\n")
elif (a=="Dryfruits"):
    print("Farmely Premium: Kaju,Badam & Pista\n\t 1Kg\n\t Rs100\n\t Moderate\n")
elif (a=="Wheat"):
    print("Desi Choice: Normal wheat grains\n\t 100kg\n\t Rs300\n\t Cheap\n")
else:
    print("Sorry but we don't have your demanded item in our store.")   

gro=str(input("Please write your final order: "))

print("Thanks for making an order of "+gro+" from our website.We will deliever it as \nsoon as possible.Cash on delievery.")

print("\nThanks "+name+" for visiting our website.") 
  
