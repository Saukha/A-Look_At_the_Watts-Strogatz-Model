# A Look At the Watts-Strogatz Model

Random networks, in which nodes are connected randomly, are small worlds but not clustered. Watts-Strogatz (WS) proposed a network model that is both clustered and a small world, like real networks to some extent. They started off with the idea that people know their neighbors, so they connect each node with their n nearest neighbors. </p>

This produces a clustered network, but it is a large world. They randomly rewired some of the links. WS discovered that rewiring only a few links is enough to decrease the average distance between nodes, i.e. make it a small world, while not affecting the clustering considerably. <br />

Investigate this claim by WS. Start with nearest neighbor network (provided) of 100 nodes, where each node connects to its 6 nearest neighbors (similar to Fig. 1).  <br />

Figure 1.  Each node connects with nearest neighbors. This produces a clustered but large-world network.  <br />
<img src="   " />

Figure 2. Network with rewired links (red). This is a clustered, small world network. (Note, red links in image were added not rewired.  <br />
<img src="   " />


a) Calculate the average clustering coefficient and average path length of this network C(ave) and D(ave). <br />
b) Choose one link randomly and rewire one end to a different, randomly chosen, node. <br />
c) Calculate Cave and dave again.  <br /> 
d) Repeat steps b and c until all links have been rewired.  <br />
e) Perform this simulation a sufficient number of times* to obtain representative averages of C(ave) and D(ave) for each number of rewired edges. <br />
f) Plot these averages as a function of the number of rewired edges. Argue the claim made by WS. <br />

## Watts-Strogatz algorithm
Watts-Strogatz algorithm is a graph generator.  It creates a Watts-Strogatz small-world graph with your inputs.  <br />
Here is the syntax: <br />
watts_strogatz_graph(n, k, p, seed=None)  <br />
Parameters :  <br />
n : int (The number of nodes)  <br />
k : int (Each node is connected to k nearest neighbors in ring topology)  <br />
p : float (The probability of rewiring each edge)  <br />
seed : int, optional (Seed for random number generator (default=None))  <br />











