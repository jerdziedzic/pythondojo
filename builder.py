"""
Basic character builder system
"""


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


#TODO: Limit input
player_name = input("Your Name: ")

#TODO: Better stat system
player_hp_max = int(input("Max HP: "))
player_hp = player_hp_max

player_damage_min = int(input("Damage Min: "))

player_damage_max = int(input("Damage Max: "))

player_hit = int(input("Hit Rate: "))

#TODO: Limit quote length
player_start_quote = input("Start Quote: ")

player_win_quote = input("Win Quote: ")

player=Character(
    player_name,
    player_hp_max,
    player_hp_max,
    player_damage_min,
    player_damage_max,
    player_hit,
    player_start_quote,
    player_win_quote
)