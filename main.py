import random
import time

dragonhp = 100
myhp = 100


def checkhp():
    global myhp
    global dragonhp

    if myhp < 1:
        print("Scared man - 'Oh no...'")
        time.sleep(1.6)
        print("Scared man - 'Dragon will kill everyone of us!'")
        time.sleep(3.2)
        print("You're lose :(")
    elif dragonhp < 1:
        print("Scared man - 'Hooray!'")
        time.sleep(1.8)
        print("Scared man - 'You're save all of us, thank you!'\n 'You are our hero..'")
        time.sleep(1.9)


def fight():
    global dragonhp
    global myhp
    if dragonhp or myhp > 1:
        time.sleep(1.5)
        whoatt = random.randint(1, 2)
        if whoatt == 1:
            print("You're lucky! It's time for your attack!")
            time.sleep(1.5)
            dragonhp = dragonhp - random.randint(5, 10)
            print(f"Dragon's hp is {dragonhp}")
            fight()
        elif whoatt == 2:
            print("Oh no.. The dragon attacks!")
            time.sleep(1.5)
            myhp = myhp - random.randint(5, 10)
            print(f"Your hp is {myhp}")
            fight()
    else:
        checkhp()


name = input("Write your name, the knight: ")
print(f"Scared man - 'Hello, {name}!'")
time.sleep(2)
print("Scared man - 'You have to fight with the evil \nand save the world!'")
time.sleep(3.6)
print("Scared man - 'Can do you do this for people?'")
time.sleep(3.2)
a = input(f"Scared man - 'We are believe in you, {name}!' ok/no ")
time.sleep(0.5)

if a == "ok":
    print("Scared man - 'OK, lets go!'")
    time.sleep(3)
    print("You are the Knight(100 hp)")
    time.sleep(2)
    print("Your enemy is the dragon(100 hp)")
    time.sleep(2)
    print("Scared man - 'Fight him!'")
    time.sleep(1.7)
    fight()
else:
    print("Scared man - 'You kill all of us, weak..'")
    time.sleep(3.2)
    print("You lose:(")
