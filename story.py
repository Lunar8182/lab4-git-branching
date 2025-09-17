def intro():
    print("You wake up in a dark forest. You can go left or right or center.")
    choice = input("Which direction do you choose? (left/right/center): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "center":
        center_path
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find an evil witch.")
    print("You defeat the evil witch and save the day!")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

def center_path():
    print("You walk down the center path and encounter a horrible sight.")

if __name__ == "__main__":
    intro()
