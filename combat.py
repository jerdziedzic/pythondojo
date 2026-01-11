"""
Basic combat system
"""

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

# Set combat values for player and enemy
player_name = "Hero Joe"
player_hp = 10
player_damage_min = 1
player_damage_max = 3
player_hit = 80
player_start_quote = "You killed my father. Prepare to die."
player_win_quote = "You can't stand up to my Mersenne Twister!"

enemy_name = "Punchley"
enemy_hp = 10
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
time.sleep(3) # Pause for X seconds

if turn_order == 1:
    print(f"\n{player_name} gets the first strike!")
elif turn_order == 2:
    print(f"\n{enemy_name} gets the first strike!")

while True: # Infinite loop until one side loses
    
    # Player takes a swing, if hit, inflict damage and subtract from enemy HP.    
    if turn_order == 1:
        input("\nPress Enter to attack...")
        print(f"\n{player_name} takes a swing!")
        to_hit = random.randint(1, 100)
        print(f"To hit roll: {to_hit}")
        if to_hit <= player_hit:
            damage = random.randint(player_damage_min, player_damage_max)
            print(f"{player_name} hits {enemy_name} for {damage} damage!")
            enemy_hp -= damage
            # TODO: simple health bars
            print(f"{player_name} HP: {player_hp}")
            print(f"{enemy_name} HP: {enemy_hp}")
            time.sleep(3)
        else:
            print(f"{player_name} misses {enemy_name}!")
            time.sleep(3)
        # If enemy HP is equal to or less than 0, go to player victory, otherwise, go to enemy turn.
        if enemy_hp <= 0:
            print(f"\n{player_name} wins!")
            print(f"{player_name}: {player_win_quote}") 
            time.sleep(3)
            break
        turn_order = 2
    
    # Enemy takes a swing, if hit, inflict damage and subtract from player HP.
    if turn_order == 2:
        print(f"\n{enemy_name} takes a swing!")
        to_hit = random.randint(1, 100)
        print(f"To hit roll: {to_hit}")
        if to_hit <= enemy_hit:
            damage = random.randint(enemy_damage_min, enemy_damage_max)
            print(f"{enemy_name} hits {player_name} for {damage} damage!")
            player_hp -= damage
            # TODO: simple health bars
            print(f"{player_name} HP: {player_hp}")
            print(f"{enemy_name} HP: {enemy_hp}")
            time.sleep(3)
        else:
            print(f"{enemy_name} misses {player_name}!")
            time.sleep(3)
        # If player HP is equal to or less than 0, go to game over, otherwise, go to player turn.
        if player_hp <= 0:
            print(f"\n{player_name} loses!")
            print(f"{enemy_name}: {enemy_win_quote}") 
            time.sleep(3)
            break
        turn_order = 1

print("\nCombat over! Final results:")
print(f"{player_name} HP: {player_hp}")
print(f"{enemy_name} HP: {enemy_hp}")