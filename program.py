from tamagotchi import Tamagotchi

# define a home for all of our tamagotchis
tamagotchis = dict()

def run():
    while True:
        # let the user enter commands one at a time
        command = input('Command: ')

        # get commands for a specific tamagotchi
        # also, check number of arguments (Tamagotchi names will not contain spaces)
        args = command.split(' ')
        if len(args) == 2:
            cmd = args[0]
            name = args[1]

            # if an unknown named Tamagotchi is provided to a known command, ask for a new command
            if name == '' or name == 'unknown':
                continue

            # The create command creates a new Tamagotchi with the given name
            if cmd == 'create':
                # You cannot create a new Tamagotchi with the same name as an existing Tamagotchi unless it is dead
                if name in tamagotchis:
                    if tamagotchis[name].is_dead() == False:
                        print('You already have a Tamagotchi called that.')
                        continue
                tamagotchis[name] = Tamagotchi(name)
            elif cmd == 'feed':
                if name not in tamagotchis:
                    print('No Tamagotchi with that name.')
                    continue
                tamagotchis[name].feed()
            elif cmd == 'play':
                if name not in tamagotchis:
                    print('No Tamagotchi with that name.')
                    continue
                tamagotchis[name].play()

            # After each valid command, print out the current state of each Tamagotchi in name sorted order, and then increment age of all Tamagotchis
            output()
        # The wait command does nothing, but time passes as normal
        elif command == 'wait':
            output()

        # stop when an empty string is entered
        elif command == '':
            return
        else:
            print('Invalid command.')
        
# output the current state of each Tamagotchi in name sorted order, and then increment age of all Tamagotchis
def output():
    for name in sorted(tamagotchis.keys()):
        print(tamagotchis[name])
        tamagotchis[name].increment_time()

# run the program
run()
