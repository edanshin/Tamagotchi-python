You've been given a Tamagotchi class in the file tamagotchi.py. Your job is to use this class to build a multi-tamagotchi game.

Here's how to use the Tamagotchi class.

from tamagotchi import Tamagotchi

niblet = Tamagotchi('Niblet')
print(niblet)
niblet.feed()
niblet.increment_time()
print(niblet)


In this example, we're creating a new Tamagotchi (giving it the name 'Niblet'), feeding it and using the increment_time method to simulate time passing.

Your game should let the user enter commands one at a time and stop when an empty string is entered. The commands to implement are:

    create <name>
    feed <name>
    play <name>
    wait

Since this is a multi-tamagotchi game, each command (except wait) needs the name of the Tamagotchi on which to act. Tamagotchi names will not contain spaces.

The create command creates a new Tamagotchi with the given name, the feed and play commands should call the feed and play methods on the correct Tamagotchi. The wait command does nothing, but time passes as normal (see below).

If the entered command is not one of these four values, it should print Invalid command.. For the commands which specify a Tamagotchi by name, if the Tamagotchi has not been created it should say No Tamagotchi with that name.. You cannot create a new Tamagotchi with the same name as an existing Tamagotchi unless it is dead. If the Tamagotchi already exists and is not dead, print You already have a Tamagotchi called that..

In this game, each command also causes time to pass. After each command (if it is a valid command) print out the current state of each Tamagotchi in name sorted order, and then call the increment_time method to pass time for all Tamagotchi.

If the command is unknown, an unknown named Tamagotchi is provided to a known command, or a not-yet-dead Tamagotchi is provided to the create command, your program should ask the user for the next command without printing out the state of each Tamagotchi or incrementing time.

Here's an example with one Tamagotchi:

Command: create fluffy

 _____
/ ^_^ \
\_____/
Name:    fluffy
Hunger:  ooooo
Boredom: 
Age:     0

Command: wait

 _____
/ ^_^ \
\_____/
Name:    fluffy
Hunger:  oooooo
Boredom: o
Age:     1

Command: feed fluffy

 _____
/ ^_^ \
\_____/
Name:    fluffy
Hunger:  oooo
Boredom: oo
Age:     2

Command: play fluffy
   _______
  /       \
 /  ^ _ ^  \
 \_________/
    U   U
Name:    fluffy
Hunger:  ooooo
Boredom: 
Age:     3

Command:

​

And here's a longer example with multiple simultaneous Tamagotchi:

Command: feed fluffy
No Tamagotchi with that name.
Command: sdfjsldkf
Invalid command.
Command: create fluffy

 _____
/ ^_^ \
\_____/
Name:    fluffy
Hunger:  ooooo
Boredom: 
Age:     0

Command: create buffy

 _____
/ ^_^ \
\_____/
Name:    buffy
Hunger:  ooooo
Boredom: 
Age:     0


 _____
/ ^_^ \
\_____/
Name:    fluffy
Hunger:  oooooo
Boredom: o
Age:     1

Command: create zoom

 _____
/ ^_^ \
\_____/
Name:    buffy
Hunger:  oooooo
Boredom: o
Age:     1


 _____
/ ^_^ \
\_____/
Name:    fluffy
Hunger:  ooooooo
Boredom: oo
Age:     2


 _____
/ ^_^ \
\_____/
Name:    zoom
Hunger:  ooooo
Boredom: 
Age:     0

Command: feed fluffy

 _____
/ ^_^ \
\_____/
Name:    buffy
Hunger:  ooooooo
Boredom: oo
Age:     2

   _______
  /       \
 /  ^ _ ^  \
 \_________/
    U   U
Name:    fluffy
Hunger:  ooooo
Boredom: ooo
Age:     3


 _____
/ ^_^ \
\_____/
Name:    zoom
Hunger:  oooooo
Boredom: o
Age:     1

Command: feed buffy
   _______
  /       \
 /  ^ _ ^  \
 \_________/
    U   U
