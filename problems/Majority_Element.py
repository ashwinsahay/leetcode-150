# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        #Solution 

        # if len(nums)==1:
        #     return nums[0]

        # d1={}
        # for e in nums:
        #     if e not in d1:
        #         d1[e]=0
        #     d1[e]+=1

        # ans=-1
        # for k in d1:
        #     if d1[k]>len(nums)/2:
        #         ans=k
        
        # return ans

        #Above solution time complexity 0(n) and Space Complexity O(n)

        # below sol. is O(1) space
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
            
        return res

        #Above solution time complexity 0(n) and Space Complexity O(1)

        #Explanation - 

        #Two variables are initialized: res (to hold the potential majority element) and count (to keep track of the count of the current candidate).
        #The algorithm iterates through each element n in the array nums.
        # if after incrementing and decrementing the count for one element when the count comes to zero, it means there's no current candidate, so we set res to the current element n.
        #Eventually element with count >0 in the end is majority element and returned

        