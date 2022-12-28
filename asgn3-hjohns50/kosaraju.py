import sys
from stack_array import * #Needed for Depth First Search
from directed_graph import *



def main():
    file = open(str(sys.argv[-1]), "r")
    nums = file.read()
    nums = nums.strip("\n")
    nums = nums.replace("\n", " ")
    file.close()
    num_list = nums.split(" ")
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
        #print(num_list[i])
    di_graph = Graph(num_list)
    scc_list = []
    stack = Stack(len(di_graph.graph.keys()))

    for i in di_graph.graph.keys():
        if(di_graph.graph[i].visited == False):
            di_graph.dsf_1(i, stack)
    
    di_graph.transpose(num_list)

    while(stack.is_empty() == False):
        vert = di_graph.graph[stack.pop().id]
        #print(vert.visited)
        if vert.visited is False:
            scc_str = di_graph.dsf_2(vert)
            scc_str = scc_str.rstrip(", ")
            scc_list.append(scc_str)
    print(str(len(scc_list)) + " Strongly Connected Component(s):")
    for i in range(len(scc_list)):
        #if(len(scc_list) - i == 1):
            #scc_list[i] = scc_list[i].rstrip(", ")
        print(scc_list[i])
        """""
        for l in range(len(i)):
            if (len(i) - l) == 1:
                print(i[l])
            else:
                print(str(i[l]) + ", ", end="")
        """
if __name__ == "__main__":
    main()