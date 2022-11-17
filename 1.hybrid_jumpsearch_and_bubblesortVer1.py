import math

accounts_no =[]
def bubbleSort(array):
    for i in range(len(array)):# 0 7
        for j in range(0,len(array)-i-1):#j= 0 to 6(0,....5)
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

def jump_search(array,n,x):
    step = math.sqrt(n)#4.0

    prev = 0
    while array[int(min(step,n)-1)] < x:#3
        prev = step #8
        step+=math.sqrt(n)#12
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
    new_nums = bubbleSort(accounts_no)
    print("Sorted order of new arrays: ",new_nums)
    n = len(new_nums)
    find_no = int(input("Please enter a number to find: "))
    result = jump_search(new_nums,n,find_no)
    if result == -1:
        print("Element not found")
    else:
        print("Number", find_no, "is at index", "%.0f" % result)
