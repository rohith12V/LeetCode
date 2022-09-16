from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Maintain the result set
        result = []
        # Maintain teh visited arary to keep track of the elemnets hwich are visted
        visited = [False]*len(nums)

        def recursive(current_stack, index):
            # one we reach the target size we sadd to the result array
            if len(current_stack) == len(nums):
                result.append(current_stack.copy())
                return
            for index in range(0, len(nums)):
                # if current element is not visited we start the recursion
                if not visited[index]:
                    # A
                    visited[index] = True
                    current_stack.append(nums[index])

                    # Recursion
                    recursive(current_stack, index)

                    # B
                    visited[index] = False
                    current_stack.pop()
        recursive([], 0)
        return result


ob = Solution()
print(ob.permute([
    1, 2, 3
]))

#              []
#       [1]    [2]     [3]
#   [2,3]     [1,3]   [1,2]
# [1]   [2]    [3]  [1]  [2][1]
