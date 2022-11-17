import math

accounts_no =[]
#selection sort
#1. Set the first element as minimum
#20 12 10 15 2 ---> 20 assume smallest element
#2.Compare minimum with the second element.
# If the second element is smaller than minimum, assign the second element as minimum.
#After each iteration, minimum is placed in the front of the unsorted list.

def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
    return  array

def jump_search(array,n,x):
    step = math.sqrt(n)

    prev = 0
    while array[int(min(step,n)-1)] < x:
        prev = step
        step+=math.sqrt(n)
        if prev>=n:
           return -1

    while array[int(prev)] <x:
        prev+=1
        if prev == min(step,n):
            return -1

    if array[int(prev)] == x:
        return prev
    return -1

if __name__ == "__main__":
    no_of_elements = int(input("Please enter number of element that you want to add: "))
    for i in range(no_of_elements):
        elements = int(input("Enter element: "))
        accounts_no.append(elements)
    print(accounts_no)
    new_nums = selectionSort(accounts_no,no_of_elements)
    print("Sorted order of new arrays: ",new_nums)
    n = len(new_nums)
    find_no = int(input("Please enter a number to find: "))
    result = jump_search(new_nums,n,find_no)
    if result == -1:
        print("Element not found")
    else:
        print("Number", find_no, "is at index", "%.0f" % result)
