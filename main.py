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

-------------------------
Master file template:
currentID
-------------------------

with open('test.dat', 'rt') as file:
    myArray = []
    for line in file:
        myArray.append(int(line.rstrip()))

print(myArray)
print('Luck: '+str(myArray[5]))
"""
import random as r

masterData = []
baseList = [['Bulbasaur', ''], 'Charmander', 'Squirtle', 'Caterpie', 'Weedle', 'Pidgey', 'Rattata', 'Spearow', 'Ekans',
            'Pikachu', 'Sandshrew', 'Nidoran (F)', 'Nidoran (M)', 'Clefairy', 'Vulpix', 'Jigglypuff', 'Zubat',
            'Oddish', 'Paras', 'Venonat', 'Diglett']

with open('master.dat', 'rt') as master:
    for line in master:
        masterData.append(int(line.rstrip()))


def create_poke():
    data = []

    def roll_stats():
        temp_data = [r.randint(1, 5), r.randint(1, 5), r.randint(1, 5), r.randint(1, 5), r.randint(1, 5)]
        return temp_data

    for n in range(1, len(baseList)+1):
        print(str(n) + ': ' + baseList[n-1])

    choice = int(input('Enter the number of the Pokemon you wish to create: '))
    if 1 <= choice <= 21:
        if choice == 1:
            poke_id = 1
        elif choice == 2:
            poke_id = 4
        elif choice == 3:
            poke_id = 7
        elif choice == 4:
            poke_id = 10
        elif choice == 5:
            poke_id = 13
        elif choice == 6:
            poke_id = 16
        elif choice == 7:
            poke_id = 19
        elif choice == 8:
            poke_id = 21
        elif choice == 9:
            poke_id = 23
        elif choice == 10:
            poke_id = 25
        elif choice == 11:
            poke_id = 27
        elif choice == 12:
            poke_id = 29
        elif choice == 13:
            poke_id = 32
        elif choice == 14:
            poke_id = 35
        elif choice == 15:
            poke_id = 37
        elif choice == 16:
            poke_id = 39
        elif choice == 17:
            poke_id = 41
        elif choice == 18:
            poke_id = 43
        elif choice == 19:
            poke_id = 46
        elif choice == 20:
            poke_id = 48
        else:
            poke_id = 50
    else:
        print('Choice not in range...')

    cID = masterData[0]
    data.append(cID)
    data.append(poke_id)
    stats = roll_stats()
    for i in stats:
        data.append(stats[i-1])
    data.append(1)
    print(data)


create_poke()
