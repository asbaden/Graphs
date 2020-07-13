"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        #check if verts in the graph
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")

        
        pass  # TODO

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #created a set to stores visited vertices
        visited = set()
        #create a queue for bredth-first-traversal
        qq = Queue()
        #enqueue the startign node
        qq.enqueue(starting_vertex)
        #while the queue isn't empty
        while qq.size() > 0:
            #when you dequeue, you need to point/store the vertex 
            #dequeue the first vertex
            vertex = qq.dequeue()
            #if that vertex is not in visited, we need to add it to the visited set before moving on 
            if vertex not in visited:
                #print the vertex to follow the directions
                print(vertex)
                #add the vertex to the visited set
                visited.add(vertex)
                #loop through the neighbors connected to the visited vertex using the method above
                for next_vert in self.get_neighbors(vertex):
                    #enqueue those neighbors
                    qq.enqueue(next_vert)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        ss = Stack()

        ss.push(starting_vertex)
        while ss.size() > 0:
            vertex = ss.pop()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for next_vert in self.get_neighbors(vertex):
                    ss.push(next_vert)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #create a visited set/ base case
        if visited is None:
            visited = set()
        #add the started vertex to visited
        visited.add(starting_vertex)
        print(starting_vertex)
        # create a loop through the vertex to get the neighbors
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)



    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #inititize visited 
        visited = set()
        #create a queue
        #enquee the starting vertex 
        qq = Queue()
        qq.enqueue([starting_vertex])


        #while queue is not empty 
       
        while qq.size() > 0:
            #dequeue the vertex that will be the path 
            path = qq.dequeue()
            # print("THIS IS REG PATH", path)
            # print("This is last path", path[-1])
            #if the last vertex is not visited 
            if path[-1] not in visited:
                # if the  vertex is the desination vertex
                if path[-1] == destination_vertex:
                    #return the path
                    return path
                #if the vertex is not in visited, add it
                visited.add(path[-1])
                #for loop to get the neghbors of the vertex
                for next_vert in self.get_neighbors(path[-1]):
                    #create a new path
                    new_path = list(path)
                    #append the next vert
                    new_path.append(next_vert)
                    #enqueue the path 
                    qq.enqueue(new_path)
            

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #initialze a visited set 
        visited = set()
        #create a stack 
        ss = Stack()
        #push the starting vertex 
        ss.push([starting_vertex])
        # print("starting vertex", starting_vertex)
        # print("[starting_vertex]", starting_vertex)
        #while the stack is not empty 
        while ss.size() > 0:
            #pop the vertex that will be the path 
            path = ss.pop()
            #check the last vertex is in visited
            if path[-1] not in visited:
                #check if the desination vertex is equal to  path[-1]
                if path[-1] == destination_vertex:
                    return path
                #add path
                visited.add(path[-1])
                #for loop to get the neighbors of the vertex 
                for next_vert in self.get_neighbors(path[-1]):
                    #create a new path 
                    new_path = list(path)
                    #append the next vert 
                    new_path.append(next_vert)
                    #push the path to the stack
                    ss.push(new_path)
            

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        #we will need 3 base cases: visited, path, and if the starting vertex is the destination vertexh
        if visited is None:
            visited = set()
        if path is None:
            path = []
        
        #add the starting vertex to visited
        visited.add(starting_vertex)
        #create a new path 
        new_path = path + [starting_vertex]

        print("new path", new_path)
        # check if the passed vertex is the destination vertex 
        if starting_vertex == destination_vertex:
            return new_path
        # we need to get the neighbors of the starting vertex
        for neighbor in self.vertices[starting_vertex]:
            #check if the neighbor is not in visited
            if neighbor not in visited:
                #create a path by recursivelly calling the function
                neighbor_path = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
                #if the neighbor_path exists
                if neighbor_path:
                    
                    return neighbor_path
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
