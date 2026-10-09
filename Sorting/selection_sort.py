class Solution():
    def selection_sort(self, nums):
        n = len(nums)
        for i in range(0, n):
            mini_index = i
            for j in range (i+1, n):
                if nums[j] < nums[mini_index]:
                    mini_index = j
            nums[i], nums[mini_index] = nums[mini_index], nums[i]
        return nums

solution = Solution()
nums = [4,2,6,3,7,1,9,8]
print(solution.selection_sort(nums))

'''
TC = O(N^2)
SC = O(1)
Used when we have to sort large array, use less memory
https://www.geeksforgeeks.org/problems/selection-sort/1
'''

        