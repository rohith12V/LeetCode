from typing import List
import heapq


class Solution:
    def jump(self, nums: List[int]) -> int:
        # Using Greedy Algorithm to pick the max_reachable and expand
        cost_queue = []

        # Base case
        if len(nums) <= 1:
            return 0

        # As we start with Index 0
        # (max_reachable, current_cost, current_index)
        # we use -ve max_reachable to mimic MAX QUEUE
        heapq.heappush(cost_queue, (-nums[0], 1, 0))
        heapq.heapify(cost_queue)

        while cost_queue:
            (max_reachable, cost, index) = heapq.heappop(cost_queue)
            # Exit Case if we find the last index
            if abs(max_reachable) >= len(nums) - 1:
                return cost
            # Else for current_index -> max_reachable we append to the Q
            for i in range(index + 1, abs(max_reachable) + 1):
                # to avoid index errors while adding to heap Q
                if i > len(nums):
                    break
                heapq.heappush(cost_queue, (
                    -(i + nums[i]),
                    cost+1,
                    i))
        return len(nums) - 1


ob = Solution()
print(ob.jump([2, 3, 1, 1, 4]))
