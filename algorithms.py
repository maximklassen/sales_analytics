import timeit
import random

def bubble_sort(arr):
    data = arr.copy()
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data

def builtin_sort(arr):
    return sorted(arr)

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

def builtin_search(arr, target):
    return target in arr
