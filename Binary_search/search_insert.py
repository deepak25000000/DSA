class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        ans = n
        while(low<=high):
            mid = (low+high)//2
            if(nums[mid] >= target):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


s = Solution()
print(s.searchInsert([1,3,5,6], 5))    
print(s.searchInsert([1,3,5,6], 2))     
print(s.searchInsert([1,3,5,6], 7))  
#tc = O(log n)    
#sc = O(1)    







'''
https://leetcode.com/problems/search-insert-position/ 

'''
