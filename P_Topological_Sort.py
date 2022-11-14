class Solution:
    # Depth First Search DFS
    # for all u -> , in topo sort u should appear before v
    def topological_sort_using_dfs(self, graph):
        # Store the TOPO Order
        order = []
        # Store visisted vertices
        visited = set()
        # Perform DFS
        def dfs(index):
            # add node to visited
            visited.add(index)
            # expand node's children
            for child in graph[index]:
                if child not in visited:
                    dfs(child)
            # add POST recursion to add the final state (last executed node)
            # last executed node is the node with dependencies of others.
            order.append(index)

        for index in range(len(graph)):
            if index not in visited:
                dfs(index)
        return order

    # Khan's Algorithm BFS
    def topological_sort_using_bfs(self, graph):
        # calculate the indegree of each node
        in_degree = [0 for _ in range(len(graph))]
        # from u -> v indegree of v = 1
        for index in range(len(graph)):
            for child in graph[index]:
                in_degree[child] += 1
        que = []
        # add all nodes whose indegree == 0
        que.extend([index for index in range(len(graph)) if in_degree[index] == 0])
        # place to store indegree
        result = []
        # BFS
        while len(que) > 0:
            node = que.pop(0)
            result.append(node)
            # expand children
            for child in graph[node]:
                in_degree[child] -= 1
                # if we encounter indegree == 0 add it to the queue
                if in_degree[child] == 0:
                    que.append(child)

        return result


graph = [[1], [2], [3], [4], [5, 6], [], []]
ob = Solution()
print(ob.topological_sort_using_dfs(graph))
print(ob.topological_sort_using_bfs(graph))
graph = [[], [], [3], [1], [0, 1], [0, 2]]
print(ob.topological_sort_using_dfs(graph))
print(ob.topological_sort_using_bfs(graph))

