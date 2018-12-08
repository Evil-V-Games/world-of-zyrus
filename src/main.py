import sys
import os
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.max_health = 100
        self.health = self.max_health
        self.strength = 10
        self.gold = 0
        self.specials = 10
        self.player_class = ""

class Goblin:
    def __init__(self, name):
        self.name = name
        self.max_health = 50
        self.health = self.max_health
        self.strength = 5
        self.goldgain = 10

class Zombie:
    def __init__(self, name):
        self.name = name
        self.max_health = 70
        self.health = self.max_health
        self.strength = 7
        self.goldgain = 15

class ArenaFighter:
    def __init__(self):
        self.name = "John Cena"
        self.max_health = player.max_health
        self.health = self.max_health
        self.strength = player.strength + 5
        self.goldgain = (player.gold + 10) * 4

def clear():
    if sys.platform == "linux":
        os.system("clear")
    else:
        os.system("cls")

def main():
    clear()
    print("Welcome to World of Zyrus")
    print("1.) Start")
    print("2.) Exit")
    option = input("-> ")
    if option == "1":
        clear()
        start()
    elif option == "2":
        sys.exit()
    else:
        clear()
        print("Invalid option")

def start():
    print("You are a young man living on the countryside with your parents. You are working the farm when you notice an old man walking around. It seems like he wants to buy some corn from you. You eagerly walk up to the currently abandoned produce stand and wait. The man introduces himself as Erebus, a powerful wizard, who, in his old age, is looking for young people to go on an adventure for him.")
    print("Erebus: What is your name?")
    option = input("-> ")
    global player
    player = Player(option)
    clear()
    print("Erebus: Well then, hello " + player.name + "! But the question still remains: will you join me on my adventure? (Y / N)")
    option = input("-> ")
    if option == "Y" or option == "y":
        clear()
        print("Erebus: Thank you for accepting my request!")
        input("Press enter or return to continue.")
        clear()
        print("You and the wizard walk to a small town not far out from your farm that you visit regularly.")
        print("Erebus: So then, young lad, what class would you like to be?")
        print("1: Fighter | 2: Wizard | 3: Ranger")
        option = input("-> ")
        if option == "1":
            player.player_class = "fighter"
            player.strength = 20
        elif option == "2":
            player.player_class = "wizard"
        elif option == "3":
            player.player_class = "ranger"
            player.strength = 15
        else:
            print("Invalid option")
            sys.exit()
        clear()
        print("You have chosen " + player.player_class + ".")
        input("Press enter or return to continue.")
        clear()
        print("Name: " + player.name)
        print("Class: " + player.player_class)
        print("Attack: " + str(player.strength))
        print("Health: " + str(player.health) + "/" + str(player.max_health))
        print("Gold: " + str(player.gold))
        if player.player_class == "fighter":
            print("Potions: " + str(player.specials) + "\n")
        elif player.player_class == "wizard":
            print("Spells: " + str(player.specials) + "\n")
        elif player.player_class == "ranger":
            print("Arrows: " + str(player.specials) + "\n")
        input("Press enter or return to continue")
        
        clear()
        print("You and the wizard head out of town. About half an hour along the dirt road, you are blocked by a goblin and a zombie.")
        print("Erebus: Attack those vile creatures!")
        goblin = Goblin("Goblin")
        zombie = Zombie("Zombie")
        encounter(goblin)
        encounter(zombie)
        input("Press enter or return to continue.")
        clear()
        print("Erebus: Good thing your parents taught you self defense!")
        print("You and the wizard keep going, reaching his house by nightfall. He lives in a small and cozy log cabin in the woods.")
        input("Press enter or return to continue.")
        clear()
        print("Erebus: So, you must be wondering what you came here for. Here's the story. One day, in the city of Grindlewood (now only known in legend), everything was seemingly going well. The children were playing in the park, the birds were singing, and even the workers were happy. However, on this day, an evil sorcerer came apon the city and took its people hostage. The vaults of the rich were emptied simply as a tribute to prevent any more inoccent lives from being lost. Many willfully left the city that day, and many more against their will. And thus ends the grim story of Grindlewood. I would like you to journey to the ruins of the city, free the enslaved people, and kill the evil sorcerer.\nYou eagerly except.")
        input("Press enter or return to continue.")
        clear()
        print("The wizard gives you provisions for the journey to come as well as healing you. As you set off on your journey, you imagine defeating the sorcerer and coming home rich. You keep on walking down the dirt road, thinking about the future.")
        player.health = player.max_health
        player.specials += 20
        input("Press enter or return to continue.")
        clear()
        print("You sleep the night on the dirt trail and walk to the nearby village of Dragontail in the morning. You can do many things in this village.")
        while True:
            print("1.) Shop")
            print("2.) Fight")
            print("3.) Leave")
            print("4.) Gamble")
            option = input("-> ")
            if option == "1":
                shop("Dragontale")
            elif option == "2":
                fight("Dragontale")
                input()
            elif option == "3":
                break
            elif option == "4":
                gamble("Dragontale")
            else:
                print("Invalid option.")
                sys.exit()
            clear()

        print("You leave the village.")

    elif option == "N" or option == "n":
        print("The wizard walks away silently, badly hiding his disappointement.")
        print("Game over.")
    else:
        print("Invalid option")

