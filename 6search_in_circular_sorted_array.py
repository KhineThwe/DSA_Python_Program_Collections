# Function to find an element in a circularly sorted list
def searchCircularList(nums, target,n):
    low = 0
    high = n -1

    while low <= high:

        mid = (low + high) // 2

        if target == nums[mid]:
            return mid

        # if right half nums[mid…right] is sorted and `mid` is not
        # the key element
        if nums[mid] <= nums[high]:
            # compare key with nums[mid] and nums[right] to know
            # if it lies in nums[mid…right] or not
            if nums[mid] < target <= nums[high]:
                low = mid + 1  # go searching in the right sorted half
            else:
                high = mid - 1  # go searching left

        # if left half nums[left…mid] is sorted, and `mid` is not
        # the key element
        else:
            # compare key with nums[left] and nums[mid] to know
            # if it lies in nums[left…mid] or not
            if nums[low] <= target < nums[high]:
                high = mid - 1  # go searching in the left sorted half
            else:
                low = mid + 1  # go searching right

    # key not found or invalid input
    return -1


if __name__ == '__main__':

    nums = [9, 10, 2, 5, 6, 8]
    key = 5
    n = len(nums)
    index = searchCircularList(nums, key,n)
    if index != -1:
        print('Element found at index', index)
    else:
        print('Element found not in the list')
