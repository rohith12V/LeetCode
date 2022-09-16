from typing import List

# given an array we have to determine if we can reach to the end of the index
# from any index we can jump at max arr[index+1]


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Keep a track of what is the max index we can reach
        max_reachable_index = 0
        for index in range(0, len(nums)):
            # if our index goes beyond max_reachable we can exit our algorithm as there is no option further
            if index > max_reachable_index:
                return False
            # else if we find better max_reachable we can update the same
            elif nums[index] + index > max_reachable_index:
                max_reachable_index = index + nums[index]
        return True


ob = Solution()
print(ob.canJump([0, 3, 1, 1, 4]))
