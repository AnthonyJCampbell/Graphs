from room import Room
from player import Player
from world import World
from room_storage import roomGraph1 as roomGraph


# Load world
world = World()
world.loadGraph(roomGraph)
world.printRooms()
player = Player("Name", world.startingRoom)



# Create a loop/process that:
    # - Tries moving in a particular direction
    # - If you find yourself in a new room, update the entries on your graph (showing that the previous room has an exit that leads to the current room and vice versa)

    # Base case is when there are exactly 500 entries in the graph & no `'?'` in the adjacency dictionairies

# Do a BFS to find the nearest room with `?` for an exit.
# Then, do a DFS on everything past the '?' until it runs into a case where there are no more '?'. Adding the rooms to traversalPath all the while.
    # In that case, move back up the stack until there is one.




# start at player.currentRoom

# run DFT until you hit dead end (room with no unvisited neighbours) OR you have visited every room

# on every move, add room to traversalPath
# mark every visited room as visited

# if you find a room with no more unvisited neighbours (dead end)

# run BFT to find SHORTEST PATH to first room that is unvisited
# on every move to that room save path
# then run this path with the player so you get to that room

# continute DFT loop (until you find another dead end, then repeat BFT again)

# >>> Create separate functions for DFT and BFT

def dft(player):
    visited = []
    stack = []
    stack.append(player.currentRoom)

    while len(stack) > 0:
        # run DFT
        # Remove item from stack
        # Evaluate if we've already visited current room
            # If not, add current_room to visited

            # Track stack size before evaluating rooms and exits

            # Declare a neighbouring rooms dict, which we'll use to store the exits in the neighbouring rooms to evaluate possible dead-ends.
            # neighbouring_rooms = {'n': None, 'w': None, 's': None, 'e': None}

            # for room in current_room.getExits():
                # room = current_room.getRoomInDirection(direction)
                # neighbouring_rooms[direction] = room

        # else reloop
        pass
    pass

def bft():
    pass

print(player.currentRoom.getRoomInDirection('n'))












traversalPath = dft(player)

print(f'path: {traversalPath}')
print(f'path length: {len(traversalPath)}')




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
