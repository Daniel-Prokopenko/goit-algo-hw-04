import timeit
import random


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
    # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def Timsort(arr):
    return sorted(arr)


def make_array(l):
    arr = [i for i in range(l)]
    random.shuffle(arr)
    return arr


lengths = [10, 100, 1000, 10000]

for l in lengths:
    arr1 = make_array(l)
    arr2 = arr1.copy()
    arr3 = arr1.copy()
    insertion_time = timeit.timeit(lambda: insertion_sort(arr1), number=100)
    merge_time = timeit.timeit(lambda: merge_sort(arr2), number=100)
    timsort_time = timeit.timeit(lambda: Timsort(arr3), number=100)
    print(
        f"\narray{l}:\n     insertion: {insertion_time};\n     merge: {merge_time};\n     timsort: {timsort_time};\n"
    )
