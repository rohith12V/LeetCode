from textwrap import indent
from typing import List
import copy
import os

import time


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        current_stack = [['_' for _ in range(0, n)] for _ in range(0, n)]
        filled_row = [0 for _ in range(0, n)]
        filled_upperdiagonal = [0 for _ in range(0, 2*n - 1)]
        filled_lowerdiagonal = [0 for _ in range(0, 2*n - 1)]

        def isSafe(col_num, row_num):
            if (filled_row[col_num] == 1):
                return False
            if (filled_lowerdiagonal[n - 1 + (row_num - col_num)] == 1):
                return False
            if (filled_upperdiagonal[col_num + row_num] == 1):
                return False
            return True

        # def printResult(res):
        #     index = 0
        #     for r in result:
        #         print("------Soultion {}-------".format(index))
        #         for x in r:
        #             print(x)
        #         index += 1

        #     for matrix in res:
        #         print(matrix)
        #     time.sleep(0.04)
        #     os.system('cls' if os.name == 'nt' else 'clear')

        def performBacktracking(row_num, n, queens):
            # printResult(current_stack)
            if(row_num > n):
                return
            if (row_num == n):
                if queens == 0:
                    result.append(copy.deepcopy(current_stack))
                return

            for col_num in range(0, n):
                if isSafe(col_num, row_num):
                    current_stack[row_num][col_num] = 'Q'
                    queens -= 1
                    filled_row[col_num] = 1
                    filled_lowerdiagonal[n - 1 + (row_num - col_num)] = 1
                    filled_upperdiagonal[row_num + col_num] = 1
                    performBacktracking(row_num + 1, n, queens)
                    queens += 1
                    filled_lowerdiagonal[n - 1 + (row_num - col_num)] = 0
                    filled_upperdiagonal[row_num + col_num] = 0
                    filled_row[col_num] = 0
                    current_stack[row_num][col_num] = '_'
        performBacktracking(0, n, n)
        return result


ob = Solution()
res = ob.solveNQueens(
    n=9
)
print(len(res))
