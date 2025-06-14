class Solution:
    def repetitions(self, s: str) -> int:
        max_count = 1
        count = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1

        return max_count

s = Solution()
string = input()
print(s.repetitions(string))
