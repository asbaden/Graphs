
# Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.


# Clarifications:
# * The input will not be empty.
# * There are no cycles in the input.
# * There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
# * IDs will always be positive integers.
# * A parent may have any number of children.


#will use DFT to find the earliest ancestor 
#the parent is always on the left side of the tuple

from graph import Graph
from util import Stack


def earliest_ancestor(ancestors, starting_node):
    # import our graph and assign it to a variable in order to make the input tuples into a graph that we can traverse
    gg = Graph()


    # loop through the ancestors to add vertices 
    for pair in ancestors:
        gg.add_vertex(pair[0])
        gg.add_vertex(pair[1])
        # print("THIS IS PAIR", pair)

    # loop through the ancestors to add edges from the child to the parent 
    for pair in ancestors:
        gg.add_edge(pair[1], pair[0])
        print("THIS IS PAIR", pair)
       
    # implemnet  depth-first-traversal
    # assign Stack to a veriable
    ss = Stack()
    # we are tracking the path traversed to find the earliest ancestor, so we will need a variable assigned to path 
    path = []
    # need to initialize the eariliest ancestor as -1 
    earliest_ancestor = - 1
    #we need to initialze a maxium_length as 1 because thats the farthest you could go if the node had no ancestors 
    maximum_length = 1 

    #push the startign node to the stack so the loop will run 
    ss.push([starting_node])
    while ss.size() > 0:
        #pop the the starting node to begin the path 
        path = ss.pop()
        #in order to identify an individual node form path, we will create a variable assigned to the last node in the path
        curr = path[-1]
        # conditional for adding things to the path 
        # we are looking for the nodes that are furthest away and in the event two nodes are the same distance waya, we are loking for the one with a lesser value

        if (len(path) >= maximum_length and curr < earliest_ancestor) or len(path) > maximum_length:
            #conditional passed, we found nodes to go, update the maxium length and the earliest ancestor
            maximum_length = len(path)
            earliest_ancestor = curr
        #create a for loop to retrieve the next nodes to go
        for next_node in gg.vertices[curr]:
            #create a new path
            new_path = list(path)
            #append the next vertices 
            new_path.append(next_node)
            #push the pth to the stack
            ss.push(new_path)
    return earliest_ancestor
    