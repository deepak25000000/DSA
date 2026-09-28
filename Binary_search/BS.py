class Solution:
    def bs(nums, target) -> int:
        n = len(nums)
        low = 0
        high = n -1
        while low <= high:
            mid = (low+high)//2
            if(nums[mid] == target):
                return mid
            elif(nums[mid] < target):
                low = mid + 1
            else:
                high = mid - 1
        return -1 


nums = [2]
target = 2
print(Solution.bs(nums, target))    

nums = [1,2,3,4,5,6,7,8,9,10]
target = 5
print(Solution.bs(nums, target))    

nums = [1,2,3,4,5,6,7,8,9,10]
target = 0
print(Solution.bs(nums, target))    

nums = [1,2,3,4,5,6,7,8,9,10]
target = 11
print(Solution.bs(nums, target))    

nums = []
target = 5
print(Solution.bs(nums, target))    

#TC = O(log n)
#SC = O(1)
'''
https://leetcode.com/problems/binary-search/ 
'''