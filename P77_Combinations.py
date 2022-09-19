from typing import List


class Solution:
    def combine(self, upper_bound: int, target_size: int) -> List[List[int]]:
        result = []
        self.generateCombinations(result, [], upper_bound, 1, target_size)
        return result

    def generateCombinations(self, result, current_stack, upper_bound, lower_bound, target_size):
        if len(current_stack) == target_size:
            result.append(current_stack.copy())
            return
        for index in range(lower_bound, upper_bound + 1):
            current_stack.append(index)
            self.generateCombinations(
                result, current_stack, upper_bound, index+1, target_size)
            current_stack.pop()


ob = Solution()
print(ob.combine(
    4, 2
))
