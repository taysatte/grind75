
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n

        while left < right:
            mid = int(left + (right - left) / 2)
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        return right