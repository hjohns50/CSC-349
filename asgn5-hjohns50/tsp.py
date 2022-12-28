from stack_array import * #Needed for Depth First Search
from graph import * #graph class
import sys



def kruskal(graph):
    edges = []
    for vertex in graph:
        for neighbor in graph[vertex].items():
            edges.append((vertex, neighbor[0], neighbor[1]))
    edges = sorted(edges, key=lambda x: x[2])

    forest = [{v} for v in graph.keys()]
    mst = []

    for edge in edges:
        u_set = next(filter(lambda s: edge[0] in s, forest))
        v_set = next(filter(lambda s: edge[1] in s, forest))

        if u_set != v_set:
            mst.append(edge)
            forest.remove(u_set)
            forest.remove(v_set)
            forest.append(u_set | v_set)
    
    return mst
def find_hamiltonian_cycle(mst_graph, start):
    ham = []
    visited = set()
    stack = Stack((len(mst_graph))*10)
    stack.push(start[0])
    while not stack.is_empty():
        node = stack.pop()
        visited.add(node)
        ham.append(node)
        neighbors = mst_graph[node]
        for neighbor in neighbors:
            if  neighbor not in visited:
                stack.push(neighbor)
    ham.append(start[0])
    return ham

def main():
    graph = Graph()
    graph = graph.from_file(str(sys.argv[1]))
    mst = kruskal(graph)
    mst_graph = Graph()
    for i in mst:
        mst_graph.add_edge(i[0], i[1], i[2])
    #print(mst)
    cycle = find_hamiltonian_cycle(mst_graph, mst[0])
    sum = 0
    for i in range(len(cycle)-1):
        temp = graph[cycle[i]]
        sum += temp[cycle[i+1]]
    result = "Hamiltonian cycle of weight " + str(sum) + ":"
    print(result)
    res_str = ""
    for i in range(len(cycle)):
        if i == len(cycle)-1:
            res_str += str(cycle[i])
        else:
            res_str += str(cycle[i])
            res_str += ", "
    print(res_str)

if __name__ == "__main__":
    main()
