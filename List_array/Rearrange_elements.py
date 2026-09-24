class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        posIndex = 0
        negIndex = 1
        for i in range(0, n):
            if(nums[i] >= 0):
                result[posIndex] = nums[i]
                posIndex += 2
            else:
                result[negIndex] = nums[i]
                negIndex += 2
        return result

sol = Solution()
print(sol.rearrangeArray([3,1,-2,-5,2,-4]))

# https://leetcode.com/problems/rearrange-array-elements-by-sign/
#Example 1
# Input: nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]
#Tc = O(n)
#SC = O(n)