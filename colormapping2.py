# A class to represent a graph object
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# Function to assign colors to vertices of a graph
def colorGraph(graph, n):
 
    # keep track of the color assigned to each vertex
    result = {}
 
    # assign a color to vertex one by one
    for u in range(n):
 
        # check colors of adjacent vertices of `u` and store them in a set
        assigned = set([result.get(i) for i in graph.adjList[u] if i in result])
 
        # check for the first free color
        color = 1
        for c in assigned:
            if color != c:
                break
            color = color + 1
 
        # assign vertex `u` the first available color
        result[u] = color
 
    for v in range(n):
        print(f'Color assigned to vertex {v} is {colors[result[v]]}')
 
 
# Greedy coloring of a graph
if __name__ == '__main__':
 
    # Add more colors for graphs with many more vertices
    colors = ['', 'BLUE', 'GREEN', 'RED', 'YELLOW', 'ORANGE', 'PINK',
            'BLACK', 'BROWN', 'WHITE', 'PURPLE', 'VOILET']
 
    # List of graph edges as per the above diagram
    edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]
 
    # total number of nodes in the graph (labelled from 0 to 5)
    n = 6
 
    # build a graph from the given edges
    graph = Graph(edges, n)
 
    # color graph using the greedy algorithm
    colorGraph(graph, n)
 
