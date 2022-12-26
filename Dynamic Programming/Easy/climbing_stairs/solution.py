
class Solution:
    def climb_stairs(self, n: int) -> int:
        num_1, num_2, n_len = 1, 1, n - 1

        for i in range(n_len):
            temp = num_1
            num_1 = num_1 + num_2
            num_2 = temp

        return num_1
