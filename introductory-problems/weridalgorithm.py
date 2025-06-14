class Solution :
    def weirdalgorithm(self,number):
        while number != 1 :
            print(number, end = " ")
            if number %2 == 0 :
                number //= 2
            elif number % 2 != 0 :
                number = number * 3 + 1
        
        print(1)            
        
s = Solution()
n = int(input())
s.weirdalgorithm(n)