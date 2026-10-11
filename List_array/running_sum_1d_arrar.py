class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(1, n):
            nums[i] = nums[i] + nums[i - 1]
        return nums

solution = Solution()
nums = [1,4,5,6,7,8]
print(solution.runningSum(nums))

#TC = O(N)
#SC = O(1)