def shop(town):
    clear()
    print("Clerk: Welcome to the " + town + " store.")
    while 1 > 0:
        print("You have " + str(player.gold) + " gold.")
        print("1.) Buy a special item (potion, spell or arrow) [10 gold]")
        print("2.) Be healed [20 gold]")
        print("3.) Raise your max health [15 gold]")
        print("4.) Exit")
        option = input("-> ")
        if option == "1":
            if player.gold >= 10:
                player.specials += 1
                player.gold -= 10
                print("You have bought a special item")
            else:
                print("You do not have enough money.")
        elif option == "2":
            if player.gold >= 20:
                player.health = player.max_health
                player.gold -= 20
                print("You have been healed.")
            else:
                print("You do not have enough money.")
        elif option == "3":
            if player.gold >= 15:
                player.max_health += 10
                player.gold -= 15
                print("Your max health has been raised to " + str(player.max_health) + ".")
            else:
                print("You do not have enough money.")
        elif option == "4":
            print("Goodbye.")
            input("Press enter or return to continue.")
            clear()
            return
        input("Press enter or return to continue.")
        clear()

def fight(town):
    print("Welcome to the " + town + " arena.")
    print("Announcer: In one corner: " + player.name + ", in the other corner, our long-reigning champion: John Cena!!!!")
    encounter(ArenaFighter())

def gamble(town):
    print("Welcome to the " + town + " casino.")
    if player.gold <= 0:
        print("You do not have enough money to gamble.")
    print("You bet half of your money on a coin flip. Someone else bets as much as you do.")
    result = random.randint(0, 1)
    if result == 0:
        print("You lose.")
        player.gold -= player.gold / 2
    else:
        print("You win.")
        player.gold += player.gold
    print("Play again? (Y / N)")
    option = input("-> ")
    if option == "y" or option == "Y":
        clear()
        gamble(town)
    elif option == "n" or option == "N":
        print("Goodbye.")
        input("Press enter or return to continue.")
        clear()

def encounter(monster):
    input("Press enter or return to continue.")
    clear()
    print(player.name + " VS " + monster.name)
    print(monster.name + "'s Health: " + str(monster.health))
    print(monster.name + "'s Strength: " + str(monster.strength))
    print(monster.name + "'s Reward: " + str(monster.goldgain) + "\n")
    print("Your Health: " + str(player.health) + "/" + str(player.max_health))
    print("Your Strength: " + str(player.strength))
    print("Your Gold: " + str(player.gold))
    if player.player_class == "fighter":
        print("Your Potions: " + str(player.specials) + "\n")
    elif player.player_class == "wizard":
        print("Your Spells: " + str(player.specials) + "\n")
    elif player.player_class == "ranger":
        print("Your Arrows: " + str(player.specials) + "\n")
    input("Press enter or return to continue.")
    while (monster.health > 0 and player.health > 0):
        clear()
        print("Your turn")
        if player.health <= 0:
            print("You have died.")
            print("Game over.")
            sys.exit()
        print("Your Health: " + str(player.health) + "/" + str(player.max_health))
        if player.player_class == "fighter":
            print("Your Potions: " + str(player.specials))
        elif player.player_class == "wizard":
            print("Your Spells: " + str(player.specials))
        elif player.player_class == "ranger":
            print("Your Arrows: " + str(player.specials))
        print("1.) Attack for " + str(player.strength) + " damage")
        if player.player_class == "fighter":
            print("2.) Drink a potion (" + str(player.specials) + " left)")
        elif player.player_class == "wizard":
            print("2.) Use a spell (" + str(player.specials) + " left)")
        elif player.player_class == "ranger":
            print("2.) Shoot an arrow (" + str(player.specials) + " left)")
        print("3.) Run away")
        option = input("-> ")
        if option == "1":
            print("You hit the enemy, dealing " + str(player.strength) + " damage.")
            monster.health -= player.strength
            print(monster.name + " has " + str(monster.health) + "/" + str(monster.max_health) + " health.")
            if monster.health <= 0:
                print("You won the fight. You gained " + str(monster.goldgain) + " gold and " + str(monster.max_health / 5) + " strength.")
                player.gold += monster.goldgain
                player.strength += monster.max_health / 5
                return
        elif option == "2":
            if player.specials > 0:
                if player.player_class == "fighter":
                    print("You drink a potion, healing you for " + str(player.max_health / 2) + " health.")
                    player.health += player.max_health / 2
                elif player.player_class == "wizard":
                    print("You cast a spell, dealing " + str(monster.health / 2) + " damage.")
                    monster.health -= monster.health / 2
                    print(monster.name + " has " + str(monster.health) + "/" + str(monster.max_health) + " health.")
                    if monster.health <= 0:
                        print("You won the fight. You gained " + str(monster.goldgain) + " gold and " + str(monster.max_health / 5) + " strength.")
                        player.gold += monster.goldgain
                        player.strength += monster.max_health / 5
                        return
                elif player.player_class == "ranger":
                    print("You shoot the monster with an arrow from your bow, dealing " + str(player.strength * 1.5) + " damage.")
                    monster.health -= player.strength * 1.5
                    print(monster.name + " has " + str(monster.health) + "/" + str(monster.max_health) + " health.")
                    if monster.health <= 0:
                        print("You won the fight. You gained " + str(monster.goldgain) + " gold and " + str(monster.max_health / 5) + " strength.")
                        player.gold += monster.goldgain
                        player.strength += monster.max_health / 5
                        return
                player.specials -= 1
                print("You have " + str(player.specials) + " special items left.")
            else:
                print("You have no more special left. You have wasted this turn.")
        elif option == "3":
            print("You ran away")
            return
        print(monster.name + "'s turn.")
        print("The monster attacks you and deals " + str(monster.strength) + " damage.")
        player.health -= monster.strength
        if player.health <= 0:
            print("You have died.")
            print("Game over.")
            sys.exit()
        input("Press enter or return to continue.")
        
if __name__ == "__main__":
    main()
    input()
