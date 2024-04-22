"""
Question

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

"""


"""

Solution


Strategy:
The most efficient way to solve this problem is to use a two-pointer technique:

Pointer Setup:
One pointer (write_index) is used to keep track of where the next element that is not equal to val should be written.
Another pointer (read_index) is used to examine each element of the array.
Iterate through the Array:
Start both pointers at the beginning of the array.
Move read_index through the array from start to finish.
When nums[read_index] is not equal to val, copy nums[read_index] to nums[write_index] and increment write_index.
In-place Modification:
By doing this, you are overwriting the elements equal to val in nums with those that are not, effectively removing them.
Return the New Length:
After the loop ends, write_index will be at the position where the next non-val element would be written, which is essentially the count of non-val elements in nums. This is the value you return.

Complexity:
Time Complexity: O(n), where n is the number of elements in nums, since each element is checked exactly once.
Space Complexity: O(1), because the modification is done in-place without using extra space.
This solution is efficient, uses minimal space, and adheres to the problem's constraints by modifying the array in-place.









"""


def remove_element(nums, val):

    write_index=0


    for read_index in range(len(nums)):
        if nums[read_index] != val:
            nums[write_index]=nums[read_index]
            write_index = write_index + 1

    return write_index