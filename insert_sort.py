from general import swap


def insertion_sort(arr):
    """Sorts a mutable array using the insertion sort algorithm.
    :param arr: The array
    """
    # Make a new array to hold the elements as they are added.
    out = []

    # add every element to the end
    for j in range(0, len(arr)):
        out.append(arr[j])
        i = len(out) - 1
        # Bubble it down to its location in the sorted array
        while i > 0:
            prev = out[i - 1]
            curr = arr[j]
            if prev > curr:
                swap(out, i - 1, i)
                i -= 1
            else:
                break

    # Copy to original array
    for i in range(0, len(out)):
        arr[i] = out[i]


if __name__ == "__main__":
    arr = [25, 11, 18, 4, 6, 8, 19, 30]
    print("Before: {0}".format(arr))
    insertion_sort(arr)
    print("After: {0}".format(arr))
