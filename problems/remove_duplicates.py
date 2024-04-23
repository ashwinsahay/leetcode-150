'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.

'''



''''
Solution

Here's a step-by-step approach to solving this:

Use two pointers: one to iterate through the array (i) and another (j) to keep track of the position in the array where the next unique element should be placed.
Start both pointers at the first element.
Increment the i pointer to go through each element of the array.
If the element at the i pointer is different from the element at the j pointer (indicating a new unique element), increment j, and copy the value from i to j.
Continue this process until you have gone through the entire array.
Return the value of j + 1 (since j is an index).

Complexity:
Time Complexity: O(n), where n is the number of elements in nums, since each element is checked exactly once.
Space Complexity: O(1), because the modification is done in-place without using extra space.
This solution is efficient, uses minimal space, and adheres to the problem's constraints by modifying the array in-place.


'''


from typing import List  # Necessary for using List in type hints

def remove_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    
    j = 0  # Pointer j keeps track of the last unique element's position
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]  # Copy the unique element to index j
    
    return j + 1  # Since j is an index, and we need count of unique elements

# Test case
nums = [1, 1, 2]
k = remove_duplicates(nums)
print("Number of unique elements:", k)  # Expected: 2
print("Modified array:", nums[:k])      # Expected: [1, 2]