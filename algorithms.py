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


def compare_sorting_performance():
    data = [random.randint(1, 10_000) for _ in range(1_000)]

    bubble_time = timeit.timeit(
        lambda: bubble_sort(data), number=10
    )

    builtin_time = timeit.timeit(
        lambda: sorted(data), number=10
    )

    return {
        "bubble_sort": bubble_time,
        "builtin_sort": builtin_time
    }

def compare_search_performance():
    data = list(range(10_000))
    target = 9_999

    linear_time = timeit.timeit(
        lambda: linear_search(data, target), number=1_000
    )

    builtin_time = timeit.timeit(
        lambda: target in data, number=1_000
    )

    return {
        "linear_search": linear_time,
        "builtin_search": builtin_time
    }
