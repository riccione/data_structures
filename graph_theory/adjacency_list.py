"""
AdjacencyList class
"""


class AdjacencyList:
    class Edge:
        def __init__(self, f, t, cost=1):
            self.from_ = f
            self.to_ = t
            self.cost = cost

    def __init__(self, typos):
        self.typos = typos
        self.graph = {}

    # default value for cost is 1 == unweighted graph
    def add(self, a, b, cost=1):
        if self.typos == "undirected":
            self._add(a, b, cost)
            self._add(b, a, cost)
        else:  # directed
            self._add(a, b, cost)

    # create adjencency list
    def _add(self, a, b, cost):
        aa = self.Edge(a, b, cost)
        xs = self.graph.get(a)
        if xs is None:
            self.graph[a] = []
        self.graph[a].append(aa)

    def get(self, node):
        return self.graph.get(node)

    def __repr__(self):
        st = ""
        for k, v in self.graph.items():
            edges = []
            for x in v:
                edges.append(f"{x.from_}=>{x.to_}, cost={x.cost}")
            st += "\n".join(edges)
        return st

    def __str__(self):
        return self.__repr__()


num_nodes = 5
aa = AdjacencyList("directed")
aa.add(0, 1, 4)
aa.add(0, 2, 3)
print(aa)
"""
graph = {}
graph[0] = [dfs.Edge(0, 1, 4)]
graph[0].append(dfs.Edge(0, 2, 5))
graph[1] = [dfs.Edge(1, 2, -2)]
graph[1].append(dfs.Edge(1, 3, 6))
graph[2] = [dfs.Edge(2, 3, 1)]
graph[2].append(dfs.Edge(2, 2, 10)) # self loop
"""
