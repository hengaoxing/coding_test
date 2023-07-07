from typing import List

def maximumU(arr: List[int]) -> List[int]:
    arr.sort()
    n = len(arr)
    res = [0] * n
    j = 0
    for i in range(2, n, 2):
        res[i] = arr[j]
        j += 1
    res[0] = arr[j]
    j += 1
    for i in range(1, n, 2):
        res[i] = arr[j]
        j += 1
    return res
