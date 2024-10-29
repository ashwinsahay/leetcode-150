"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""


"""
Problem Understanding
You start at the first index of an array, and each number in the array tells you the maximum number of steps you can jump forward from that position. The goal is to check if you can reach the last index of the array.

Solution Idea
The idea is to keep track of how far we can jump as we move through the array. We don’t need to actually "jump"; we just keep updating the farthest point we could potentially reach.

Step-by-Step Solution
Start with the First Index:
Set a variable max_reach to 0. This variable will keep track of the farthest position we can reach in the array as we go through each index.
Loop Through the Array:
For each index i:
Check if we’re Stuck: If i is greater than max_reach, it means we've reached a point where we can’t go forward. In this case, return false.
Update max_reach: Update max_reach to the maximum of its current value or the sum of the current index and the value at that index (i + nums[i]). This tells us the farthest position we can reach from the current index.
After the Loop:
If we finished the loop without returning false, it means we were able to reach or go beyond the last index, so we return true.
Example Walkthrough
Example 1: nums = [2,3,1,1,4]

Start at index 0 with max_reach = 0.
At index 0, nums[0] = 2, so max_reach becomes 0 + 2 = 2.
Move to index 1, nums[1] = 3, so max_reach becomes max(2, 1 + 3) = 4.
Now, max_reach is 4, which is the last index, so we return true.
Example 2: nums = [3,2,1,0,4]

Start at index 0 with max_reach = 0.
At index 0, nums[0] = 3, so max_reach becomes 0 + 3 = 3.
Move to index 1, nums[1] = 2, so max_reach stays 3 (since 1 + 2 is not more than 3).
Move to index 2, nums[2] = 1, max_reach stays 3.
Move to index 3, nums[3] = 0, max_reach is still 3.
We can’t reach index 4 because max_reach is stuck at 3, so we return false.

"""


def can_jump(nums):
    max_reach = 0
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
    return True
