class Solution:
    def upperbound(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        ub = -1
        while low<= high:
            mid = (high+low)//2
            if nums[mid]==target:
                ub = mid
                low = mid + 1
            else:
                high = mid - 1             
        return ub
    
    def lowerbound(self, nums, target):
        n  = len(nums)
        high = n -1
        low = 0
        lb = -1
        while low<=high:
            mid = (high+low)//2
            if nums[mid]==target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb

nums = [5,6,7,8,8,8,10]
target = 8
sol = Solution()
lower_ans = sol.lowerbound(nums, target)
upper_ans = sol.upperbound(nums, target)
print("Lower bound:", lower_ans)
print("Upper bound:", upper_ans)
