import datetime
import random
name=input("What your name")

while True:
    answer = input("I am the magic eight ball" + str(name) + "Whats your wish!(Type stop if you want to quit.)")
    randnum = random.randint(0, 3)
    if randnum == 0:
        print("no chances at all for " + str(answer))
    elif randnum == 1:
        print("you will get to " + str(answer))
    elif randnum == 2:
        print("there is a good chance of" + str(answer))
    else:
        print("you will not get this outcome")
    if answer=="stop":
        break
    else:
        continue


print("The end")