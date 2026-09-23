class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        maxi = float("-inf")
        for i in range(0, n):
            total = total + nums[i]
            maxi = max(maxi, total)
            if(total < 0):
                total = 0
        return maxi
#Tc = O(n)
#SC = O(1)
#Leetcode 53 Maximu sub array

nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
print(sol.maxSubArray(nums))