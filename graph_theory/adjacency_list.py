class AdjacencyList:
    class Edge:
        def __init__(self, f, t, cost):
            self.from_ = f
            self.to_ = t
            self.cost = cost

    # create adjencency list
    def add(self, graph, from_, to_, cost):
        aa = AdjacencyList.Edge(from_, to_, cost)
        xs = graph.get(from_)
        if xs is None:
            graph[from_] = []
        graph[from_].append(aa)


num_nodes = 5
aa = AdjacencyList()
graph = {}
aa.add(graph, 0, 1, 4)
aa.add(graph, 0, 2, 3)
print(graph[0][0].from_)
"""
graph = {}
graph[0] = [dfs.Edge(0, 1, 4)]
graph[0].append(dfs.Edge(0, 2, 5))
graph[1] = [dfs.Edge(1, 2, -2)]
graph[1].append(dfs.Edge(1, 3, 6))
graph[2] = [dfs.Edge(2, 3, 1)]
graph[2].append(dfs.Edge(2, 2, 10)) # self loop
"""
