from room import Room
from player import Player
from world import World
from ast import literal_eval


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# need to make a reverse dictionary with the opposite directions to back track 
reverse = {"n": "s", "s": "n", "e": "w", "w": "e"}

#use a function to generate the path we need to take 
    #we need to keep track of path we take, so this will passed into the argument 
def generate_path(visited_rooms = None):
    #visited_rooms is set to None, this is to set up a base case to use this function recursively

    
    if visited_rooms is None: 
        visited_rooms = set()
    
    #initialize the function with direction_history 
    direction_history = []
    #once we are in a room, in order to find the directions, we can use a method called  get_exits, once we have the exits, 
    for direction in player.current_room.get_exits():
        #  move in each of the  directions we have available
        player.travel(direction)
        # print("TRAVELING TO", direction)

        #once we are in the other room, we are checking if the room is in visited 
        if player.current_room.id not in visited_rooms:
            # if so, add the room to visited, also we need to keep track of the direction we took to get to this room. Add the direction we took to the path history.
            visited_rooms.add(player.current_room.id)
            # print("CURRENT ROOM", player.current_room.id)
            # print("VISITED ROOMS", visited_rooms)
            direction_history.append(direction)
            # print("DIRECTION HISTORY", direction_history)
            # recursively call the generate_path function passing in the visited rooms. We need to increment 
            direction_history = direction_history + generate_path(visited_rooms) 
            #if we reach a room where there are no exits except for where we have gone, we need to back track. 
            player.travel(reverse[direction])
            
            # Keep track of the directions taken. 
            direction_history.append(reverse[direction])

        # else it has been visited
        else:
            #back track to the previous room 
            player.travel(reverse[direction])
            # do not track this movement, because we will constantly be going into visited rooms
    
    #return the direction history 
    return direction_history

#call the function, and store the results in the traversal path
traversal_path = generate_path()
            

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)


#visited rooms counted with current room on each move 

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)
    # print("TRAVERSAL TEST", visited_rooms)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
