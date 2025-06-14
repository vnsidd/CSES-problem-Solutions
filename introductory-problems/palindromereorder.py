from collections import Counter

class Solution:
    def can_form_palindrome(self, s: str) -> bool:
        freq = Counter(s)
        odd_count = sum(1 for count in freq.values() if count % 2 != 0)
        return odd_count <= 1

    def construct_palindrome(self, s: str) -> str:
        freq = Counter(s)
        half = []
        middle = ''
        
        for char in sorted(freq): 
            count = freq[char]
            if count % 2 != 0:
                middle = char
            half.extend([char] * (count // 2))

        first_half = ''.join(half)
        return first_half + middle + first_half[::-1]

    def permutationofstring(self, s: str):
        if self.can_form_palindrome(s):
            print(self.construct_palindrome(s))
        else:
            print("NO SOLUTION")


s = Solution()
inp = input()
s.permutationofstring(inp)
