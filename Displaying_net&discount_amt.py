# Displaying Total sales amount,discount amount and net sales amount
qan=int(input("Enter total quantity: "))           
rate=int(input("Enter the rate: "))
tot=qan*rate                    #Using if-elif statements
if tot<=10000:
    dis=tot*(5/100)
    net=tot-dis
    print(f"Total units:{qan}")
    print(f"Rate:{rate}Rs")
    print(f"Total sales amount:{tot}Rs")
    print(f"Your discount:{dis}Rs")
    print(f"Net sales amount:{net}Rs")
elif tot<=50000:
    dis=tot*(10/100)
    net=tot-dis
    print(f"Total units: ",qan)
    print(f"Rate:{rate}Rs")
    print(f"Total sales amount:{tot}Rs")
    print(f"Your discount:{dis}Rs")
    print(f"Net sales amount:{net}Rs")
elif tot<=100000:
    dis=tot*(15/100)
    net=tot-dis
    print(f"Total units:{qan}")
    print(f"Rate:{rate}Rs")
    print(f"Total sales amount:{tot}Rs")
    print(f"Your discount{dis}Rs")
    print(f"Net sales amount:{net}Rs")
elif tot<=500000:
    dis=tot*(20/100)
    net=tot-dis
    print(f"Total units:{qan}Rs")
    print(f"Rate:{rate}Rs")
    print(f"Total sales amount:{tot}Rs")
    print(f"Your discount:{dis}Rs")
    print(f"Net sales amount:{net}Rs")
elif tot>500000:
    dis=tot*(25/100)
    net=tot-dis
    print(f"Total units:{qan}")
    print(f"Rate:{rate}Rs")
    print(f"Total sales amount:{tot}Rs")
    print(f"Your discount:{dis}Rs")
    print(f"Net sales amount:{net}Rs")