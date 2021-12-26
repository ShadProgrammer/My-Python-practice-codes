# Game on flipping coins ~Best of 3~ 
P1=0   
P2=0               #Points
for i in range(100):        #It will never reach 100th round unless 1 or 2 is not printed continuously
    n_1=int(input("Enter 1 or 2: "))
    if n_1==1: 
        P1+=1
        print("Player 1 wins the flip.")
    elif n_1==2:
        P2+=1
        print("Player 2 wins the flip.")
    else: 
        print("Only 1 and 2 numbers can proceed output.")
    if P1==3:
        break
    elif P2==3:
        break
print("Game finish here!")
print("Player1's point: ",P1)
print("Player2's point: ",P2)