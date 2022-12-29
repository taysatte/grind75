
class Solution:
    def add_binary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2))) [2:]

a, b = "1010", "1011"
x = Solution().add_binary(a, b)
print(x)