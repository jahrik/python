## 
from nose.tools import *
## 
from ex47.game import Room


def test_room():
	## create an object from the class Room(), named GoldRoom.
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""")
    ## test to see if gold.name equals "GoldRoom"
	assert_equal(gold.name, "GoldRoom")
    ## gold.paths should contain an empty dictionary
	assert_equal(gold.paths, {})

def test_room_paths():
    ## create center Room() object, named "Center"
	center = Room("Center", "Test room in the center.")
    ## create north Room() object, named "North"
	north = Room("North", "Test room in the north.")
    ## create north Room() object, name "South"
	south = Room("South", "Test room in the south.")

    ## add a dictionary to center object
	center.add_paths({'north': north, 'south': south})
    ## test to see if north equals north in the center.path dictionary.
	assert_equal(center.go('north'), north)
    ## test to see if south equals south in the center.path dictionary.
	assert_equal(center.go('south'), south)

def test_map():
    ## create a start Room() object
	start = Room("Start", "You can go west and down a hole.")
    ## create a west Room() object
	west = Room("Trees", "There are trees here, you can go east.")
    ## create a down Room() object
	down = Room("Dungeon", "It's dark down here, you can go up.")

    ## add a dictionary to start with the values west and down.
	start.add_paths({'west': west, 'down': down})
    ## add a dictionary to west with the value east
	west.add_paths({'east': start})
    ## add a dictionary to down with the value up
	down.add_paths({'up': start})

    ## test to see if you can go west from start
	assert_equal(start.go('west'), west)
    ## test to see if you can go west and then east from start
	assert_equal(start.go('west').go('east'), start)
    ## test to see if you can go down and up from start
	assert_equal(start.go('down').go('up'), start)
