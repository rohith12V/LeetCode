from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # BaseCase
        # [1], []
        if (len(nums) <= 1):
            return

        # Find the index ( which negates increasing sequence)
        # To Find out which part of the nums array is in last possible state
        # eg : [1, 4, 5, 3, 2] where [5, 3, 2] is in last possible state ( strictly decreasing )
        # [index 2 -> 4] is decreasing so capture index = 1 ( 4 ) which can be replaced for next sequence
        index = len(nums) - 2
        while(index >= 0 and (nums[index] > nums[index + 1])):
            index -= 1

        # Base Case
        # Swap only if we have valid i , j
        if index >= 0:
            j_index = len(nums) - 1
            # Find the next index from last whoch is just greater than the element at index [1]
            while(nums[j_index] <= nums[index]):
                j_index -= 1
            # Swap
            nums[index], nums[j_index] = nums[j_index], nums[index]

        self.reverse(nums, j_index + 1, len(nums) - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def get_number_of_permutations(self, n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res


ob = Solution()

nums = [5, 1, 1]

possible_number_of_perms = ob.get_number_of_permutations(len(nums))

for i in range(0, possible_number_of_perms + 1):
    ob.nextPermutation(nums)
    print(nums)

print("Total Possible Permutations for length ",
      len(nums), "are", possible_number_of_perms)
