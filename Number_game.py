name=str(input("Enter your name: "))
x=int(input("Enter any rational no: "))
badge="None"

for i in range(1):
    opt_1=('''1. Multiply it by 10? OR 
    2. Multiply it by 11?''')
    print(opt_1)
    ch_1=int(input())
    if ch_1==1:
        (x*10)-50
        print(x)
    elif ch_1==2:
        (x*11)-50
        print(x)
    else:
        print("Game has been stopped because of your unexpected behaviour.")
        break
    opt_2=('''1. Multiply by 5 OR
    2. Multiply by 2?''')
    print(opt_2)
    ch_2=int(input())
    if ch_2==1:
        x*5
        print(x)
    elif ch_2==2:
        x*2
        print(x)
    else:
        print("Game has been stopped because of your unexpected behaviour.")
        break
    opt_3=('''1. Divide your number by 2? OR 
    2. Divide your number by 3? OR 
    3. Divide your number by 5?''')
    print(opt_3)
    ch_3=int(input())
    if ch_3==1:
        if x/2==0:
            print("Your number: ",x)
            badge="'Mastermind of this game'"
            print("Badge awarded: ",badge)
        elif x/2>0 and x/2=="<class 'float'>":
            print("Your number: ",x)
            badge="'Thug life'"
            print("Badge awarded: ",badge)
        elif x/2<0 and x/2=="<class 'float'>":
            print("Your number: ",x)
            badge="'Junior Pro'"
            print("Badge awarded: ",badge)
        elif x/2>0:
            print("Your number: ",x)
            badge="'King/Queen of the game'"
            print("Badge awarded: ",badge)
        elif x/2<0:
            print("Your number: ",x)
            badge="'Senior Pro"
            print("Badge awarded: ",badge)
        else:
            print("None")
    elif ch_3==2:
        if x/3==0:
            print("Your number: ",x)
            badge="'Mastermind of this game'"
            print("Badge awarded: ",badge)
        elif x/3>0 and x/3=="<class 'float'>":
            print("Your number: ",x)
            badge="'Thug life'"
            print("Badge awarded: ",badge)
        elif x/3<0 and x/3=="<class 'float'>":
            print("Your number: ",x)
            badge="'King/Queen of the game'"
            print("Badge awarded: ",badge)
        elif x/3>0:
            print("Your number: ",x)
            badge="'King/Queen of the game'"
            print("Badge awarded: ",badge)
        elif x/3<0:
            print("Your number: ",x)
            badge="'Senior Pro"
            print("Badge awarded: ",badge)
        else:
            print("None")
    elif ch_3==3:
        if x/5==0:
            print("Your number: ",x)
            badge="'Mastermind of this game'"
            print("Badge awarded: ",badge)
        elif x/5>0 and x/5=="<class 'float'>":
            print("Your number: ",x)
            badge="'Thug life'"
            print("Badge awarded: ",badge)
        elif x/5<0 and x/5=="<class 'float'>":
            badge="'King/Queen of the game'"
            print("Badge awarded: ",badge)
        elif x/5>0:
            print("Your number: ",x)
            badge="'King/Queen of the game'"
            print("Badge awarded: ",badge)
        elif x/5<0:
            print("Your number: ",x)
            badge="'Senior Pro"
            print("Badge awarded: ",badge)
        else:
            print("None")


with open("Game data.txt","a+") as game_data:
    print("Player's name: ",name)
    game_data.write(name)
    game_data.write("\n")
    game_data.write(badge)
    game_data.write("\n\n")
    

