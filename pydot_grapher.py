import pydot
import sys
import pickle as pkl
filename = sys.argv[1]

graph = pydot.Dot(graph_type = 'graph')

f = open(filename, "r")

# starting person is root node
# need to pass a log file

people = ['President1Trump']

people_bios = pkl.load(open("people1.p", "rb"))
predictions = pkl.load(open("predictions.p", "rb")) 

print people_bios

for line in f:
    toks = line.split()
    if len(toks) > 7 and toks[1] != 'unfollowed':
        if toks[8] in people and toks[8] != toks[2]:
            people.append(toks[2])
            temp = "@"+toks[2]+""
            print temp
            try:
                index = people_bios.index(temp)
                print index
                fill = predictions[index]
                print fill
                print "found"
                if fill == -1:
                    color = "#0000ff"
                elif fill == 1:
                    color = "#ff0000"
                else:
                    color = "#ffffff"

            except Exception as e:
                color = "#ffffff"
            
            node_temp = pydot.Node(toks[2], style="filled", fillcolor=color)
            graph.add_node(node_temp)
            graph.add_edge(pydot.Edge(toks[8], node_temp))

graph.write_png('example.png')