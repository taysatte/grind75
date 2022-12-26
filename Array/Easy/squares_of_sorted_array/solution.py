
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = []
        for i in range(len(nums)):
            sqr = int(nums[i] * nums[i])
            new_nums.append(sqr)
        return sorted(new_nums)