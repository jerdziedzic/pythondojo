"""
Basic combat system
"""

# TODO: Add some color

# Import the libraries
import os # To clear terminal
import random # For random number generation
import time # For sleep pauses


# Class to store stats for player and enemies
class Character:

    def __init__(self, name, hp, hp_max, damage_min, damage_max, hit, start_quote, win_quote):
        self.name = name
        self.hp = hp
        self.hp_max = hp_max
        self.damage_min = damage_min
        self.damage_max = damage_max
        self.hit = hit
        self.start_quote = start_quote
        self.win_quote = win_quote


# Function to clear the screen
def clear_screen():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for Linux/macOS (posix)
        _ = os.system('clear')

# Function to display stat bars for HP, SP, etc.
def show_statbar(stat_title, stat_current, stat_max):
    # Handle input outside of 0 - 100%, as well as sliver of health cases
    statbar_slice_count = ((stat_current / stat_max) * 10)
    if statbar_slice_count > 10:
        statbar_slice_count = 10
    elif statbar_slice_count < 0:
        statbar_slice_count = 0
    elif statbar_slice_count < 1 and statbar_slice_count > 0:
        statbar_slice_count = 1
    statbar_slice_count = int(statbar_slice_count // 1) # Floor and cast as an integer

    # Display the bar
    print(f"{stat_title} [", end="")

    for i in range (1, (10+1)):
        if i <= statbar_slice_count:
            print("O", end="")
        else:
            print("x", end="")

    print(f"] ({stat_current}/{stat_max})")

# Set combat values for player and enemy
player=Character("Hero Joe", 10, 10, 1, 3, 80, "You killed my father. Prepare to die.", "You can't stand up to my Mersenne Twister!")

enemy=Character("Punchley", 10, 10, 1, 3, 80, "Get ready to taste pavement, brat.", "Kid, your dad was much stronger than you are.")

# Clear screen, display start quotes and text
clear_screen()

print(f"{player.name} vs {enemy.name}")

print(f"\n{player.name}: {player.start_quote}")
print(f"{enemy.name}: {enemy.start_quote}")
time.sleep(3) # Pause for X seconds

# Determine who goes first and display the result
# TODO: better initiative system
turn_order = random.randint(1,2)
if turn_order == 1:
    print(f"\n{player.name} gets the first strike!")
elif turn_order == 2:
    print(f"\n{enemy.name} gets the first strike!")
time.sleep(3) # Pause for X seconds

while True: # Infinite loop until one side loses
    
    # Player takes a swing, if hit, inflict damage and subtract from enemy HP.    
    if turn_order == 1:
        clear_screen()
        show_statbar(player.name, player.hp, player.hp_max)
        show_statbar(enemy.name, enemy.hp, enemy.hp_max)
        input("\nPress Enter to attack...") # TODO: better player input
        print(f"\n{player.name} takes a swing!")
        to_hit = random.randint(1, 100)
        print(f"To hit roll: {to_hit}")
        if to_hit <= player.hit:
            damage = random.randint(player.damage_min, player.damage_max)
            print(f"{player.name} hits {enemy.name} for {damage} damage!")
            enemy.hp -= damage
            time.sleep(3)
        else:
            print(f"{player.name} misses {enemy.name}!")
            time.sleep(3)
        # If enemy HP is equal to or less than 0, go to player victory, otherwise, go to enemy turn.
        if enemy.hp <= 0:
            clear_screen()
            show_statbar(player.name, player.hp, player.hp_max)
            show_statbar(enemy.name, enemy.hp, enemy.hp_max)
            print(f"\n{player.name} wins!")
            print(f"{player.name}: {player.win_quote}") 
            time.sleep(3)
            break
        turn_order = 2
    
    # Enemy takes a swing, if hit, inflict damage and subtract from player HP.
    if turn_order == 2:
        clear_screen()
        show_statbar(player.name, player.hp, player.hp_max)
        show_statbar(enemy.name, enemy.hp, enemy.hp_max)
        print(f"\n{enemy.name} takes a swing!")
        to_hit = random.randint(1, 100)
        print(f"To hit roll: {to_hit}")
        if to_hit <= enemy.hit:
            damage = random.randint(enemy.damage_min, enemy.damage_max)
            print(f"{enemy.name} hits {player.name} for {damage} damage!")
            player.hp -= damage
            time.sleep(3)
        else:
            print(f"{enemy.name} misses {player.name}!")
            time.sleep(3)
        # If player HP is equal to or less than 0, go to game over, otherwise, go to player turn.
        if player.hp <= 0:
            clear_screen()
            show_statbar(player.name, player.hp, player.hp_max)
            show_statbar(enemy.name, enemy.hp, enemy.hp_max)
            print(f"\n{player.name} loses!")
            print(f"{enemy.name}: {enemy.win_quote}") 
            time.sleep(3)
            break
        turn_order = 1

clear_screen()
print("Combat over! Final results:")
print(f"{player.name} HP: {player.hp}")
print(f"{enemy.name} HP: {enemy.hp}")