# 선형 탐색
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# 이진 탐색
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = ( high + low ) // 2

        # if x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # if x is smaller, ignore right hal
        elif arr[mid] > x:
            high = mid - 1

        # x is present at mid
        else:
            return mid
    # if we reach here, then element was not present
    return -1