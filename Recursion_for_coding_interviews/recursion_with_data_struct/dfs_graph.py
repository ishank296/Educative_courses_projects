from collections import defaultdict


class Graph:

    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self,e1,e2):
        self.graph[e1].append(e2)


def helper(graph,currentNode,visited):
    if visited[currentNode]:
        return
    print(currentNode)
    visited[currentNode] = True
    for i in graph.graph[currentNode]:
        helper(graph,i,visited)


def dfs(graph):
    visited = [False]*graph.vertices
    helper(graph,0,visited)


if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(0,1)
    g.addEdge(1,2)
    g.addEdge(1,3)
    g.addEdge(2,4)
    g.addEdge(3,4)
    g.addEdge(3,5)

    print("DFS graph traversal")
    dfs(g)