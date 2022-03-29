import random
import time


class Player():
    def __init__(self, name):
        self.health = 100
        self.name = name
        self.wins = 0

    def calculate_damage(self, damage_amount, attacker):
        if (damage_amount > self.health):
            overkill = abs(self.health - damage_amount)
            self.health = 0
            if (overkill > 0):
                print("{0} takes fatal damage from {1}, with {2} overkill!"
                      .format(self.name.capitalize(), attacker, overkill))
            else:
                print("{0} takes fatal damage from {1}!"
                      .format(self.name.capitalize(), attacker))
        else:
            self.health -= damage_amount
            print("{0} takes {1} damage from {2}!"
                  .format(self.name.capitalize(), damage_amount, attacker))

    def calculate_heal(self, heal_amount):
        if (heal_amount + self.health > 100):
            self.health = 100
            print("{0} heals back to full health!"
                  .format(self.name.capitalize()))
        else:
            self.health += heal_amount
            print("{0} heals for {1}!"
                  .format(self.name.capitalize(), heal_amount))


def parse_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False


def get_selection():
    valid_input = False
    while (valid_input is False):
        print()
        choice = input("Select an attack: ")
        if (parse_int(choice) is True):
            return int(choice)
        else:
            print("The input was invalid. Please try again.")


def get_computer_selection(health):
    sleep_time = random.randrange(2, 5)
    print("....thinking....")
    time.sleep(sleep_time)

    if (health <= 35):
        # Have the computer heal ~50% of its turns when <= 35
        result = random.randint(1, 6)
        if (result % 2 == 0):
            return 3
        else:
            return random.randint(1, 2)
    elif (health == 100):
        return random.randint(1, 2)
    else:
        return random.randint(1, 3)


def play_round(computer, human):
    game_in_progress = True
    current_player = computer

    while game_in_progress:
        # swap the current player each round
        if (current_player == computer):
            current_player = human
        else:
            current_player = computer

        print()
        print(
            "You have {0} health remaining and the "
            "computer has {1} health remaining."
            .format(human.health, computer.health))
        print()

        if (current_player == human):
            print("Mis sa siis saad:")
            print("1) Löö vana hea terasmõõgaga - .")
            print("2) Ninjutsu: tulepalli tehnika - Kui saate, siis davai vaatame ")
                  
            print("3) Chidori - äike ,Vaevalt et jõuad.")
            move = get_selection()
        else:
            move = get_computer_selection(computer.health)

        if (move == 1):
            damage = random.randrange(18, 25)
            if (current_player == human):
                computer.calculate_damage(damage, human.name.capitalize())
            else:
                human.calculate_damage(damage, computer.name.capitalize())
        elif (move == 2):
            damage = random.randrange(10, 35)
            if (current_player == human):
                computer.calculate_damage(damage, human.name.capitalize())
            else:
                human.calculate_damage(damage, computer.name.capitalize())
        elif (move == 3):
            heal = random.randrange(18, 25)
            current_player.calculate_heal(heal)
        else:
            print ("The input was not valid. Please select a choice again.")

        if (human.health == 0):
            print("Sorry, you lose!")
            computer.wins += 1
            game_in_progress = False

        if (computer.health == 0):
            print("Congratulations, you beat the computer!")
            human.wins += 1
            game_in_progress = False


def start_game():
    print("Tere tulemast võidlus mängi!")
    print("Täna saame teada, kes on tugevam (Windows XP) või (Inimene)")

    computer = Player("Computer")

    name = input("Sisestage oma nimi: ")
    inimene = Player(name)

    keep_playing = True

    while (keep_playing is True):
        print("Teie Score:")
        print("Sina - {0}".format(inimene.wins))
        print("Windows XP - {0}".format(computer.wins))

        computer.health = 100
        inimene.health = 100
        play_round(computer, inimene)
        print()
        response = input("Tahad veel kakelda?(Y/N)")
        if (response.lower() == "n"):
            break

start_game()