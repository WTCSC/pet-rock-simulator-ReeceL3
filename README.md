# Pet Rock Game — Python (CLI)

A simple virtual pet rock game written in Python.
Take care of your rock by feeding it, playing with it, or… doing nothing.
Your goal is to keep it alive, happy, and not too hungry — otherwise, it might leave you… or worse.

# Features

* Interactive command-line virtual pet.

* Stats tracking: Happiness, Hunger, and Health.

* Multiple ways to interact with your pet rock: feed, play, or ignore.

* Branching outcomes and game-over conditions.

* Lightweight, single-file Python script (no external libraries).

# How to Run

1. Make sure you have Python 3 installed (3.7+ recommended).

2. Save the code to a file, e.g. pet_rock.py.

3. Run from a terminal:

![](image.png)

# Example Playthrough
 What would you like to name your pet rock? Rocky

Welcome! You are now taking care of Rocky.
Keep them happy, healthy, and not too hungry!

Rocky's stats: Happiness = 5, Hunger = 5, Health = 5
What would you like to do?
1. Feed your rock
2. Play with your rock
3. Do nothing
Enter 1, 2, or 3: 2

You played with Rocky. Happiness increases, but hunger increases slightly.

## Possible outcomes:

1. Rock dies of starvation if hunger ≥ 10.

2. Rock abandons you if happiness ≤ 0.

3. Rock dies if health reaches 0.

