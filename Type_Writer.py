from time import time,sleep
from random import choice

sentences = ["\t\t morphito embracink ambalo ephuno zotukno philaphin naruto instin dampharamdo.",
"\t\t abiano torusto gimphanako ruexem haphaniko quomphena viloaki namua abrizadon nikhila ostophi."]

print("Write the following text: ")
sleep(2)
text = choice(sentences)
print(text)

t1 = time()
c = input("Start:\n")
t2 = time()
t = t2 - t1

lst = text.split()
lstc = c.split()
accuracy = 100/len(lst) 
zero = 0

for i in range(len(lstc)):
    # print(lst[i])
    # print(lstc[i])
    if lst[i] == lstc[i]:
        zero += accuracy
    else:
        print("Error at: ")
        print(lst[i],end=":-")
        print(lstc[i])

print(f"You took {int(t)} seconds.")
try:
    print("Your accuracy: ",zero) 
except:
    print(None)
