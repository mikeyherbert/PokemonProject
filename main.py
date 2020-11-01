"""
File Standard for Pokemon:
ID 0
pokemonID 1
name 2
strength 3
dexterity 4
intelligence 5
luck 6
charm 7
level 8
levelEvolve 9
evolveID 10
HP 11
nickname 12
"""

import random as r
import os

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
           (35, 'Clefairy', 'Clefable', 1, 16), (36, 'Clefable', 'None', 2, 0),
           (37, 'Vulpix', 'Ninetales', 1, 16), (38, 'Ninetales', 'None', 2, 0),
           (39, 'Jigglypuff', 'Wigglytuff', 1, 16), (40, 'Wigglytuff', 'None', 2, 0),
           (41, 'Zubat', 'Golbat', 1, 22), (42, 'Golbat', 'None', 2, 0),
           (43, 'Oddish', 'Gloom', 1, 21), (44, 'Gloom', 'Vileplume', 2, 30), (45, 'Vileplume', 'None', 3, 0),
           (46, 'Paras', 'Parasect', 1, 24), (47, 'Parasect', 'None', 2, 0),
           (48, 'Venonat', 'Venomoth', 1, 31), (49, 'Venomoth', 'None', 2, 0),
           (50, 'Diglett', 'Dugtrio', 1, 26), (51, 'Dugtrio', 'None', 2, 0)
           )  # t0w0ple. Contains [ID, current state, next state, form number, level to evolve

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

    for n in range(1, len(POKEMON)-1): # prints all the basic pokemon
        if POKEMON[n - 1][3] == 1:
            print(str(x) + ': ' + str(POKEMON[n - 1][1]))
            x += 1

    choice = int(input('Enter the number of the Pokemon you wish to create: '))

    current_id = masterData[0]
    data.append(current_id)
    poke_data = (find_poke_data(choice)) # calls local function to get the basic data of the chosen pokemon from the pokedex
    data.append(poke_data[0])
    data.append(poke_data[1])

    stats = roll_stats() # calls local function to get stats for pokemon

    for item in stats:
        data.append(item) # adds the stats onto the data array

    data.append(1)
    data.append(poke_data[4]) #level it evolves
    data.append((poke_data[0] + 1)) # evolveID
    data.append(100) # hp

    print('You created a new Pokemon!')
    print('Type: '+data[2])
    print('ID: '+str(data[0]))
    print('Pokedex ID: '+str(data[1]))
    print('Strength: '+str(data[3]))
    print('Dexterity: ' + str(data[4]))
    print('Intelligence: '+str(data[5]))
    print('Luck: '+str(data[6]))
    print('Charm: '+str(data[7]))

    nick_q = input('Would you like to give your new pokemon a nickname? Y/N: ').capitalize()

    if nick_q == 'Y':
        nickname = input('Please enter the nickname for your pokemon: ')
    else:
        nickname = 'N/A'

    data.append(nickname)

    file_name = str(data[2])+str(data[0])+'.dat'

    current_id += 1

    with open('master.dat', 'wt') as master_dat:
        master_dat.write(str(current_id)) # overwrites the master file with the next pokemon id

    with open('data/'+file_name, 'x') as create_file:
        for num in data:
            create_file.write(str(num)+'\n') # creates the pokemons save file with its data


def check_poke_stats():
    all_poke = [] # i hate commenting

    for file in os.listdir('data'):
        temp_array = []
        if file.endswith('.dat'):
            with open('data/'+file) as f:
                for line in f:
                    temp_array.append(line.rstrip())
                all_poke.append(temp_array) # places the data of each pokemon into a temporary array, then that array is appended to the all_poke array

    for n in range(0, len(all_poke)):
        if str(all_poke[n][11]) != 'N/A':
            print(str(n+1)+'. Level ' + str(all_poke[n][8]) + ' ' + all_poke[n][2] + ' ('+all_poke[n][12]+')')
        elif str(all_poke[n][11]) == 'N/A':
            print(str(n+1)+'. Level ' + str(all_poke[n][8]) + ' ' + all_poke[n][2])

    choice = int(input('Please enter the number of the pokemon you want to check: '))

    if not choice > len(all_poke):
        evo = int(all_poke[choice-1][10])
        print('Type: ' + all_poke[choice-1][2])
        print('ID: ' + str(all_poke[choice-1][0]))
        print('Pokedex ID: ' + str(all_poke[choice-1][1]))
        print('Strength: ' + str(all_poke[choice-1][3]))
        print('Dexterity: ' + str(all_poke[choice-1][4]))
        print('Intelligence: ' + str(all_poke[choice-1][5]))
        print('Luck: ' + str(all_poke[choice-1][6]))
        print('Charm: ' + str(all_poke[choice-1][7]))
        print('Evolves to: '+str(POKEMON[evo-1][1])+' at level '+str(all_poke[choice-1][9])) # if you can read you know what it does


