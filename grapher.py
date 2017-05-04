import networkx as nx
from networkx.drawing.nx_pydot import write_dot
import matplotlib.pyplot as plt
import sys

filename = sys.argv[1]
outfilename = sys.argv[2]

G = nx.DiGraph()
f = open(filename, "r")

for line in f:
	toks = line.split()
	G.add_edge(toks[8], toks[2])

write_dot(G, outfilename)

# pos = nx.shell_layout(G)
# nx.draw_networkx_nodes(G, pos)
# nx.draw_networkx_edges(G, pos)
# nx.draw_networkx_labels(G, pos)
# plt.show()

