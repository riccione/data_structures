"""
Graph Theory: BFS

Inspired by William Fiset
https://github.com/williamfiset/
"""
from adjacency_list import AdjacencyList


class BFSAdjacencyList:
    def __init__(self, graph, n: int):
        if graph is None:
            raise ValueError("Graph cannot be None")

        self.n = n  # size of the graph
        self.graph = graph
        self.prev = [None] * self.n

    # perform a BFS on a graph from starting node 'start'
    def bfs(self, start: int):
        visited = [False] * self.n
        queue = []

        # start by visiting the start node and add it to the queue
        queue.append(start)
        visited[start] = True

        # continue until BFS is done
        while queue:
            node = queue.pop(0)

            # loop through all edges attached to this node. Mark nodes as
            # visited once they're in the queue.
            for edge in self.graph.get(node):
                if not visited[edge.to_]:
                    visited[edge.to_] = True
                    self.prev[edge.to_] = node
                    queue.append(edge.to_)

    def reconstruct_path(self, start: int, end: int):
        self.bfs(start)
        path = []
        at = end
        while at is not None:
            path.append(at)
            at = self.prev[at]
        path = path[::-1]
        if path[0] == start:
            return path
        return []

    def format_path(self, path):
        path_str = [str(x) for x in path]
        return "->".join(path_str)


num_nodes = 13
aa = AdjacencyList("undirected")
# unweighted undirected graph
aa.add(0, 7)
aa.add(0, 9)
aa.add(0, 11)
aa.add(7, 11)
aa.add(7, 6)
aa.add(7, 3)
aa.add(6, 5)
aa.add(3, 4)
aa.add(2, 3)
aa.add(2, 12)
aa.add(12, 8)
aa.add(8, 1)
aa.add(1, 10)
aa.add(10, 9)
aa.add(9, 8)
bfs = BFSAdjacencyList(aa, num_nodes)

start = 10
end = 5
path = bfs.reconstruct_path(start, end)
print(f"Actual: {bfs.format_path(path)}")
print(f"Expected: 10->9->0->7->6->5")
