
# coding: utf-8

# In[61]:


import networkx as nx
import matplotlib.pyplot as plt
import numpy as ny
import random as random
from operator import itemgetter

# randomly pick a node from the chosen edge to rewire
def rewire_edge(h,u,v):
    # choose a node
    picked_node = random.choice((u,v))    
    if picked_node == u: 
        neighbor_list=[int(node) for node in h.neighbors(str(u))]
        print ('neigbors =', neighbor_list)
        u=str(random.choice([node for node in all_nodes if node not in neigbor_list]))
    else:
        neighbor_list=[int(node) for node in h.neighbors(str(v))]
        print ('neigbors =', neighbor_list)
        v=str(random.choice([node for node in all_nodes if node not in neighbor_list]))
    print('rewired edge: ', u, v)
    h.add_edge(u, v)  

# actually there is a built-in function in Networkx! == > non_neighbors(graph, node) Return type: iterator    
# find unconnected nodes
def random_unconnected_node(g,x):
    neighbor_list=[int(node) for node in g.neighbors(str(x))]
    print ('neigbors of ', x, '=', neighbor_list)
    print('unconnected nodes =', [node for node in all_nodes if node not in neighbor_list])
    # randomly find a new unconnected node for v1 to add an edge
    y=random.choice([node for node in all_nodes if node not in neighbor_list])     
    return y
    
# plot all charts
def present_results(g, num_rewired_edge_list, ave_cluster_list, ave_path_length_list):
    # print number of edges rewired before break out of loop or when all are rewired
    print('number of edges rewired = ', i+1) 
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
    print('Number of Rewired Edges = ', len(num_rewired_edge_list)-1)
    print(nx.info(g))
    nx.draw_circular(g, with_labels=True)
    plt.show()
    plt.close()

# main program
# convert graphml data into gml data
G=nx.read_graphml("problem3.graphml")
nodes = list(G.nodes)
edges = list(G.edges)
print('type of nodes', type(nodes))
print('type of edges', type(edges))
print(len(nodes))
print(len(edges))
print(nodes)
print(edges)
N=nx.Graph()
N.add_nodes_from(nodes)
N.add_edges_from(edges)
nx.draw_circular(N,with_labels=True)
nx.write_gml(N,'problem3.gml')

# read graph data
H=nx.read_gml("problem3.gml")

print ('Original Graph')
print (nx.info(H))
nx.draw_circular(H,with_labels=True) # draw original graph
plt.show()
plt.close()

# create a list of all nodes
all_nodes=[]
for i in range(1,301):
    all_nodes.append(i)

# create a list of edges from the <class 'networkx.classes.reportviews.EdgeDataView'>
# EdgeDataView does not support indexing
edge_list =[] # emplty list
for edge in H.edges(H):  
    edge_list.append(edge)
print ('original edge list =', edge_list[0:10])
random.shuffle(edge_list) # randomly shuffle edge_list to rewire one at a time in random order
print('shuffled edge list = ', edge_list[0:10])    

# create lists to store graph metrics; first metric in the lists are before rewiring edges
ave_clustering_coeff=[nx.average_clustering(H)]
ave_shortest_path_length=[nx.average_shortest_path_length(H)]
number_of_rewired_edge=[0]

# rewire one edge at a time according to the order in the shuffled list of edges
for i in range (0,300):
    # go through the shuffled edges list one edge at a time
    print('edge ', i+1)
    print(edge_list[i])
    u1=edge_list[i][0]
    v1=edge_list[i][1]
    u1_degree=H.degree(str(u1))
    v1_degree=H.degree(str(v1))
    print ('degree of u1 node ', u1, ' = ', u1_degree,' / ', 'degree of v1 node', v1, ' = ', v1_degree)
    print ('number of edges before rewiring = ', len(H.edges))
    
    # pick a node with less degree from the edge and find a unconnected node to add an edge
    # if both nodes have the same degree, pick the target node
    if u1_degree < v1_degree:
        # do not remove edge from u1
        # must connect u1 to non-neighbors
        # randomly find a new unconnected node v2 for u1 to add an edge
        # v2=random_unconnected_node(H,u1)
        non_neighbor_list = [int(node)for node in nx.non_neighbors(H, str(u1))]
        v2 = random.choice(non_neighbor_list)
        H.add_edge(str(u1),str(v2))
        print ('added edge', u1, v2)
    else:
        # do not remove edge from v1
        # must connect v2 to non-neighbors
        # randomly find a new unconnected node u2 for v1 to add an edge
        # u2=random_unconnected_node(H,v1)
        non_neighbor_list = [int(node)for node in nx.non_neighbors(H, str(v1))]
        u2 = random.choice(non_neighbor_list)
        H.add_edge(str(u2),str(v1))
        print ('added edge', u2, v1)
    print ('number of edges after added one = ',len(H.edges))
    print ('number of nodes after added one edge = ', len(H.nodes))
    H.remove_edge(str(u1), str(v1)) # remove the selected edge
    print ('removed edge: ', u1, v1)
    print ('number of edges after rewiring = ',len(H.edges))
    print ('number of edges after rewiring =',len(H.nodes))
    if not nx.is_connected(H):
        print ('Graph is NOT connected!  Graph is NOT connected!   Graph is NOT connected!')
        break
    
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

