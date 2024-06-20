
def merge(items, sections, temporary_storage):
    (start_1, end_1), (start_2, end_2) = sections
    i_1 = start_1
    i_2 = start_2
    i_t = 0
    while i_1 < end_1 and i_2 < end_2:
        if len(items[i_1]) >= len(items[i_2]):
            temporary_storage[i_t] = items[i_1]
            i_1 += 1
        else:
            temporary_storage[i_t] = items[i_2]
            i_2 += 1
        i_t += 1

    while i_1 < end_1:
        temporary_storage[i_t] = items[i_1]
        i_1 += 1
        i_t += 1

    while i_2 < end_2:
        temporary_storage[i_t] = items[i_2]
        i_2 += 1
        i_t += 1

    for i in range(i_t):
        items[start_1 + i] = temporary_storage[i]

def merge_sort(items):
    n = len(items)
    temporary_storage = [None] * n

    step = 1
    while step < n:
        for start in range(0, n, 2 * step):
            start_1 = start
            end_1 = min(start + step, n)
            start_2 = end_1
            end_2 = min(start + 2 * step, n)
            sections = ((start_1, end_1), (start_2, end_2))
            merge(items, sections, temporary_storage)
        step *= 2

list_of_strings = ["abcdefghijklm", "abc", "abcdefghi", "abcdefghijkl", "abcdefg", "abcdefghijklmnopqrstu"]
merge_sort(list_of_strings)
print("Sorted by string length (long to short):", list_of_strings)