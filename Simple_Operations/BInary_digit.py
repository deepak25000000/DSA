class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        result = 0
        count1 = 0
        
       
        #conversion from integer to binary
        while a > 0 and b > 0:
            remainder = a % 2
            if remainder == 1:
                count1 += 1
            a = a//2


        count2 = 0
        while b > 0:
            remainder = b%2
            if remainder == 1:
                count2 += 1
            b = b//2

        if count1 >= count2:
            result = count1 * count2
            
        else:
            result = count2 // count1
        return result

s = Solution()
a = 22
b = 7
print(s.calculateScore(a,b))

'''
https://leetcode.com/problems/calculate-score/description/
TC = O(logN + logM)
SC = O(1)
'''



        
        
        
        
                
                
            
            
        