from re import U
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        # we use hashmap to eleminate duplicate entries or duplicate tree decisons
        element_frequency = {}

        # Calculate Frequency of each elemnt
        for element in nums:
            if element not in element_frequency:
                element_frequency[element] = 0
            element_frequency[element] += 1

        def recursion(current_stack, max_length):
            for key in element_frequency:
                if element_frequency[key] > 0:
                    # Populate
                    current_stack.append(key)
                    element_frequency[key] -= 1

                    # Recursion
                    recursion(current_stack, max_length)

                    # Depopulate
                    element_frequency[key] += 1
                    current_stack.pop()
            # Add to Result
            if len(current_stack) == max_length:
                result.append(current_stack.copy())
        recursion([], len(nums))
        return result


ob = Solution()
print(ob.permuteUnique(
    [1, 1, 2]
))
