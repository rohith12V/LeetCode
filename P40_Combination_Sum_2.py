from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result_stack = []
        # Sorting to eliminate duplicates
        # eg - [1,1,7] [7,1,1] are both same
        candidates.sort()

        def recur_dataset(candidates, start_index, current_stack, current_sum):
            # Base Case
            if current_sum == target:
                result_stack.append(current_stack.copy())
                return
            # Base Case
            if current_sum > target or start_index > len(candidates) - 1:
                return

            # Track current candidate using Stack
            current_stack.append(candidates[start_index])

            # Recursion
            recur_dataset(candidates, start_index + 1, current_stack,
                          current_sum + candidates[start_index])
            # Remove top Element
            current_stack.pop()

            #  Make Sure next element is not the previous element
            while (start_index + 1 < len(candidates) and candidates[start_index] == candidates[start_index+1]):
                start_index += 1

            # Recursion
            recur_dataset(candidates, start_index + 1,
                          current_stack, current_sum)
        recur_dataset(candidates, 0, [], 0)
        return result_stack

# [10,1,2,7,6,1,5] => [1,1,2,5,6,7,10]

#                                                0 ( index = -1 )
#                    (0 + 1) {index = 0 -> n}                            (0) {index = 0  -> n}
#   (1 + 1) {index = 1 -> n}        (1) {index = 1  -> n}       (0 + 1) {index = 1 -> n}        (0) {index = 1  -> n}
#


ob = Solution()
print(ob.combinationSum2(
    [10, 1, 2, 7, 6, 1, 5],
    8
))
