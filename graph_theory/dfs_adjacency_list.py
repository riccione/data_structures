"""
Graph Theory: DFS

Inspired by William Fiset
https://github.com/williamfiset/
"""
from adjacency_list import AdjacencyList


class DFSAdjacencyList:

    """
    class Edge:

        def __init__(self, f, t, cost):
            self.from_ = f
            self.to_ = t
            self.cost = cost
    """

    # perform a DFS on a graph with n nodes from a starting point to count the
    # number of nodes in a given component
    def dfs(self, graph, start: int, n: int):
        count = 0
        visited = [False] * n
        # start by visiting the starting node
        stack = [start]

        # start by visiting the starting node
        # stack.append(start)
        # visited[start] = True

        while stack:
            node = stack.pop()
            count += 1
            edges = graph.get(node)

            if edges:
                for edge in edges:
                    if not visited[edge.to_]:
                        stack.append(edge.to_)
                        visited[edge.to_] = True

        return count


num_nodes = 5
aa = AdjacencyList()
dfs = DFSAdjacencyList()
graph = {}
aa.add(graph, 0, 1, 4)
aa.add(graph, 0, 2, 5)
aa.add(graph, 1, 2, -2)
aa.add(graph, 1, 3, 6)
aa.add(graph, 2, 3, 1)
aa.add(graph, 2, 2, 10)  # self loop

node_count = dfs.dfs(graph, 0, num_nodes)
print(f"DFS node count starting at node 0: {node_count}")
if node_count != 4:
    print("Error with DFS")

node_count = dfs.dfs(graph, 4, num_nodes)
print(f"DFS node count starting at node 4: {node_count}")
if node_count != 1:
    print("Error with DFS")
"""
dfs = DFSAdjacencyList()
graph = {}
graph[0] = [dfs.Edge(0, 1, 4)]
graph[0].append(dfs.Edge(0, 2, 5))
graph[1] = [dfs.Edge(1, 2, -2)]
graph[1].append(dfs.Edge(1, 3, 6))
graph[2] = [dfs.Edge(2, 3, 1)]
graph[2].append(dfs.Edge(2, 2, 10)) # self loop

node_count = dfs.dfs(graph, 0, num_nodes)
print(f"DFS node count starting at node 0: {node_count}")
if node_count != 4:
    print("Error with DFS")

node_count = dfs.dfs(graph, 4, num_nodes)
print(f"DFS node count starting at node 4: {node_count}")
if node_count != 1:
    print("Error with DFS")
"""
