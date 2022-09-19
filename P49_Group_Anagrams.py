from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        reference = defaultdict(list)
        for element in strs:
            count = [0] * 26
            for char in element:
                count[ord(char) - ord("a")] += 1
            reference[repr(count)].append(element)
        return list(reference.values())


ob = Solution()
print(ob.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
