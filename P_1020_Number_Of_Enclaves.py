from typing import List


class Solution:
    # recursive DFS Solution
    # costly with space limiations

    # SPACE
    # 1. use visited array - result will be matrix[x][y]==1 and visited[x][y] == False
    # 2. Change 1 -> 2 while performing DFS from oputer coordinates, Result = number of 1's in the array
    def numEnclavesUsingDFS(self, grid: List[List[int]]) -> int:
        row_max = len(grid)
        col_max = len(grid[0])
        # Store all the visited coordinates
        visited = set()

        # DFS Function to traverse all adjacent nodes
        def performDfs(x, y):
            if x < 0 or x >= row_max:
                return
            if y < 0 or y >= col_max:
                return
            if (x, y) in visited:
                return
            if grid[x][y] == 0:
                return
            grid[x][y] = 2
            visited.add((x, y))
            performDfs(x + 1, y)
            performDfs(x - 1, y)
            performDfs(x, y + 1)
            performDfs(x, y - 1)

        # Traverse Boundaries TOP and BOTTOM and perform DFS
        for row_num in [0, row_max - 1]:
            for index in range(0, col_max):
                # if current cell has land then perform DFS to find all land points which are also a part.
                # so that they are not covered with water
                if grid[row_num][index] == 1:
                    performDfs(row_num, index)

        # Traverse Boundaries LEFT and RIGHT and perform BFS
        for col_num in [0, col_max - 1]:
            for index in range(0, row_max):
                # if current cell has land then perform DFS to find all land points which are also a part.
                # so that they are not covered with water
                if grid[index][col_num] == 1:
                    performDfs(index, col_num)

        # Get count of 1's in the matrix (now 1's indicate that none of the outer land has reached this cell.)
        result = self.getLandsCount(grid)
        return result

    def getLandsCount(self, grid):
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    count += 1
        return count

    def numEnclavesUsingBFS(self, grid: List[List[int]]) -> int:
        visited = set()
        que = []
        row_max = len(grid)
        col_max = len(grid[0])

        # Collect all the coordinates which are in the outer layer (TOP / BOTTOM ) and are land
        # add such points to the queue to perform BFS
        for row_num in [0, row_max - 1]:
            for index in range(0, col_max):
                if grid[row_num][index] == 1:
                    que.append((row_num, index))
                    visited.add((row_num, index))

        # Collect all the coordinates which are in the outer layer (LEFT / RIGHT ) and are land
        # add such points to the queue to perform BFS
        for col_num in [0, col_max - 1]:
            for index in range(0, row_max):
                if grid[index][col_num] == 1:
                    que.append((index, col_num))
                    visited.add((index, col_num))

        # Perform BFS
        while len(que) > 0:
            size = len(que)
            # Level wise traversal - not mandatory
            while size > 0:
                (x, y) = que.pop(0)
                # UP
                if x - 1 >= 0 and grid[x - 1][y] == 1 and ((x - 1, y)) not in visited:
                    que.append((x - 1, y))
                    visited.add((x - 1, y))
                # LEFT
                if y - 1 >= 0 and grid[x][y - 1] == 1 and ((x, y - 1)) not in visited:
                    que.append((x, y - 1))
                    visited.add((x, y - 1))
                # DOWN
                if (
                    x + 1 < len(grid)
                    and grid[x + 1][y] == 1
                    and ((x + 1, y)) not in visited
                ):
                    que.append((x + 1, y))
                    visited.add((x + 1, y))
                # RIGHT
                if (
                    y + 1 < len(grid[0])
                    and grid[x][y + 1] == 1
                    and ((x, y + 1)) not in visited
                ):
                    que.append((x, y + 1))
                    visited.add((x, y + 1))
                size -= 1
        # Count all the elements which are 1 (land ) and are not visited before (indicating unreachable from outer border land cells)
        count = 0
        for x in range(0, len(grid)):
            for y in range(0, len(grid[0])):
                if grid[x][y] == 1 and (x, y) not in visited:
                    count += 1
        return count


ob = Solution()
print(ob.numEnclavesUsingBFS([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))
