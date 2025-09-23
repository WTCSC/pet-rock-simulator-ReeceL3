import time

def pet_rock_game():
   
    name = input("What would you like to name your pet rock? ")

    stats = {
        "happiness": 5,
        "hunger": 5,
        "health": 5
    }

    print(f"\nWelcome! You are now taking care of {name}.")
    print("Keep them happy, healthy, and not too hungry!\n")

    # Main Game Loop
    while True:
        print(f"\n{name}'s stats: Happiness = {stats['happiness']}, Hunger = {stats['hunger']}, Health = {stats['health']}")
        print("What would you like to do?")
        print("1. Feed your rock")
        print("2. Play with your rock")
        print("3. Do nothing")

        choice = input("Enter 1, 2, or 3: ")

        # Action & Consequence
        if choice == "1":  # Feed
            stats["hunger"] -= 2
            stats["happiness"] -= 1
            print(f"You fed {name}. Hunger decreases, and happiness decreases slightly.")
        elif choice == "2":  # Play
            stats["happiness"] += 2
            stats["hunger"] += 1
            print(f"You played with {name}. Happiness increases, but hunger increases slightly.")
        elif choice == "3":  # Do nothing
            stats["happiness"] -= 1
            stats["hunger"] += 1
            print(f"You did nothing. Both hunger and unhappiness grow worse.")
        else:  # Invalid input
            print(f"{name} looks confused by your choice...")

       
        stats["hunger"] += 1
        stats["happiness"] -= 1

  
        stats["hunger"] = max(stats["hunger"], 0)
        stats["happiness"] = max(stats["happiness"], 0)

        # Game Over Conditions
        if stats["health"] <= 0:
            print(f"\nYour pet rock {name} died. 💀")
            break
        if stats["hunger"] >= 10:
            print(f"\nYour pet rock {name} got too hungry died of starvation")
            break
        if stats["happiness"] <= 0:
            print(f"\nYour pet rock {name} is bored of ur ah and found a new owner")
            break

        time.sleep(1) #makes code easier to comprehend

pet_rock_game()
