def linear_search(arr,target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1
def input_list():
    arr = []
    n = int (input("Enter the number of elements in the list:"))
    for i in range(n):
        element = int(input("Enter element"))
        arr.append(element)
    return arr


arr = input_list()
target = int(input("Enter the element to search for:"))


result = linear_search(arr,target)
if result != -1:
    print(target,"Element found at index",result)
else:
    print(target,"Element not found in the list.")