Name:    buffy
Hunger:  ooooo
Boredom: ooo
Age:     3

   _______
  /       \
 /  ^ _ ^  \
 \_________/
    U   U
Name:    fluffy
Hunger:  oooooo
Boredom: oooo
Age:     4


 _____
/ ^_^ \
\_____/
Name:    zoom
Hunger:  ooooooo
Boredom: oo
Age:     2

Command: feed zoom
   _______
  /       \
 /  ^ _ ^  \
 \_________/
    U   U
Name:    buffy
Hunger:  oooooo
Boredom: oooo
Age:     4

   _______
  /       \
 /  ^ _ ^  \
 \_________/
    U   U
Name:    fluffy
Hunger:  ooooooo
Boredom: ooooo
Age:     5

   _______
  /       \
 /  ^ _ ^  \
 \_________/
    U   U
Name:    zoom
Hunger:  ooooo
Boredom: ooo
Age:     3

Command: play fluffy
   _______
  /       \
 /  ^ _ ^  \
 \_________/
    U   U
Name:    buffy
Hunger:  ooooooo
Boredom: ooooo
Age:     5

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    fluffy
Hunger:  oooooooo
Boredom: o
Age:     6

   _______
  /       \
 /  ^ _ ^  \
 \_________/
    U   U
Name:    zoom
Hunger:  oooooo
Boredom: oooo
Age:     4

Command: feed fluffy
   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    buffy
Hunger:  oooooooo
Boredom: oooooo
Age:     6

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    fluffy
Hunger:  oooooo
Boredom: oo
Age:     7

   _______
  /       \
 /  ^ _ ^  \
 \_________/
    U   U
Name:    zoom
Hunger:  ooooooo
Boredom: ooooo
Age:     5

Command: feed fluffy
   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    buffy
Hunger:  ooooooooo
Boredom: ooooooo
Age:     7

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    fluffy
Hunger:  oooo
Boredom: ooo
Age:     8

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    zoom
Hunger:  oooooooo
Boredom: oooooo
Age:     6

Command: feed zoom
   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    buffy
Hunger:  oooooooooo
Boredom: oooooooo
Age:     8

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    fluffy
Hunger:  ooooo
Boredom: oooo
Age:     9

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    zoom
Hunger:  oooooo
Boredom: ooooooo
Age:     7

Command: play zoom

Name:    buffy
DEAD

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    fluffy
Hunger:  oooooo
Boredom: ooooo
Age:     10

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    zoom
Hunger:  ooooooo
Boredom: ooo
Age:     8

Command: feed fluffy

Name:    buffy
DEAD

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    fluffy
Hunger:  oooo
Boredom: oooooo
Age:     11

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    zoom
Hunger:  oooooooo
Boredom: oooo
Age:     9

Command: feed zoom

Name:    buffy
DEAD

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    fluffy
Hunger:  ooooo
Boredom: ooooooo
Age:     12

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    zoom
Hunger:  oooooo
Boredom: ooooo
Age:     10

Command: feed fluffy

Name:    buffy
DEAD

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    fluffy
Hunger:  ooo
Boredom: oooooooo
Age:     13

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    zoom
Hunger:  ooooooo
Boredom: oooooo
Age:     11

Command: play zoom

Name:    buffy
DEAD

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    fluffy
Hunger:  oooo
Boredom: ooooooooo
Age:     14

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    zoom
Hunger:  oooooooo
Boredom: oo
Age:     12

Command: feed fluffy

Name:    buffy
DEAD

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    fluffy
Hunger:  oo
Boredom: oooooooooo
Age:     15

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    zoom
Hunger:  ooooooooo
Boredom: ooo
Age:     13

Command: play zoom

Name:    buffy
DEAD


Name:    fluffy
DEAD

   ___________
  /           \
 /  /\     /\  \
 \      _      /
  \___________/
    \_/   \_/
Name:    zoom
Hunger:  oooooooooo
Boredom: 
Age:     14

Command: wait

Name:    buffy
DEAD


Name:    fluffy
DEAD


Name:    zoom
DEAD

Command: 
