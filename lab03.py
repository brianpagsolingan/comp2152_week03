import random
#Dice options created using list() and range
diceOptions = list(range(1,7))
weapons = ["Fist", "Knife","Club","Gun","Bomb","Nuclear Bomb"]

print("Available weapons are ", ", ".join(weapons))

def getCombatStrength(prompt):
    while True:
        value = int(input(prompt))
        if 1 <= value <= 6:
            return value
        else:
            print("Invalid input, please enter a number between 1 - 6.")

combatStrength = getCombatStrength("Please enter a number between 1 and 6: ")
mCombatStrength = getCombatStrength("Please enter a number between 1 - 6 monster: ")

for i in range(1, 21 ,21):
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    heroTotal = combatStrength + heroRoll
    monsterTotal = mCombatStrength + monsterRoll

    print(f"\n Hero rolled {heroRoll}. Monster rolled {monsterRoll}")
    print(f"\n Hero weapon was {heroWeapon}. Monster weapon was {monsterWeapon}")
    print(f"\n Hero total strength was {heroTotal}. Monster total was {monsterTotal}")

    if heroTotal > monsterTotal:
        print("Player wins")
    elif monsterTotal > heroTotal:
        print("Monster wins")
    else:
        print("Tie")
if i != 11:
    print("Battle concluded after 20 rounds.")
