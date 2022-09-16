from typing import List


class Solution:
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     result_stack = []

    #     def recur_dataset(current_sum, candidates, current_stack, current_index):
    #         if current_sum < 0:
    #             return
    #         elif current_sum == 0:
    #             result_stack.append(current_stack.copy())

    #         for candidate in candidates[current_index:]:
    #             current_stack.append(candidate)
    #             recur_dataset(current_sum - candidate,
    #                           candidates, current_stack)
    #             current_stack.pop()

    #     recur_dataset(target, candidates, [])
    #     return result_stack

    def combinationSumV1(self, candidates: List[int], target: int) -> List[List[int]]:
        result_stack = []

        def recur_dataset(candidates, start_index, current_stack, current_sum):
            if current_sum > target or start_index > len(candidates) - 1:
                return

            if current_sum == target:
                result_stack.append(current_stack.copy())
                return
            current_stack.append(candidates[start_index])
            recur_dataset(candidates, start_index, current_stack,
                          current_sum + candidates[start_index])
            current_stack.pop()
            recur_dataset(candidates, start_index + 1,
                          current_stack, current_sum)
        recur_dataset(candidates, 0, [], 0)
        return result_stack


ob = Solution()
print(ob.combinationSumV1(
    [2, 3, 6, 7],
    7
))
