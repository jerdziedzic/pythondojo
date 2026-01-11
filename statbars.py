"""
Basic health bar display
"""


import os # To clear terminal


# Set combat values for player and enemy
player_name = "Hero Joe"
player_hp = 15
player_hp_max = 20

enemy_name = "Punchley"
enemy_hp = 15
enemy_hp_max = 30


# Function to clear the screen
def clear_screen():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for Linux/macOS (posix)
        _ = os.system('clear')

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
            print("X", end="")

    print(f"] ({stat_current}/{stat_max})")


clear_screen()
show_statbar(player_name, player_hp, player_hp_max)
show_statbar(enemy_name, enemy_hp, enemy_hp_max)