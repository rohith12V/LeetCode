from typing import List


class Solution:
    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        row_max = len(grid)
        col_max = len(grid[0])
        # To Track all visisted elements
        visited = set()
        # To Store all island shapes
        islands = set()
        # to store current DFS traversal Land Points
        island = []

        # x, y are starting coordinates
        # a, b are the base points

        def explore(x, y, a, b):
            if x < 0 or x >= row_max:
                return
            if y < 0 or y >= col_max:
                return
            if (x, y) in visited:
                return
            if grid[x][y] == 0:
                return
            visited.add((x, y))
            # reduce by base coordinates to match will other similar cell
            island.append([x - a, y - b])
            # DFS - UP DOWN LEFT RIGHT
            explore(x + 1, y, a, b)
            explore(x - 1, y, a, b)
            explore(x, y + 1, a, b)
            explore(x, y - 1, a, b)

        for row_index in range(row_max):
            for col_index in range(col_max):
                if (
                    grid[row_index][col_index] == 1
                    and (row_index, col_index) not in visited
                ):
                    island.clear()
                    explore(row_index, col_index, row_index, col_index)
                    islands.add(repr(island))
        return len(islands)


ob = Solution()
print(
    ob.countDistinctIslands(
        [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 1, 1], [1, 1, 0, 0, 0]]
    )
)
