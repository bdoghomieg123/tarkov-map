
import random as rando
import time

maps = ['Reserve', 'Factory' , 'Customs' , 'Interchange' , 'Woods' , 'Shoreline' , 'Lighthouse' , 'Streets of Tarkov']

#Change this line to True if you have a labs card
labs = False

if labs:
    maps.append("Labs")

for x in range(10):

    print("Loading...")

    time.sleep(1)

print(f'Play the map: {rando.choice(maps)}')
