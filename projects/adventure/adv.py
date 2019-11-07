from room import Room
from player import Player
from world import World
from room_storage import roomGraph

import random

# Load world
world = World()



world.loadGraph(roomGraph)

# UNCOMMENT TO VIEW MAP
world.printRooms()

player = Player("Name", world.startingRoom)

# Fill this out
traversalPath = []


# Function that fills traversalpath with directions that, when walked in order, will visit every room on the map at least once

# Probably need a combination of BFS & DFS

# Create a loop/process that:
    # - Tries moving in a particular direction
    # - If you find yourself in a new room, update the entries on your graph (showing that the previous room has an exit that leads to the current room and vice versa)

    # Base case is when there are exactly 500 entries in the graph & no `'?'` in the adjacency dictionairies

# Do a BFS to find the nearest room with `?` for an exit.
# Then, do a DFS on everything past the '?' until it runs into a case where there are no more '?'. Adding the rooms to traversalPath all the while.
    # In that case, move back up the stack until there is one.

# Create traversal path:
# BFS out from world.startingRoom















# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)

for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph):
    print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")
