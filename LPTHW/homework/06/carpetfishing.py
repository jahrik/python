from random import *
# from time import *

def Carpet_Fishing():
    Grid = ('grid 1', 'grid 2', 'grid 3',
            'grid 4', 'grid 5', 'grid 6',
            'grid 7', 'grid 8', 'grid 9')
    Fish = ('Marlin', 'Salmon', 'Sea Robin',
            'Shad', 'Sea Bass', 'Perch',
            'Catfish', 'Largemouth Bass', 'Clown')
    print choice(Fish), 'in', choice(Grid), '\n'
#    sleep(3600)

while 1:
    Carpet_Fishing()

