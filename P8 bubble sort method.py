def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def input_list():
    arr = []
    n = int(input("Enter the number of elements in the list:"))
    for i in range(n):
        element = int(input("Enter element"))
        arr.append(element)
    return arr


arr = input_list()
print("Original list:",arr)


bubble_sort(arr)
print("Sorted list:",arr)
                
            
