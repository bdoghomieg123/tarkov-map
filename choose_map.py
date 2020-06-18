
import random as rando
import time

maps = ['Reserve', 'Factory' , 'Customs' , 'Interchange' , 'Woods' , 'Shoreline']

#Change this line to True if you have a labs card
labs = False

if labs:
    maps.append("Labs")

for x in range(10):



    print("Go fuck yourself")

    time.sleep(1)

print(f'Play the map: {rando.choice(maps)}')
