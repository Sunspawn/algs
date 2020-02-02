from math import floor
from insert_sort import insertion_sort


def bucket_sort(arr, k):
    """Sorts a mutable array with bucket sort algorithm.
    :param arr: The array
    :param k: The number of buckets to use
    """
    # generate empty buckets
    buckets = []
    for i in range(0, k + 1):
        buckets.append([])

    # find maximum value in array
    m_num = max(arr)

    # place elements into buckets according to index = floor(element / m_num * k)
    for elem in arr:
        n_index = floor(k * elem / m_num)
        buckets[n_index].append(elem)

    # sort each bucket
    for bucket in buckets:
        insertion_sort(bucket)

    # concatenate buckets and copy into original array
    out = []
    for bucket in buckets:
        out.extend(bucket)
    for i in range(0, len(out)):
        arr[i] = out[i]


if __name__ == "__main__":
    arr = [25, 11, 18, 4, 6, 8, 19, 30]
    print("Before: {0}".format(arr))
    bucket_sort(arr, 3)
    print("After: {0}".format(arr))
