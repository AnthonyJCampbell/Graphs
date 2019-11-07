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
        # Remove item from stack
        current_room = stack.pop()
        # Evaluate if we've already visited current room
        if current_room.id not in visited:
            # If not, add current_room to visited
            visited.append(current_room.id)

            # Track stack size before evaluating rooms and exits
            stack_size_before = len(stack)

            # Declare a neighbouring rooms dict, which we'll use to store the exits in the neighbouring rooms to evaluate possible dead-ends.
            neighbouring_rooms = {'n': None, 'w': None, 's': None, 'e': None}

            for direction in current_room.getExits():
                room = current_room.getRoomInDirection(direction)
                neighbouring_rooms[direction] = room

            # print(neighbouring_rooms)

            # Create a list that only contains the neighbouring rooms which have exits themselves. Any neighbours that do not have more exits are disregarded.
            dict_with_no_none = [i for i in neighbouring_rooms.items() if i[1] != None]
            # print(dict_with_no_none)

            # Sort the list from room with most exits to least. The one with the fewest exits should be visited first, so it will get added to the stack last.
            sorted_obj = sorted(
                dict_with_no_none, key=lambda room: len(room[1].getExits()), reverse=True)
            # print("here")
            # print(sorted_obj)

            # Check every room in sorted_obj to see if we've already visited it
            for room in sorted_obj:
                # If not, add it to stack
                if room[1].id not in visited:
                    stack.append(room[1])

            # Check if stack_size is larger than what it was in the beginning (stack_size_before)
            # If the lenghts are equal, we have not pushed any rooms to the stack, so we're at a dead end. Therefore, we should start BFT
            # If it's different, we should just reloop
            if len(stack) == stack_size_before:

                # declare shortest path list
                shortest_path = []
                try:
                    # If the current room id is the same as the id of the next room on the stack, we're at risk of beginning a looped cycle. In that case, we should take the second item of the stack [-2].id as target for our bfs (if it exists)
                    # If there is no second item in the stack, we're done!
                    if current_room.id == stack[-1].id:
                        shortest_path = bfs(current_room, stack[-2])

                    # Call BFS with current room and the last/uppermost item in the stack
                        # bfs(current_room, stack[-1])
                    else:
                        shortest_path = bfs(current_room, stack[-1])

                    # append paths traversed with BFS to visited list
                    # except the first and the last node
                    # as they are added to the traversed path with DFT (unvisited nodes at this point)
                    for i in range(1, len(shortest_path)-1):
                        visited.append(shortest_path[i])
                
                except:
                    print("done")
    
    return visited

def bft(starting_room, target_room):
    qq = []
    enqueue(qq, {"node": starting_room, "path": []})
    visited = set()

    while len(qq) > 0:
        # current room is dequeue(qq)
        current_room = dequeue(qq)
        # check if current room[starting_room].id is not in visited
        if current_room[starting_room].id not in visited:
            # If so, add current_room[starting_room].id to current_room[path]
            visited.add(current_room["node"].id)

            if current_room["node"].id == target_room.id:
            # This means we've reached the next item in our stack on DFS and we're good to go for another iteration of DFS
                # Add current_room[starting_room].id to current_room[path]
                current_room["path"].append(current_room["node"].id)
                return current_room["path"]

            # Otherwise, we should add all neighbouring nodes to the queue to go for another round of BFS
            for direction in current_room["node"].getExits():
                # set currently_evaluated_room to current_room["node"].getRoomInDirection(direction)
                currently_evaluated_room = current_room["node"].getRoomInDirection(direction)

                # Create a copy of the path we took to get here
                path_copy = current_room["path"]
                path_copy.append(current_room["node"].id)

                # Add new path to queue
                enqueue(qq, {"node": currently_evaluated_room, "path": path_copy})


        else:
            dequeue(qq)
    return None









def enqueue(queue, data):
    queue.insert(0, data)

def dequeue(queue):
    if len(queue)>0:
        return queue.pop()
    return ("Queue empty!")



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
