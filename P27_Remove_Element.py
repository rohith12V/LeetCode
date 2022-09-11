from typing import List

# Tc - O(n)
# Sc - O(1)


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = len(nums) - 1
        i = 0
        while(i <= index):
            # if target matches current val then swap with last elemnet
            # do not move to next element util that element is != target
            if(nums[i] == val):
                nums[i], nums[index] = nums[index], nums[i]
                index -= 1
            else:
                # if its not target value move to next elemnet
                i += 1
        return index + 1 if index > 0 else index


ob = Solution()

# case - 1
print(ob.removeElement([1, 2], 2))

# case - 2
print(ob.removeElement([1], 1))

# case - 3
print(ob.removeElement([1, 2], 3))

# case - 4
print(ob.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
