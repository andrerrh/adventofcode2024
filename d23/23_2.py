import re
import networkx as nx

input = open("./input.txt").read().strip().splitlines()

G = nx.Graph()
for row in input:
    (p1, p2) = re.findall(r"(\w+)", row)

    G.add_edge(p1, p2)

cliques = list(nx.find_cliques(G))
maxC = max(cliques, key=len)

print(",".join(sorted(maxC)))

