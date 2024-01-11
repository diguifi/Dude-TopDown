# Adventures of Dude in the Top-Down world
<p align="center">
  <img src="https://user-images.githubusercontent.com/31022286/56502606-4d62f800-64e9-11e9-93e9-2f6230433a9f.gif"/>
</p>

# [Download](https://github.com/diguifi/Dude-TopDown/releases)

A game developed in Python, using PyGame, which purpose is to test out a genetic algorithm and compare it to a finite state machine.

This project was conceived as a final paper on my computing science graduation at Instituto Federal de Educaçao, Ciencia e Tecnologia do Sul de Minas Gerais, Muzambinho (Brazil).

My goal now, with this, is to distribute openly for anyone who's into game development (specially with Python) and Artificial Intelligence for games.

Since this was my first PyGame project, my code is a little messy (the game itself is not and object, for exemple) and any contribution is not only welcome, as it is encouraged.

Thanks for your support.

# Setting up

Python version 3.7 or above
To be able to execute the Game, must have the 'PyGame' Library, and then, execute the 'Game.py' file.

- Installing PyGame:
    - Windows:
        - open the cmd (windows+r -> cmd)
        - execute the command 'python -m pip install pygame'
    - Linux:
        - use your package manager to install 'pip' (Ex - 'sudo apt-get install python3-pip')
        - run 'pip install pygame'

# Explanation

The game itself doesnt make clear of what is happening on the Genetic Algorithm mode, so I'll try to sum it up here (i'm also planning a video explaining how it works, and for the 1.0 release I also aim for an in-game option that explains the game, like a "How it works" option on the menu).

## Genetic Algorithms

If you never heard about Genetic Algorithms, don't worry, it sounds complex but its actually very simple to understand (and implement).
A Genetic Algorithm is a Machine Learning approach that is based on biological evolution to reach optimal results. It simulates a couple of core steps that happen in a real world evolution to accomplish a certain goal. These are the basic steps needed for a genetic algorithm to work:
- Selection
- Crossover
- Mutation

### Selection
Lets supose a population of creatures. These creatures have the goal to survive, the ones who survive can pass their genome to the next generation and so on. In order to "survive" there are several tasks that need to be performed, and the ones that perform them better, have better chances to be successfull.  
The **Selection** method does exactly this. It evaluates how well an individual creature performed on its goal.

On this game, the main goal for the enemies is to "live longer" (not be killed soon), cause damage to the player and steal items from the player. The **selection** method will then be responsible for selecting the enemies that will cross their chromosomes (on the **crossover** method) to create new enemies and will also live for the next round. The ones not selected are "killed" and do not pass their genes.  
The selection method used in this game is called "**Roulette wheel selection**".

### Crossover
This is basically the part where two successfull creatures "copulate" to have "children" that carry their parents mixed caracteristics on their chromosomes.  
Genetic Algorithms have several approaches for this method and the selected one was "**Single-point crossover**"

### Mutation
In biological evolution, mutations happen all the time and are responsible to create bad results or good results. Its thanks to mutation that we are no longer a single celled organism.  
A Genetic Algorithm can sometimes reach what is called a "Local Optimal Result". This is basically finding a nice result but not the best. In order to avoid being stuck on this Local Optimal Result we must have a mutation rate. The mutation rate's job is to change a certain part of the chromosome randomly and this may cause a new caracteristic to happen, that can be very positive (or negative) to reach the goal to be selected.

## How it is represented ingame

To understand where are the chromosomes and how they work, who was selected, how have their "children" become, its simple. Lets start on the chromosomes.

### Chromosome
A chromosome is represented as a list, like so:

![](https://i.imgur.com/A7L2lUN.png)

Each index of the list represents a certain caracteristic that the enemy has:  
![](https://i.imgur.com/pVFvbjH.png)

- **A:** Enemy's movement type. There are 10 different ways an enemy can move and this index indicates wich one is applied to this enemy
- **B:** Enemy's speed. Ranges from 70 to 130 units
- **C:** Enemy's relation to the item HP. Ranges from 0 to 2. If 0 the enemy doesnt care for the item, if 1 the enemy always reaches for the item as soon it enters the enemy's field of view and if 2, the enemy avoids the item, reverting its trajectory.
- **D:** Enemy's relation to the item Shield. Ranges from 0 to 2. If 0 the enemy doesnt care for the item, if 1 the enemy always reaches for the item as soon it enters the enemy's field of view and if 2, the enemy avoids the item, reverting its trajectory.
- **E:** Enemy's relation to the item Points. Ranges from 0 to 2. If 0 the enemy doesnt care for the item, if 1 the enemy always reaches for the item as soon it enters the enemy's field of view and if 2, the enemy avoids the item, reverting its trajectory.
- **F:** Enemy's relation to the Player. Ranges from 0 to 1. If 0 the enemy doesnt care for the player and if 1 the enemy always reaches for the player as soon it enters the enemy's field of view.
- **G:** Size of the Field of View. Ranges from 0.5 to 2
- **H:** Enemy's life. Ranges from 0.5 to 2

The enemies with best _fitness scores_ (a score that evaluates how well the enemy did) have better chances to pass its genome to the next round.

### Who was selected
On the first round, all chromosomes are random. To know who was selected on the next round and so on, just look at the two last enemies on the list at the bottom of the screen and their children are the first two. The one on the middle is always random.
To visualize better, an animation happens each next level to show who was selected, how are their children and the new enemies' you will face next round.

![](https://i.imgur.com/5HkxQRJ.png)

## Thats it!
Thanks for showing interest on this work and feel free to contribute as you like. If any questions, you can find my contact info [here](https://diguifi.github.io)

# TODOs

- ~Animation of genetic pool methods when passing a level~ (must be improved)
- Code refactoring to make the game loop and variables part of an object
- New maps for levels
- Better in-game UI
- ~Optimize music and sounds for better sync~
- General optimization
