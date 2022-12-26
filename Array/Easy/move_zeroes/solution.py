
from typing import List

class Solution:
    def move_zeroes(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            [nums]
        for i in range(0, len(nums)):
            if nums[i] == 0 and i != len(nums):
                nums.remove(0)
                nums.append(0)
        