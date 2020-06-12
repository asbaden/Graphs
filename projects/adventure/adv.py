from room import Room
from player import Player
from world import World
from util import Stack
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


#`player.current_room.id` will return the current room, `player.current_room.get_exits()` will show rthe available neighbors, and `player.travel(direction)` will move the player 
# edges will the dictionary get exits provides with the av
# To iterate through the list in a dft function  create a helper function that uses the "travel" method from player to move in a direction
# similar to the traversal test below, add that direction of that move to the traversal path to keep track of the moves 

# create a dictionary called backtrack with the swaped values of direciton to move in the opposite direction 

# Use a DFS function that utilizes back tracking with visited and move as arguments set to none
    # set the current room to the player.current_room.id
    # create the edges with setting neighbors to player.current_room.get_exits()
    # create a conditional checking if no nodes have been visited, create a set(dictionary) to store the nodes we visit






# Movement in the dft function

def DFS_util(direction):
    player.travel(direction)
    traversal_path.append(direction)
    print("this is traversal path", traversal_path)

# print("this is current room", player.current_room.id)

print("this is testing uutil", DFS_util("n"))





# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

#visited rooms counted with current room on each move 

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
