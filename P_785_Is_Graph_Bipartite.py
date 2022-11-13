from typing import DefaultDict, List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Create a new graph
        # Preprocessing
        new_graph = DefaultDict(list)
        number_of_edges = len(graph)
        for [node, edges] in enumerate(graph):
            for edge in edges:
                new_graph[node].append(edge)

        # Maintain visited array
        visited = set()
        # maintain Colored Array
        color = [-1 for _ in range(number_of_edges)]

        # Deploy BFS and Check if during expanding nodes
        # we encounter any node whih cis alreayd viisted and colored with the same value as the parent node
        def is_graph_bipartite(index):
            que = [(index, 0)]
            while len(que) > 0:
                # Parent node and its color
                (node, code) = que.pop(0)
                visited.add(node)
                color[node] = code
                for child in new_graph[node]:
                    # Check if child is visited and has same color as parent
                    if child in visited and color[child] == code:
                        # Graph is not bipartite
                        return False
                    # Expand Selection
                    elif child not in visited and color[child] == -1:
                        que.append((child, 1 - code))
            return True

        # For Addressing the issue for Disconnected Graph
        for index in range(number_of_edges):
            if index not in visited and not is_graph_bipartite(index):
                return False
        return True


ob = Solution()
# node 0 ->. 1, 2, 3
# node 1 -> 0, 2 ...
print(ob.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))

