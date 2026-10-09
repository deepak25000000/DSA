class Solution():
    def bubble_sort(self, nums):
        n = len(nums)
        for i in range(n-2, -1, -1):
            for j in range(0, i+1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1]= nums[j+1], nums[j]
        return nums

solution = Solution()
nums = [3,5,2,8,1]
print(solution.bubble_sort(nums))
'''
Bubble sort swaps the adjcaent element with the current element if the element is greater than 
the next element
TC = O(N^2)
SC = O(1)
https://www.geeksforgeeks.org/problems/bubble-sort/1
'''