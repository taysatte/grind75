
from typing import List
from collections import Counter
import math

class Solution:
    def majority_element(self, nums: List[int]) -> int:
        num_dict = dict()
        n = len(nums)
        freq = math.floor(n / 2)

        for i in range(n):
            num_dict[nums[i]] = num_dict.get(nums[i], 0) + 1

        for i in num_dict:
            if num_dict[i] > freq:
                return i

    def majority_element_count(self, nums: List[int]) -> int:
        return Counter(nums).most_common() [0][0]