from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        result = []
        # graph = [[1,2],[2,3],[5],[0],[5],[],[]] (index -> edges)
        # to skip elements while checking dfs on all nodes
        visited = [0 for _ in range(len(graph))]
        # indicates which elements are in current stack.
        path_visited = [0 for _ in range(len(graph))]

        def explore_state(index):
            # set visited and path visited
            visited[index] = 1
            path_visited[index] = 1

            isSafeState = True
            for child in graph[index]:
                if visited[child] == 0:
                    isSafeState &= explore_state(child)
                elif path_visited[child] == 1:
                    return False
            # if its safe state then there should be no cycle, we backtrack out path
            if isSafeState:
                path_visited[index] = 0
            return isSafeState

        for node in range(len(graph)):
            # if state is not explored explore the state
            if visited[node] == 0:
                explore_state(node)

            # if node is visited and it is not a part of group which leads to cycle.
            if visited[node] == 1 and path_visited[node] == 0:
                result.append(node)

        return result


graph = [[1], [2], [3], [4, 5], [6], [6], [7], [], [1, 9], [10], [8], [9]]

ob = Solution()
print(ob.eventualSafeNodes(graph))
