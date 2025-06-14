class Solution:
    def increasingarray(self, arr):
        moves = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                moves += arr[i - 1] - arr[i]
                arr[i] = arr[i - 1]
        return moves

s = Solution()

n = int(input())
arr = list(map(int, input().split()))
print(s.increasingarray(arr))
