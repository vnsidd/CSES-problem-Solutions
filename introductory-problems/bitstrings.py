class Solution :
    def calculatebitstrings(self,n) :
        bits = 2 ** n % (10 ** 9 + 7)
        return bits
    
s = Solution()
n = int(input())
print(s.calculatebitstrings(n))