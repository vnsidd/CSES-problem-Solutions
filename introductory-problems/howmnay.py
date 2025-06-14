from itertools import permutations
class Solution :
    def generatepermutations(self,inp) :
        
        s = inp.strip()
        allperms = set(permutations(s))
        perm_strings = sorted("".join(s) for s in allperms)
        return perm_strings
c = Solution()
result = c.generatepermutations("absb")
for i in range (len(result)) :
    print(result[i])
        