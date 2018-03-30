import random

moneyInPot = int(input("how much do you want to put in the pot: "))
moneyLeft = moneyInPot
r = 1
largest=moneyInPot
while moneyLeft > 0:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print('round', r, 'die#1 =', die1, 'die#2 =', die2, end='')
    if die1 + die2 == 7:
        moneyLeft += 4
        if largest<moneyLeft:
            largest=moneyLeft
        print(' you win now you have', moneyLeft, '$ left')
    else:
        moneyLeft = moneyLeft - 1
        print(' you lose now you have', moneyLeft, '$ left')
    r += 1

print('the most mony you had was ',largest,'$')