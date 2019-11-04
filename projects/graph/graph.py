"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise KeyError("Cannot create an edge based on given vertices.")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue
        qq = Queue()
        # Create list of visited nodes
        visited = set()
        # Put starting node in the queue
        qq.enqueue(starting_vertex)
        # While queue is not empty:
        while qq.size() > 0:
            # Pop first node out of queue
            vertex = qq.dequeue()
            # If node is not visited:
            if vertex not in visited:
                # Mark as visited
                visited.add(vertex)
                print(vertex)
                # Get adjacent edges and add to list
                for next_vert in self.vertices[vertex]:
                    qq.enqueue(next_vert)
            # Rerun loop
        


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()

        stack.push(starting_vertex)

        while stack.size() > 0:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                print(vertex)

                for next_vert in self.vertices[vertex]:
                    stack.push(next_vert)

        print(self.vertices)

    def dft_recursive(self, starting_vertex, visited_set = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """

        # From the starting vertex
        # pass in each child vertex to dft_recursive
        # if visited == None:
        #     visited = set()
        
        # if starting_vertex in visited:
        #     return


        print(starting_vertex)
        visited_set.add(starting_vertex)


        # Loop over all vertices connected to the starting vertex
        for vertex in self.vertices[starting_vertex]:
            # If any of the vertices has already been visited and is present in visited_set, do nothing
            if vertex not in visited_set:
                # Otherwise, call recursive function with self.vertices[vertex]
                self.dft_recursive(vertex, visited_set)




    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        if starting_vertex == destination_vertex:
            print(starting_vertex)
            return

        qq = Queue()
        visited = set()
        qq.enqueue([starting_vertex])

        while qq.size() > 0:
            # Take first element of the queue, this is a list showing how we got to this particular vertex in the queue.
            path = qq.dequeue()
            # Take last item of the list taken from the queue. This is the vertex we're currently at
            vertex = path[-1]

            # We're only interested in vertices we have not yet visited. So if the extracted vertex has been covered already, we're going to reloop
            if vertex not in visited:
                # If the last item of the list is the destination, we're good!
                if vertex == destination_vertex:
                    # Return the list showing the steps it took us to get here.
                    return path
                # Otherwise, add the vertex to visited and keep going
                visited.add(vertex)

                # For all the vertices associated with the current vertex
                for next_vertice in self.vertices[vertex]:
                    # Take the path we used to get to this vertex
                    next_path = list(path)
                    # And add the vertex assocociated with the current vertex
                    next_path.append(next_vertice)
                    # Store the list in the Queue and reloop
                    qq.enqueue(next_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO





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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\nStarting DFT")
    graph.dft(1)

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
    print("\nStarting BFT")
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\nStarting DFT recursive")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("\nStarting Breadth-First Search")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
