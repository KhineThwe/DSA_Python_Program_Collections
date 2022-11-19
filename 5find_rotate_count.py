# Function to find the total number of times the list is rotated
#pivot property ---> both the next and previous element of the pivot element are greater than it.
# the array is circularly sorted,
# If the pivot is the last element, then the first element will be considered its next element.
# If the pivot is the first element, then the last element will be considered its previous element.
#using binarySearch

def findRotationCount(nums,n):
    low = 0
    high = n-1
    while low<=high:
        #condition1: if list is already sorted
        #found the minimum element at low index
        if nums[low] <= nums[high]:
            return low
        mid = (low+high)//2

        next = (mid+1) % n
        prev = (mid - 1+n) % n

        if nums[mid] <= nums[next] and nums[mid] <=nums[prev]:
            return mid
        elif nums[mid] <= nums[high]:#search in left half
            high = mid - 1
        elif nums[mid] >= nums[low]:
            low = mid + 1
    return -1


if __name__ == "__main__":
    # nums = [1, 2, 3, 4, 5, 6, 7,8, 9, 10]
    # nums = [1] #for testing line 14
    # nums = [8,9,10,1,2,3,4,5,6,7]
    nums = [10, 1,2,3]
    # nums = [9, 2, 5]#for line 16
    n = len(nums)
    count = findRotationCount(nums,n)
    if count == 0:
        print(f'The list is already sorted')
    else:
        print(f'The list is rotated {count} times')
