from stack_array import * #Needed for Depth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.visited = False


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, ad_list):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified
           in the input file should appear on the adjacency list of each vertex of the two vertices associated
           with the edge.'''
        # This method should call add_vertex and add_edge
        self.graph = {} #creates a graph as a dictionary
        
        for i in range(0, len(ad_list)-1, 2): #adds vertexes to graph
            if(ad_list[i] not in self.graph):
                self.add_vertex(ad_list[i])
            if(ad_list[i+1] not in self.graph):
                self.add_vertex(ad_list[i+1])
            self.add_edge(ad_list[i], ad_list[i+1])
            #print(self.graph[ad_list[i]].id)


    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        # Should be called by init
        vert = Vertex(key) #adds it into dictionary
        self.graph[key] = vert

    def add_edge(self, v1, v2):
        # Should be called by init
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.graph[v1].adjacent_to.append(v2) #adds each vertex to eachothers adj. list
        #self.graph[v2].adjacent_to.append(v1)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if key in self.graph:
            return self.graph[key] #returns the vertex id if in the dictionary
        else:
            return None

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        lst = self.graph.values() #gets the list of Vertex Objects
        vert_list = []
        for i in lst:
            vert_list.append(i.id) #makes list of only id's
        vert_list.sort() #sorts the list
        return vert_list
    
    def dsf_1(self, vert, stack):
        self.graph[vert].visited = True
        for i in self.graph[vert].adjacent_to:
            if self.graph[i].visited == False:
                self.dsf_1(i, stack)
        stack.push(self.graph[vert])
    
    def dsf_2(self, vert):
        vert.visited = True
        temp = str(vert.id)
        temp += ", "
        for i in vert.adjacent_to:
            if self.graph[i].visited == False:
                temp += self.dsf_2(self.graph[i])
                #print(temp)
        return temp

    def transpose(self, ad_list):
        self.graph = {} #creates a graph as a dictionary
        for i in range(0, len(ad_list)-1, 2): #adds vertexes to graph
            if(ad_list[i+1] not in self.graph):
                self.add_vertex(ad_list[i+1])
            if(ad_list[i] not in self.graph):
                self.add_vertex(ad_list[i])
            self.add_edge(ad_list[i+1], ad_list[i])
            self.graph[ad_list[i]].visited = False
            self.graph[ad_list[i+1]].visited =False
            #print(self.graph[ad_list[i]].id)
