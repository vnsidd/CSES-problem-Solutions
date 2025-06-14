import sys

class Solution:
    def missingnumber(self, n, arr):
        xor1 = 0
        xor2 = 0

        for num in arr:
            xor1 ^= num

        for i in range(1, n + 1):
            xor2 ^= i

        return xor1 ^ xor2

data = sys.stdin.read().split()
n = int(data[0])
arr = list(map(int, data[1:]))

s = Solution()
print(s.missingnumber(n, arr))
