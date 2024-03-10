import networkx as nx
import matplotlib.pyplot as plt

plt.style.use('dark_background')

# Example adjacency list
adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C'],
}

# Create a graph object
G = nx.Graph()

# Add nodes and edges from adjacency list
for node, neighbors in adj_list.items():
    G.add_node(node)
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Add isolated nodes (nodes without any connections)
#isolated_nodes = [node for node in G.nodes() if G.degree(node) == 0]
#for node in isolated_nodes:
#    G.add_edge(node, node)  # Add a self-loop to ensure isolated nodes are included in the layout

# Define the size of the image
fig, ax = plt.subplots(figsize=(10, 10))

# Visualize the graph
pos = nx.spring_layout(G)  # positions for all nodes

# Create a list to specify node colors
node_colors = ['red' if node == 'A' else 'skyblue' for node in G.nodes()]

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1500)

# Manually adjust node positions to the edge of the nodes
node_shift = 0.04
pos_shifted = {node: (x - node_shift, y - node_shift) for node, (x, y) in pos.items()}

# Draw edges with arrows
nx.draw_networkx_edges(G, pos_shifted, arrowstyle='->', arrowsize=25, edge_color='white', width=2, arrows=True)

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

#nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1500, font_size=10, font_weight='bold', edge_color='white', linewidths=1, arrows=True)

plt.title("Graph Visualization")

plt.savefig('graph.png')
plt.show()
