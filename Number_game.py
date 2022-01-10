name=str(input("Enter your name: "))
x=int(input("Enter any integer: "))
badge="None"

for i in range(1):
    opt_1=('''1. Multiply it by 10? OR 
    2. Multiply it by 11?''')
    print(opt_1)
    ch_1=int(input())
    if ch_1==1:
        x=(x*10)-50
        # print(x)
    elif ch_1==2:
        x=(x*11)-50
        # print(x)
    else:
        print("Game has been stopped because of your unexpected behaviour.")
        break
    opt_2=('''1. Multiply by 5 OR
    2. Multiply by 2?''')
    print(opt_2)
    ch_2=int(input())
    if ch_2==1:
        x=x*5
        # print(x)
    elif ch_2==2:
        x=x*2
        # print(x)
    else:
        print("Game has been stopped because of your unexpected behaviour.")
        break
    opt_3=('''1. Divide your number by 3? OR 
    2. Divide your number by 6? OR 
    3. Divide your number by 9?''')
    print(opt_3)
    ch_3=int(input())
    if ch_3==1:
        if x/2==0:
            badge="'Mastermind of this game'"
        elif x/2>0 and x/2=="<class 'float'>":
            badge="'Thug life'"
        elif x/2<0 and x/2=="<class 'float'>":
            badge="'Junior Pro'"
        elif x/2>0:
            badge="'King/Queen of the game'"
        elif x/2<0:
            badge="'Senior Pro"
        else:
            print("None")
    elif ch_3==2:
        if x/3==0:
            badge="'Mastermind of this game'"
        elif x/3>0 and x/3=="<class 'float'>":
            badge="'Thug life'"
        elif x/3<0 and x/3=="<class 'float'>":
            badge="'King/Queen of the game'"
        elif x/3>0:
            badge="'King/Queen of the game'"
        elif x/3<0:
            badge="'Senior Pro"
        else:
            print("None")
    elif ch_3==3:
        if x/5==0:
            badge="'Mastermind of this game'"
        elif x/5>0 and x/5=="<class 'float'>":
            badge="'Thug life'"
        elif x/5<0 and x/5=="<class 'float'>":
            badge="'King/Queen of the game'"
        elif x/5>0:
            badge="'King/Queen of the game'"
        elif x/5<0:
            badge="'Senior Pro"
        else:
            print("None")

print("Player's name: ",name)
print("Final number: ",x)
print("Badge: ",badge)

with open("Game data.txt","a+") as game_data:
    game_data.write("Player's name: ")
    game_data.write(name)
    game_data.write("\n")               #Why can't write() can't take more than 1 arguments? -_-
    game_data.write("Final number: ")
    game_data.write(str(x))
    game_data.write("\n")
    game_data.write(badge)
    game_data.write("\n\n")

print("Data saved succesfully in game data file.")
