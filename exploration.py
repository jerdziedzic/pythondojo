"""
Basic exploration system
"""

import os # To clear terminal
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

# Set boundaries for the game map
loc_x_pos_max = 1
loc_x_neg_max = -1
loc_y_pos_max = 1
loc_y_neg_max = -1
loc_z_pos_max = 1
loc_z_neg_max = -1

# Set starting coordinates
loc_x = 0
loc_y = 0
loc_z = 0

# Main exploration loop
while True:
    
    # TODO: make a class for areas with coordinates, text, and exits
    # -1,1 = NW
    if loc_x == -1 and loc_y == 1:
        clear_screen()
        print(f"X={loc_x}, Y={loc_y}")
        print("You are in the Northwesterly Woods. There's not much here yet.")

    # 0,1 = N
    if loc_x == 0 and loc_y == 1:
        clear_screen()
        print(f"X={loc_x}, Y={loc_y}")
        print("You are on Northerly Island. There's not much here yet.")

    # 1,1 = NE
    if loc_x == 1 and loc_y == 1:
        clear_screen()
        print(f"X={loc_x}, Y={loc_y}")
        print("You are in the Northeastern Desert. There's not much here yet.")

    # -1,0 = W
    if loc_x == -1 and loc_y == 0:
        clear_screen()
        print(f"X={loc_x}, Y={loc_y}")
        print("You are on the West Sieeede. There's not much here yet.")

    # 0,0 = Start
    if loc_x == 0 and loc_y == 0:
        clear_screen()
        print(f"X={loc_x}, Y={loc_y}")
        print("You are in the starting location. There's not much here yet.")

    # 1,0 = E
    if loc_x == 1 and loc_y == 0:
        clear_screen()
        print(f"X={loc_x}, Y={loc_y}")
        print("You are in Eastham. There's not much here yet.")

    # -1,-1 = SW
    if loc_x == -1 and loc_y == -1:
        clear_screen()
        print(f"X={loc_x}, Y={loc_y}")
        print("You are on the Southwest Highway. There's not much here yet.")

    # 0,-1 = S
    if loc_x == 0 and loc_y == -1:
        clear_screen()
        print(f"X={loc_x}, Y={loc_y}")
        print("You are in Southtown. There's not much here yet.")

    # 1,-1 = SE
    if loc_x == 1 and loc_y == -1:
        clear_screen()
        print(f"X={loc_x}, Y={loc_y}")
        print("You are in the Southeast Swamp. There's not much here yet.")

    # Show travel menu and get player input
    # TODO: use pynput or keyboard llibrary for keypress input (maybe pygame instead?)
    print("\nWhere do you want to go?\n")
    print("N. Go North")
    print("W. Go West")
    print("E. Go East")
    print("S. Go South")
    print("Q. Quit")
    exp_inp = input("\nYour Move:")
    # Move north
    if exp_inp == "N" or exp_inp == "n":
        if loc_y == loc_y_pos_max:
            print("You might want to stay on the map...")
            time.sleep(1)
        else:
            print("Going north...")
            time.sleep(1)
            loc_y += 1
    # Move west
    elif exp_inp == "W" or exp_inp == "w":
        if loc_x == loc_x_neg_max:
            print("You might want to stay on the map...")
            time.sleep(1)
        else:
            print("Going west...")
            time.sleep(1)
            loc_x -= 1
    # Move east
    elif exp_inp == "E" or exp_inp == "e":
        if loc_x == 1:
            print("You might want to stay on the map...")
            time.sleep(1)
        else:
            print("Going east...")
            time.sleep(1)
            loc_x += 1
    # Move south
    elif exp_inp == "S" or exp_inp == "s":
        if loc_y == -1:
            print("You might want to stay on the map...")
            time.sleep(1)
        else:
            print("Going south...")
            time.sleep(1)
            loc_y -= 1
    # Quit the game
    elif exp_inp == "Q" or exp_inp == "q":
        print("See you later!")
        break
    # Invalid input handler
    else:
        print("Invalid command!")
        time.sleep(1)