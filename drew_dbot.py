import random

def rollDie():
    #Rolls a die
    min = 1
    max = 6
    roll = random.randint(min, max,)
    return roll

def GhostyMcGhostface(numberOfRolls):
    diceRolls = []

    for i in range(1, numberOfRolls):
        diceRolls.append(rollDie())

    if diceRolls[0] == 6:
        return str(sum(diceRolls) - 6) + ' and a ghost. Hold onto your butts!'
    else:
        return str(sum(diceRolls)) + '.'
