"""
File Standard for Pokemon:
ID
pokemonID
strength
dexterity
intelligence
luck
charm
level
levelEvolve
evolveID
HP
"""

import random as r

masterData = []  # declaring the masterData array before using it

POKEMON = ((1, 'Bulbasaur', 'Ivysaur', 1, 16), (2, 'Ivysaur', 'Venusaur', 2, 36), (3, 'Venusaur', 'None', 3, 0),
           (4, 'Charmander', 'Charmeleon', 1, 16), (5, 'Charmeleon', 'Charizard', 2, 36),
           (6, 'Charizard', 'None', 3, 0),
           (7, 'Squirtle', 'Wartortle', 1, 16), (8, 'Wartortle', 'Blastoise', 2, 36), (9, 'Blastoise', 'None', 3, 0),
           (10, 'Caterpie', 'Metapod', 1, 7), (11, 'Metapod', 'Butterfree', 2, 10), (12, 'Butterfree', 'None', 3, 0),
           (13, 'Weedle', 'Kakuna', 1, 7), (14, 'Kakuna', 'Beedrill', 2, 10), (15, 'Beedrill', 'None', 3, 0),
           (16, 'Pidgey', 'Pidgeotto', 1, 18), (17, 'Pidgeotto', 'Pidgeot', 2, 36), (18, 'Pidgeot', 'None', 3, 0),
           (19, 'Rattata', 'Raticate', 1, 20), (20, 'Raticate', 'None', 2, 0),
           (21, 'Spearow', 'Fearow', 1, 20), (22, 'Fearow', 'None', 2, 0),
           (23, 'Ekans', 'Arbok', 1, 22), (24, 'Arbok', 'None', 2, 0),
           (25, 'Pikachu', 'Raichu', 1, 16), (26, 'Raichu', 'None', 2, 0),
           (27, 'Sandshrew', 'Sandslash', 1, 22), (28, 'Sandslash', 'None', 2, 0),
           (29, 'Nidoran (F)', 'Nidorina', 1, 16), (30, 'Nidorina', 'Nidoqueen', 2, 32), (31, 'Nidoqueen', 'None', 3, 0),
           (32, 'Nidoran (M)', 'Nidorino', 1, 16), (33, 'Nidorino', 'Nidoking', 2, 32), (34, 'Nidoking', 'None', 3, 0),
           ()
           )  # Pokedex pretty much. Contains [ID, current state, next state, form number, level to evolve

with open('master.dat', 'rt') as master:  # opens the master data file which contains the current unique number to
    # use for the next pokemon
    for line in master:
        masterData.append(int(line.rstrip()))  # puts the contents of the file into the previously declared masterData
        # array


def create_poke_data():
    x = 1
    data = []  # will contain the data for the new pokemon

    def roll_stats():  # used to roll the stats
        temp_data = [r.randint(1, 8), r.randint(1, 8), r.randint(1, 8), r.randint(1, 8), r.randint(1, 8)]
        return temp_data

    def find_poke_data(poke_choice):  # searches through the PokeDex
        for unit in range(0, len(POKEMON)):
            if poke_choice != 1 and POKEMON[unit][3] == 1:
                poke_choice -= 1
            elif poke_choice == 1 and POKEMON[unit][3] == 1:
                return POKEMON[unit]

    for n in range(1, len(POKEMON)-1):
        if POKEMON[n - 1][3] == 1:
            print(str(x) + ': ' + str(POKEMON[n - 1][1]))
            x += 1

    choice = int(input('Enter the number of the Pokemon you wish to create: '))

    current_id = masterData[0]
    data.append(current_id)
    poke_data = (find_poke_data(choice))
    data.append(poke_data[0])
    data.append(poke_data[1])

    stats = roll_stats()

    for item in stats:
        data.append(item)

    data.append(1)
    data.append(poke_data[4])
    data.append((poke_data[0] + 1))
    data.append(100)

    file_name = str(data[2])+str(data[0])+'.dat'

    current_id += 1

    with open('master.dat', 'wt') as master_dat:
        master_dat.write(str(current_id))

    with open(file_name, 'x') as create_file:
        for num in data:
            create_file.write(str(num)+'\n')