def evolve_pokemon():
    all_poke = [] # on the other hand, i love arrays

    for file in os.listdir('data'):
        temp_array = []
        if file.endswith('.dat'):
            with open('data/' + file) as f:
                for l in f:
                    temp_array.append(l.rstrip())
                all_poke.append(temp_array)

    for n in range(0, len(all_poke)):
        if str(all_poke[n][11]) != 'N/A': # distinguishes if there is a nickname
            print(str(n + 1) + '. Level ' + str(all_poke[n][8]) + ' ' + all_poke[n][2] + ' (' + all_poke[n][12] + ')')
        elif str(all_poke[n][11]) == 'N/A': # or not
            print(str(n + 1) + '. Level ' + str(all_poke[n][8]) + ' ' + all_poke[n][2]) # and prints the pokemon out


    choice = int(input('Which pokemon would you like to evolve? Enter the number here: '))

    if not choice > len(all_poke):
        data = all_poke[choice-1]
        if data[10] != -1:
            if int(data[8]) == int(data[9]):
                file = str(data[2])+str(data[0])+'.dat'
                print('Current level: ' + str(data[8]))
                print('Required level: ' + str(data[9]))
                print('This pokemon will now be evolved! ')

                data2 = POKEMON[int(data[10])-1]
                print(data)
                print(data2)

                data[1] = data2[0]
                data[2] = data2[1]
                if data2[2] != 'None':
                    data[10] = int(data[10])
                    data[10] += 1
                else:
                    data[10] = -1

                data[3] = int(data[3]) #everyone
                data[4] = int(data[4]) #loves
                data[5] = int(data[5]) #bloody
                data[6] = int(data[6]) #data
                data[7] = int(data[7]) #types

                data[3] += int(r.randint(1, 8)) #augyfduaghdfjknabskdj
                data[4] += int(r.randint(1, 8))
                data[5] += int(r.randint(1, 8))
                data[6] += int(r.randint(1, 8)) #that was random
                data[7] += int(r.randint(1, 8)) #get it...?

                data[9] = str(data2[4])

                print(data)
                print(file)

                new_file = str(data[2])+str(data[0])+'.dat' # its 11:30pm my patience for these bLooDY commenTs is running very thin

                with open('data/'+file, 'wt') as f:
                    for l in data:
                        f.write(str(l) + '\n')

                os.rename('data/'+file, 'data/'+new_file) # IT RENAMES IT

            else:
                print('Current level: ' + str(data[8]))
                print('Required level: ' + str(data[9]))
                print('This pokemon cannot be evolved! ')


