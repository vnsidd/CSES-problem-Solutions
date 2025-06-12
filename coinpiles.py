class Solution:
    def coinpiles(self, tests):
        results = []
        for a, b in tests:
            if (a + b) % 3 == 0 and min(a, b) * 2 >= max(a, b):
                results.append("YES")
            else:
                results.append("NO")
        return results



t = int(input())
tests = [tuple(map(int, input().split())) for _ in range(t)]
sol = Solution()
for res in sol.coinpiles(tests):
    print(res)
