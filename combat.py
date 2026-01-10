"""
Basic combat system
"""

import random

# Set combat values for player and enemy
player_hp = 10
player_damage = 2
player_hit = 80

enemy_hp = 10
enemy_damage = 2
enemy_hit = 80

# Determine who goes first.
# TODO: better initiative system
turn_order = random.randint(1,2)
if turn_order == 1:
    print("Player gets the first strike!")
elif turn_order == 2:
    print("Enemy gets the first strike!")

while True: # Infinite loop until one side loses
    # Player takes a swing, if hit, inflict damage and subtract from enemy HP.    
    if turn_order == 1:
        print("Player takes a swing!")
        to_hit = random.randint(1, 100)
        print(f"To hit roll: {to_hit}")
        if to_hit <= player_hit:
            print(f"Player hits the enemy for {player_damage} damage!") # TODO: random player damage
            enemy_hp -= player_damage
        else:
            print("Player misses the enemy!")
        # If enemy HP is equal to or less than 0, go to player victory, otherwise, go to enemy turn.
        if enemy_hp <= 0:
            print("You win!")
            break
        turn_order = 2
    # Enemy takes a swing, if hit, inflict damage and subtract from player HP.
    if turn_order == 2:
        print("Enemy takes a swing!")
        to_hit = random.randint(1, 100)
        print(f"To hit roll: {to_hit}")
        if to_hit <= enemy_hit:
            print(f"Enemy hits the player for {enemy_damage} damage!") # TODO: random enemy damage
            player_hp -= enemy_damage
        else:
            print("Enemy misses the player!")
        # If player HP is equal to or less than 0, go to game over, otherwise, go to player turn.
        if player_hp <= 0:
            print("You lose!")
            break
        turn_order = 1

    # TODO: simple health bars
    print(f"Player HP: {player_hp}")
    print(f"Enemy HP: {enemy_hp}")

# TODO: win/loss quotes
print("Combat over! Final results:")
print(f"Player HP: {player_hp}")
print(f"Enemy HP: {enemy_hp}")