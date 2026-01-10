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

# Determine who goes first

# Player takes a swing, if hit, inflict damage and subtract from enemy HP.
# If enemy HP is equal to or less than 0, go to player victory, otherwise, go to enemy turn.

# Enemy takes a swing, if hit, inflict damage and subtract from player HP.
# If player HP is equal to or less than 0, go to game over, otherwise, go to player turn.

print("Hello again!")