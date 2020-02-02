def counting_sort(arr, exp = 1, base  = 10):
    n = len(arr)

    # The array to be used for the sorted one.
    out = [0] * n

    # Count array
    count = [0] * base

    # quick lambda for indexing:
    index = lambda x: int(x / exp % 10)

    # Count number of appearances of the desired digit:
    for i in range(0, n):
        j = index(arr[i])
        count[j] += 1

    # Update them to have the starting position of each number:
    for i in range(1, base):
        count[i] += count[i-1]

    # now build the sorted array
    for i in reversed(range(0, n)):
        j = index(arr[i])
        out[count[j] - 1] = arr[i]
        count[j] -= 1

    # copy sorted array to original array:
    for i in range(0, n):
        arr[i] = out[i]


if __name__ == "__main__":
    arr = [45643, 1568, 9234, 6743, 8786, 4757]
    print("Before:", arr)
    counting_sort(arr, 1)
    print("After:", arr)
