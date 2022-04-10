import random
import time
dragonhp=100
myhp=100


def fight():
    global dragonhp
    global myhp
    time.sleep(1.5)
    whoatt=random.randint(1,2)
    if whoatt == 1:
        print("You're lucky! It's time for your attack!")
        time.sleep(2.5)
        dragonhp = dragonhp - random.randint(5,8)
        print(f"Dragon's hp is {dragonhp}")
    elif whoatt == 2:
        print("Oh no.. The dragon attacks!")
        time.sleep(2.5)
        myhp = myhp - random.randint(5,8)
        print(f"Your hp is {myhp}")

print("Scared man - 'Hello, fighter!'")
time.sleep(2)
print("Scared man - 'You have to fight with the evil \nand save the world!'")
time.sleep(4)
print("Scared man - 'Can you do this for people?'")
time.sleep(2.5)
a=input("Scared man - 'Hmm?' y/n ")
time.sleep(0.5)

if a=="y":
    print("Scared man - 'OK, lets go!'")
    time.sleep(3)
    print("You are the Knight(100 hp)")
    time.sleep(2)
    print("Your enemy is the dragon(100 hp)")
    time.sleep(2)
    print("Scared man - 'Fight!'")
    time.sleep(1.7)
    pass
else:
    print("Scared man - 'You kill all of us, weak..'")
    time.sleep(3.2)
    print("You lose:(")

while myhp>0 or dragonhp>0:
    fight()

if myhp<=0:
    print("Scared man - 'Oh no...'")
    time.sleep(1.6)
    print("Scared man - 'Dragon will kill everyone of us!'")
    time.sleep(3.2)
    print("You're lose :(")
elif dragonhp<=0:
    print ("Scared man - 'Hooray!'")
    time.sleep(1.8)
    print("Scared man - 'You're save all of us, thank you!'\n 'You are our hero..'")
    time.sleep(1.9)