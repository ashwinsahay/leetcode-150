def remove_element(nums, val):

    write_index=0


    for read_index in range(len(nums)):
        if nums[read_index] != val:
            nums[write_index]=nums[read_index]
            write_index = write_index + 1

    return write_index