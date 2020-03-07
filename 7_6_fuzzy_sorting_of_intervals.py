from random import randint


def find_intersection(left_list, right_list, start, end):
    pivot_left = left_list[end]
    pivot_right = right_list[end]
    for i in range(start, end):
        if pivot_left <= right_list[i] and pivot_right >= left_list[i]:
            if right_list[i] < pivot_right:
                pivot_right = right_list[i]
            if left_list[i] > pivot_left:
                pivot_left = left_list[i]
    return pivot_left, pivot_right


def partition(left_list, right_list, start, end, pivot_left, pivot_right):
    equal_start = start - 1
    for i in range(start, end):
        if right_list[i] < pivot_left:
            equal_start += 1
            left_list[equal_start], left_list[i] = left_list[i], left_list[equal_start]
            right_list[equal_start], right_list[i] = right_list[i], right_list[equal_start]
    equal_start += 1
    equal_end = equal_start - 1
    for i in range(equal_start, end + 1):
        if pivot_left <= right_list[i] and pivot_right >= left_list[i]:
            equal_end += 1
            left_list[equal_end], left_list[i] = left_list[i], left_list[equal_end]
            right_list[equal_end], right_list[i] = right_list[i], right_list[equal_end]
    return equal_start, equal_end


# left_list: is list of left endpoint of intervals
# right_list is list of right endpoint of intervals
def fuzzy_quick_sort(left_list, right_list, start, end):
    if start < end:
        pivot_idx = randint(start, end)
        left_list[pivot_idx], left_list[end] = left_list[end], left_list[pivot_idx]
        right_list[pivot_idx], right_list[end] = right_list[end], right_list[pivot_idx]
        pivot_left, pivot_right = find_intersection(left_list, right_list, start, end)
        equal_start, equal_end = partition(left_list, right_list, start, end, pivot_left, pivot_right)
        fuzzy_quick_sort(left_list, right_list, start, equal_start - 1)
        fuzzy_quick_sort(left_list, right_list, equal_start + 1, end)


def main():
    left_list = [13, 6, 9, 15, 3, 11, 13, 12, 14, 9, 5, 7, 1, 1, 6]
    right_list = [14, 7, 11, 15, 7, 15, 14, 14, 15, 15, 7, 9, 5, 9, 10]
    fuzzy_quick_sort(left_list, right_list, 0, len(left_list) - 1)
    for left, right in zip(left_list, right_list):
        print(left, "-", right, end=", ")
    print()
    for left, right in zip(reversed(left_list), reversed(right_list)):
        for i in range(left):
            print(" ", end="")
        for i in range(left, right + 1):
            print("_", end="")
        print()


if __name__ == "__main__":
    main()
