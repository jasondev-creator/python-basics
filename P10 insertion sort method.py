def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key


def input_list():
    arr = []
    n = int(input("Enter the number of elements in the list:"))
    for i in range(n):
        element = int(input("Enter element:"))
        arr.append(element)
    return arr


arr = input_list()
print("Original list:",arr)


insertion_sort(arr)
print("Sorted list using insertion sort method:",arr)
    
