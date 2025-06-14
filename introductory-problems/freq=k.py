class Solution :
    def frequencyequalsK(self,arr,k) :
        freq = {}
        for i in range(len(arr)) :
            freq[arr[i]] = freq.get(arr[i],0) + 1
        for key,  value in freq.items() :
            if value == k :
                return key
            
        return None
                
                
s = Solution()
print(s.frequencyequalsK([1,2,3,3,3] ,3))