def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
            arr[i],arr[min_index] = arr[min_index],arr[i]


def input_list():
    arr = []
    n = int(input("Enter the number of elements in the list:"))
    for i in range(n):
        element = int(input("Enter element"))
        arr.append(element)
    return arr


arr = input_list()


print("Original list:",arr)


selection_sort(arr)
print("Sorted list:",arr)
        
