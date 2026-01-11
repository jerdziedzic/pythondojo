"""
Basic combat system
"""

# TODO: Add some color

# Import the libraries
import os # To clear terminal
import random # For random number generation
import time # For sleep pauses


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
player_name = "Hero Joe"
player_hp = 10
player_hp_max = 10
player_damage_min = 1
player_damage_max = 3
player_hit = 80
player_start_quote = "You killed my father. Prepare to die."
player_win_quote = "You can't stand up to my Mersenne Twister!"

enemy_name = "Punchley"
enemy_hp = 10
enemy_hp_max = 10
enemy_damage_min = 1
enemy_damage_max = 3
enemy_hit = 80
enemy_start_quote = "Get ready to taste pavement, brat."
enemy_win_quote = "Kid, your dad was much stronger than you are."

# Clear screen, display start quotes and text
clear_screen()

print(f"{player_name} vs {enemy_name}")

print(f"\n{player_name}: {player_start_quote}")
print(f"{enemy_name}: {enemy_start_quote}")
time.sleep(3) # Pause for X seconds

# Determine who goes first and display the result
# TODO: better initiative system
turn_order = random.randint(1,2)
if turn_order == 1:
    print(f"\n{player_name} gets the first strike!")
elif turn_order == 2:
    print(f"\n{enemy_name} gets the first strike!")
time.sleep(3) # Pause for X seconds

while True: # Infinite loop until one side loses
    
    # Player takes a swing, if hit, inflict damage and subtract from enemy HP.    
    if turn_order == 1:
        clear_screen()
        show_statbar(player_name, player_hp, player_hp_max)
        show_statbar(enemy_name, enemy_hp, enemy_hp_max)
        input("\nPress Enter to attack...") # TODO: better player input
        print(f"\n{player_name} takes a swing!")
        to_hit = random.randint(1, 100)
        print(f"To hit roll: {to_hit}")
        if to_hit <= player_hit:
            damage = random.randint(player_damage_min, player_damage_max)
            print(f"{player_name} hits {enemy_name} for {damage} damage!")
            enemy_hp -= damage
            time.sleep(3)
        else:
            print(f"{player_name} misses {enemy_name}!")
            time.sleep(3)
        # If enemy HP is equal to or less than 0, go to player victory, otherwise, go to enemy turn.
        if enemy_hp <= 0:
            clear_screen()
            show_statbar(player_name, player_hp, player_hp_max)
            show_statbar(enemy_name, enemy_hp, enemy_hp_max)
            print(f"\n{player_name} wins!")
            print(f"{player_name}: {player_win_quote}") 
            time.sleep(3)
            break
        turn_order = 2
    
    # Enemy takes a swing, if hit, inflict damage and subtract from player HP.
    if turn_order == 2:
        clear_screen()
        show_statbar(player_name, player_hp, player_hp_max)
        show_statbar(enemy_name, enemy_hp, enemy_hp_max)
        print(f"\n{enemy_name} takes a swing!")
        to_hit = random.randint(1, 100)
        print(f"To hit roll: {to_hit}")
        if to_hit <= enemy_hit:
            damage = random.randint(enemy_damage_min, enemy_damage_max)
            print(f"{enemy_name} hits {player_name} for {damage} damage!")
            player_hp -= damage
            time.sleep(3)
        else:
            print(f"{enemy_name} misses {player_name}!")
            time.sleep(3)
        # If player HP is equal to or less than 0, go to game over, otherwise, go to player turn.
        if player_hp <= 0:
            clear_screen()
            show_statbar(player_name, player_hp, player_hp_max)
            show_statbar(enemy_name, enemy_hp, enemy_hp_max)
            print(f"\n{player_name} loses!")
            print(f"{enemy_name}: {enemy_win_quote}") 
            time.sleep(3)
            break
        turn_order = 1

clear_screen()
print("Combat over! Final results:")
print(f"{player_name} HP: {player_hp}")
print(f"{enemy_name} HP: {enemy_hp}")