from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits) - 1
        while (carry > 0 and n >= 0):
            k = digits[n] + carry
            if k < 10:
                digits[n] = k
            else:
                digits[n] = k % 10
            carry = k//10
            n -= 1
        return digits if carry == 0 else [carry] + digits


ob = Solution()
print(ob.plusOne([1, 9]))
print(ob.plusOne([2, 9]))
print(ob.plusOne([9, 1]))
print(ob.plusOne([9, 2]))
print(ob.plusOne([1, 9, 9]))
print(ob.plusOne([9, 9, 9, 9]))
print(ob.plusOne([9]))
