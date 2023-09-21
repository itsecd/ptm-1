import math
import random


def quick_sort(nums: list) -> list:
    """
    Sorts a list of numbers using the quicksort algorithm.

    Parameters:
    nums (list): The list of numbers to be sorted.

    Returns:
    list: The sorted list of numbers.
    """
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quick_sort(s_nums) + e_nums + quick_sort(m_nums)


def bubble_sort(nums: list) -> None:
    """
    Sorts a list of numbers using the bubble sort algorithm.

    Parameters:
    nums (list): The list of numbers to be sorted.

    Returns:
    None
    """
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


def selection_sort(nums: list) -> None:
    """
    Sorts a list of numbers using the selection sort algorithm.

    Parameters:
    nums (list): The list of numbers to be sorted.

    Returns:
    None
    """
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


def insertion_sort(nums: list) -> None:
    """
    Sorts a list of numbers using the insertion sort algorithm.

    Parameters:
    nums (list): List of numbers to be sorted.

    Returns:
    None
    """
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert


def heapify(nums: list, heap_size: int, root_index: int) -> None:
    """Rearranges the elements in the list in order to maintain the max-heap property.

    Parameters:
        nums: A list of integers representing the heap.
        heap_size: An integer representing the size of the heap.
        root_index: An integer representing the index of the root element.

    Returns:
        None.
    """
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


def heap_sort(nums: list) -> None:
    """Sorts a list of integers using the heap sort algorithm.

    Parameters:
        nums: A list of integers to be sorted.

    Returns:
        None. The list is sorted in-place.
    """
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


def merge(left_list: list, right_list: list) -> list:
    """Merges two sorted lists of integers into a single sorted list.

    Parameters:
        left_list: A sorted list of integers.
        right_list: A sorted list of integers.

    Returns:
        A new list that contains all the elements from both input lists in sorted order.
    """
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums: list) -> list:
    """
    Sorts a list of integers using the merge sort algorithm.

    Parameters:
        nums: a list of integers to be sorted.

    Returns:
        A new list with the elements of nums sorted in ascending order.
    """

    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)


def partition(nums: list, low: int, high: int) -> int:
    """
    This function takes an input list and reorders the elements so that all elements
    Those smaller than the anchor point are moved to the left of it, and all elements
    larger than the anchor point are moved to the right.

    Parameters:
        nums: A list of integers
        low: The lower index of the sub-list to be partitioned
        high: The upper index of the sub-list to be partitioned
    Returns:
        The index of the pivot element after rearranging the elements of the sub-list
    """
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]


def shell_sort(nums: list) -> list:
    """
    Sorts a list of integers using the shell sort algorithm.

    Parameters:
        nums: a list of integers to be sorted.

    Returns:
        A new list with the elements of nums sorted in ascending order.
    """
    n = len(nums)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = nums[i]
            j = i
            while j >= interval and nums[j - interval] > temp:
                nums[j] = nums[j - interval]
                j -= interval
            nums[j] = temp
        k -= 1
        interval = 2 ** k - 1
    return nums
