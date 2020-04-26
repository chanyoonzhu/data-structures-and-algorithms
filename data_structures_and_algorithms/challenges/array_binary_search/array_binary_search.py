def array_binary_search(sortedArr, key):
    if len(sortedArr) == 0:
        return -1
    left, right = 0, len(sortedArr) - 1
    while left <= right:
        mid = (left + right) // 2
        if key == sortedArr[mid]:
            return mid
        elif key > sortedArr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1