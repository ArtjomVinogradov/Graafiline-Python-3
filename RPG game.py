import random as r

hp = 0
coins = 0
damage = 0

def printParameters():
    print("Sul on {0} elu, {1} kahjustus и {2} money.".format(hp, damage, coins))

def printHp():
    print("Sul on", hp, "elu.")

def printCoins():
    print("Sul on", coins, "money.")

def printDamage():
    print("Sul on", damage, "kahjustus.")

def meetShop():
    global hp
    global damage
    global coins

    def buy(cost):
        global coins
        if coins >= cost:
            coins -= cost
            printCoins()
            return True
        print("Sul pole raha mine perse!")
        return False

    weaponLvl = r.randint(1, 3)
    weaponDmg = r.randint(1, 5) * weaponLvl
    weapons = ["AK-47", "Iron Sword", "Showel", "Flower", "Bow", "Fish"]
    weaponRarities = ["Spoiled", "Rare", "Legendary"]
    weaponRarity = weaponRarities[weaponLvl - 1]
    weaponCost = r.randint(3, 10) * weaponLvl
    weapon = r.choice(weapons)

    oneHpCost = 5
    threeHpCost = 12

    print("Teel kohtasite kaupmeest!")
    printParameters()
    
    while input("Mida sa tegema hakkad (sisse/välja): ").lower() == "sisse":
        print("1) Üks terviseühik -", oneHpCost, "money;")
        print("2) Kolm terviseühik -", threeHpCost, "money;")
        print("3) {0} {1} - {2} money".format(weaponRarity, weapon, weaponCost))

        choice = input("Mida sa tahad osta: ")
        if choice == "1":
            if buy(oneHpCost):
                hp += 1
                printHp()
        elif choice == "2":
            if buy(threeHpCost):
                hp += 3
                printHp()
        elif choice == "3":
            if buy(weaponCost):
                damage = weaponDmg
                printDamage()
        else:
            print("Ma ei müü seda.")

def meetMonster():
    global hp
    global coins

    monsterLvl = r.randint(1, 3)
    monsterHp = monsterLvl
    monsterDmg = monsterLvl * 2 - 1
    monsters = ["Ludex Gundyr", "Crystal Sage", "Abyss Watchers", "High Lord Wolnir", "Dancer of the Boreal Valley", "Kalevi Poeg"]

    monster = r.choice(monsters)

    print("Sa kohtasid koletist - {0}, Tal on {1} level, {2} elu и {3} kahjustus.".format(monster, monsterLvl, monsterHp, monsterDmg))
    printParameters()

    while monsterHp > 0:
        choice = input("Mida sa teed (rünnata/jookse): ").lower()

        if choice == "rünnata":
            monsterHp -= damage
            print("Sa ründasid koletist ja tal on lahkunud", monsterHp, "elu.")
        elif choice == "jookse":
            chance = r.randint(0, monsterLvl)
            if chance == 0:
                print("Sul õnnestus lahinguväljalt põgeneda!")
                break
            else:
                print("Koletis oli liiga tugev ja jõudis sulle järele...")
        else:
            continue

        if monsterHp > 0:
            hp -= monsterDmg
            print("Koletis ründas ja olete lahkunud", hp, "elu.")
        
        if hp <= 0:
            break
    else:
        loot = r.randint(0, 2) + monsterLvl
        coins += loot
        print("Teil õnnestus koletis võita, mille eest saite", loot, "money.")
        printCoins()
    
def initGame(initHp, initCoins, initDamage):
    global hp
    global coins
    global damage

    hp = initHp
    coins = initCoins
    damage = initDamage

    print("Ты отправился в странствие навстречу приключениям и опасностям. Удачного путешествия!")
    printParameters()

def gameLoop():
    situation = r.randint(0, 10)

    if situation == 0:
        meetShop()
    elif situation == 1:
        meetMonster()
    else:
        input("Man, chill out my boy...")
    

initGame(3, 5, 1)

while True:
    gameLoop()

    if hp <= 0:
        if input("Хочешь начать сначала (да/нет): ").lower() == "да":
            initGame(3, 5, 1)
        else:
            break