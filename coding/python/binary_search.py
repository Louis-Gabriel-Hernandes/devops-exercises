#!/usr/bin/env python

import random
from typing import List, Optional

def binary_search(arr: List[int], target: int) -> Optional[int]:
    """
    Perform binary search on a sorted list.
    
    :param arr: List of sorted integers
    :param target: The integer to search for
    :return: The index of the target if found, else None
    """
    lb, ub = 0, len(arr) - 1
    
    while lb <= ub:
        mid = lb + (ub - lb) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lb = mid + 1
        else:
            ub = mid - 1
    
    return None

if __name__ == '__main__':
    rand_num_li: List[int] = sorted([random.randint(1, 50) for _ in range(10)])
    target: int = random.randint(1, 50)
    result = binary_search(rand_num_li, target)
    print("List: {}\nTarget: {}\nIndex: {}".format(
        rand_num_li, target, result if result is not None else "Not found"))
