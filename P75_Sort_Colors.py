from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while(mid <= high):
            element = nums[mid]
            if element == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif element == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        return nums


ob = Solution()
print(ob.sortColors(
    [1, 2, 0]
))
