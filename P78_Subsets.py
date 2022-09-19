from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        result.append([])

        def generateCombinations(current_stack, start_index):
            for index in range(start_index, len(nums)):
                element = nums[index]
                current_stack.append(element)
                result.append(current_stack.copy())
                generateCombinations(current_stack, index+1)
                current_stack.pop()
        generateCombinations([], 0)
        return result


ob = Solution()
print(ob.subsets(
    [1, 2, 3]
))