def battle_pokemon():
    all_poke = [] # MakeArraysGreatAgain2020

    for file in os.listdir('data'):
        temp_array = []
        if file.endswith('.dat'):
            with open('data/' + file) as f: # fishes thru the dat files
                for l in f:
                    temp_array.append(l.rstrip())
                all_poke.append(temp_array)

    def print_pokemon(): # prints the pokemon, like in the check stats procedure
        for n in range(0, len(all_poke)): # im blue
            if str(all_poke[n][11]) != 'N/A': # da ba dee
                print(str(n + 1) + '. Level ' + str(all_poke[n][8]) + ' ' + all_poke[n][2] + ' (' + all_poke[n][12] + ')')
            elif str(all_poke[n][11]) == 'N/A': # da ba da
                print(str(n + 1) + '. Level ' + str(all_poke[n][8]) + ' ' + all_poke[n][2])

    print_pokemon()

    choice1 = 0
    choice2 = 0

    while not 0 < choice1 <= len(all_poke):
        choice1 = int(input('Enter the number of the first pokemon to battle: '))
        poke_choice1 = all_poke[choice1 - 1]

    print_pokemon() # 'Another one.' - Khaled Mohamed Khaled 2018

    while choice2 != choice1 and not 0 < choice2 <= len(all_poke):
        choice2 = int(input('Enter the number of the second pokemon to battle: '))
        if choice2 == choice1:
            print("You can't make it fight itself!") # low key want to smack whatever imbecile would try that
            choice2 = 0
        poke_choice2 = all_poke[choice2 - 1]

    rounds = [r.randint(1, 5)+2, r.randint(1, 5)+2, r.randint(1, 5)+2]
    stats = ['STR', 'DEX', 'INT', 'LCK', 'CHM']
    score1: int = 0
    score2 = 0
    winner = None
    roundN = 0
    go = True

    file1 = poke_choice1[2]+poke_choice1[0]+'.dat'
    file2 = poke_choice2[2]+poke_choice2[0]+'.dat'

    while go: # WHY WHY WHY WHY WHYYYYYYYYYYYYYYYYYYYYYY
            while score1 < 2 and score2 < 2: # I HATE LOGIC AT 11PM
                if int(poke_choice1[rounds[roundN]]) > int(poke_choice2[rounds[roundN]]):
                    score1 += 1
                    print(poke_choice1[2] + ' had higher '+stats[rounds[roundN]-3]+' than '+poke_choice2[2])
                    print('Score: ' + poke_choice1[2], str(score1), 'vs', str(score2), poke_choice2[2])
                    roundN += 1
                elif int(poke_choice1[rounds[roundN]]) < int(poke_choice2[rounds[roundN]]):
                    score2 += 1
                    print(poke_choice2[2] + ' had higher ' + stats[rounds[roundN] - 3] + ' than ' + poke_choice1[2])
                    print('Score: '+poke_choice1[2], str(score1), 'vs', str(score2), poke_choice2[2])
                    roundN += 1
                else: # it makes sense somehow that this works, i mean why not coinflip like real men
                    flip_coin = r.randint(1, 2)
                    if flip_coin == 1:
                        score1 += 1
                        print('The two '+stats[rounds[roundN]-3]+' stats were equal, so a coin was flipped and '+poke_choice1[2]+
                             ' won!')
                        print('Score: ' + poke_choice1[2], str(score1), 'vs', str(score2), poke_choice2[2])
                        roundN += 1
                    else:
                        score2 += 1
                        print('The two '+stats[rounds[roundN] - 3]+' stats were equal, so a coin was flipped and '+poke_choice1[2]+
                                ' won!')
                        print('Score: ' + poke_choice1[2], str(score1), 'vs', str(score2), poke_choice2[2])
                        roundN += 1
            go = False

    winner = 1 if score1 == 2 else 2 # cause 3 lines for this is just 'Stoopid' - 6ix-9ine 2019

    if winner == 1:
        print(str(poke_choice1[2])+ ' was the winner! They leveled up to level '+str(int(poke_choice1[8])+1)+'!')

        poke_choice2[11] = int(poke_choice2[11]) - 50
        if poke_choice2[11] == 0:
            print('Unfortunately, '+str(poke_choice2[2])+' died.') #F
            os.remove('data/'+file2)
        else:
            print(str(poke_choice2[2])+ ' lost 50 HP!')
            with open('data/' + file2, 'wt') as f: # FILES
                for l in poke_choice2:
                    f.write(str(l) + '\n')
        poke_choice1[8] = int(poke_choice1[8])+1

        with open('data/' + file1, 'wt') as f:
            for l in poke_choice1:
                f.write(str(l) + '\n')



    else:
        print(str(poke_choice2[2])+ ' was the winner! They leveled up to level '+str(int(poke_choice2[8])+1)+'!')
        poke_choice1[11] = int(poke_choice1[11]) - 50
        if poke_choice1[11] == 0:
            print('Unfortunately, ' + str(poke_choice1[2]) + ' died.') #F
            os.remove('data/'+file1)
        else:
            print(str(poke_choice1[2]) + ' lost 50 HP!')
            with open('data/' + file1, 'wt') as f: # FILES
                for l in poke_choice1:
                    f.write(str(l) + '\n')
        poke_choice2[8] = int(poke_choice2[8]) + 1

        with open('data/' + file2, 'wt') as f:
            for l in poke_choice2:
                f.write(str(l) + '\n')


if __name__ == '__main__': # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH
    print('Menu:')
    print('1. Create a new pokemon\n2. Check on one of your pokemon\n3. Evolve a pokemon\n4. Battle two of your pokemon')
    choice = input()
    if choice == '1':
        create_poke_data()
    elif choice == '2':
        check_poke_stats()
    elif choice == '3':
        evolve_pokemon()
    elif choice == '4':
        battle_pokemon()
    else:
        print('Invalid choice! Program will now self-destruct...') # https://www.youtube.com/watch?v=SxXdE7pBTjQ