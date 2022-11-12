from collections import defaultdict


class Graph:
    def __init__(self, number_of_vertices) -> None:
        self.edges = defaultdict(list)
        self.count = number_of_vertices

    def addEdge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def detectCycleUsingBFS(self):
        n_nodes = self.count
        visited = set()

        def checkCycleFromNode(node):
            que = [(node, -1)]
            # Traverse from the current node using BFS to all connected nodes.
            while len(que) > 0:
                size = len(que)
                print("-----LEVEL WISE TRAVERSAL----------")
                while size > 0:
                    (node, parent) = que.pop(0)
                    print(node)
                    visited.add(node)
                    for child in self.edges[node]:
                        if child not in visited:
                            que.append((child, node))
                        if child in visited and child != parent:
                            return True
                    size -= 1
            return False

        # For Disconnected Graph
        for node in range(n_nodes):
            if node not in visited:
                if checkCycleFromNode(node):
                    return True
        return False

    def detectCycleUsingDFS(self):
        n_nodes = self.count
        # To Hold all the visited nodes to trace the cycle.
        visited = set()

        def checkCycleFromNode(node):
            que = [(node, -1)]
            # Traverse from the current node using BFS to all connected nodes.
            while len(que) > 0:
                (node, parent) = que.pop()
                # Mark the node as visited
                visited.add(node)
                for child in self.edges[node]:
                    # Populate the DFS Tree
                    if child not in visited:
                        que.append((child, node))
                    # For Undirected Graph - child != parent
                    # Potential Cycle Found at this location
                    if child in visited and child != parent:
                        return True
            return False

        # For Disconnected Graph, Traverse every sub not visited node
        for node in range(n_nodes):
            if node not in visited:
                if checkCycleFromNode(node):
                    return True
        return False


ob = Graph(5)
ob.addEdge(0, 1)
ob.addEdge(0, 2)
ob.addEdge(1, 4)
ob.addEdge(2, 3)
ob.addEdge(2, 5)
ob.addEdge(4, 6)
ob.addEdge(5, 6)
print(ob.detectCycleUsingBFS())
print(ob.detectCycleUsingDFS())
