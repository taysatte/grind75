
from typing import List
from collections import Counter

class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        counts = Counter(nums).most_common() [0][1]
        return True if counts >= 2 else False