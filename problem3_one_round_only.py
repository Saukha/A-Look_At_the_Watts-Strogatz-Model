
# coding: utf-8

# In[3]:


import networkx as nx
import matplotlib.pyplot as plt
import numpy as ny
import random as random
from operator import itemgetter

# There is a built-in function in Networkx! == > non_neighbors(graph, node) Return type: iterator    
# randomly find unconnected nodes for node x in Graph g
def random_non_neighbors(g,x):
    non_neighbor_list = [int(node) for node in nx.non_neighbors(H, str(x))]
    print('non-neighbors of node', x, 'are: ', non_neighbor_list)
    # randomly find a new unconnected node for v1 to add an edge
    y = random.choice(non_neighbor_list)
    return y

# randomly pick a node from edge (u,v) in graph h to rewire to a random non-neighbor
def random_rewire_edge(h,u1,v1):
    picked_node = random.choice((u1,v1))  # randomly pick a node from (edge (u,v) to connect to a non-neighbor 
    if picked_node == u1: 
        v2=random_non_neighbors(h,u1)
        h.add_edge(str(u1), str(v2))    # add new edge      
        print('rewired edge: ', u1, v2)            
    else:  # picked_node == v1
        u2=random_non_neighbors(h,v1)
        h.add_edge(str(u2), str(v1))    # add new edge
        print('rewired edge: ', u2, v1)
    H.remove_edge(str(u1), str(v1)) # remove the selected edge      
    print('removed edge: ', u1, v1)

    
# plot all charts
def present_results(g, num_rewired_edge_list, ave_cluster_list, ave_path_length_list):
    # print number of edges rewired before break out of loop or when all are rewired
    print('    ')
    print('total number of edges rewired = ', i+1) 
    # plot Number of Rewired Edges against Average Clustering Coefficient
    plt.plot(num_rewired_edge_list, ave_cluster_list)
    plt.title('Number of Rewired Edges Vs Average Clustering Coefficient')
    plt.xlabel('Number of Rewired Edges')
    plt.ylabel('Average Clustering Coefficient')
    plt.show()
    plt.close()
    # plot Number of Rewired Edges against Average Shortest Path Length
    plt.plot(num_rewired_edge_list, ave_path_length_list)
    plt.title('Number of Rewired Edges Vs Average Shortest Path Length')
    plt.xlabel('Number of Rewired Edges')
    plt.ylabel('Average Shortest Path Length')
    plt.show()
    plt.close()
    # draw final graph when all edges rewired before break out of loop or when all are rewired
    print('total number of rewired edges = ', len(num_rewired_edge_list)-1)
    print(nx.info(g))
    nx.draw_circular(g, with_labels=True)
    plt.show()
    plt.close()

    
###########################

# main program
# read graph data
H=nx.read_graphml("problem3.graphml")

print ('Original Graph')
print (nx.info(H))
nx.draw_circular(H,with_labels=True) # draw original graph
plt.show()
plt.close()

# create a list of edges from the <class 'networkx.classes.reportviews.EdgeDataView'>
# EdgeDataView does not support indexing
edge_list = [edge for edge in H.edges(H)]  # convert EdgeDataView to a list  using list comprehension
print ('original edge list =', edge_list[0:10])  # preview beginning of edge_list
random.shuffle(edge_list) # randomly shuffle edge_list to rewire one at a time in random order
print('shuffled edge list = ', edge_list[0:10]) # preview of beginning of shuffled edge_list

# create lists to store graph metrics; first metric in the lists are before rewiring edges
ave_clustering_coeff=[nx.average_clustering(H)]
ave_shortest_path_length=[nx.average_shortest_path_length(H)]
number_of_rewired_edge=[0]

# rewire one edge at a time according to the order in the shuffled list of edges
for i in range (0,len(edge_list)):
    # go through the shuffled edges list one edge at a time
    print('   ')
    print('edge number', i+1)
    print(edge_list[i])
    u=edge_list[i][0]
    v=edge_list[i][1]
    print ('degree of node ', u, ' = ', H.degree(str(u)),' / ', 'degree of node', v, ' = ', H.degree(str(v)))
    print ('number of edges before rewiring = ', len(H.edges))
    
    # randomly rewire the selected edge
    random_rewire_edge(H,u,v)

    # append graph metrics to appropriate list
    ave_clustering_coeff.append(nx.average_clustering(H))
    ave_shortest_path_length.append(nx.average_shortest_path_length(H))
    number_of_rewired_edge.append(i+1)
    if i==1:
        print (i+1, 'edges are rewired as shown below:')
        nx.draw_circular(H,with_labels=True)
        plt.show()
        plt.close()
    if i==4:
        print (i+1, 'edge(s) are rewired as shown below:')
        nx.draw_circular(H,with_labels=True)
        plt.show()
        plt.close()
    if i==9:
        print (i+1, 'edge(s) are rewired as shown below:')
        nx.draw_circular(H,with_labels=True)
        plt.show()
        plt.close()

# plot all charts
present_results(H, number_of_rewired_edge, ave_clustering_coeff, ave_shortest_path_length)

