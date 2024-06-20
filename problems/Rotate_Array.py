# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]



class Solution:

    #Solution 1
    k=3
    nums=[1,2,3,4,5,6,7]
    nums=nums[-k:] +nums[0:len(nums)-k]
    print(nums)

    # Time complexity of above solution - O (n)
    # Space Complexity - 0(n) , since slicing the array takes k and n-k space , internally creates temp array


    #Solution 2
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        n = len(nums)
        k = k % n  # To handle cases where k > n
    
        # Helper function to reverse a portion of the array
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # Step 1: Reverse the entire array
        reverse(0, n-1)
        
        # Step 2: Reverse the first k elements
        reverse(0, k-1)
    
        # Step 3: Reverse the remaining n-k elements
        reverse(k, n-1)


        #space complexity - O(1)
        #TIME Complexity  - 0 (n)