from general import swap


def sift_down(arr, i):
    """Sifts down starting from index i"""
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2

    if left < len(arr) and arr[left] > arr[largest]:
        largest = left

    if right < len(arr) and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)

        sift_down(arr, largest)


def sift_up(arr, i):
    parent = int((i - 1) / 2)
    if arr[parent] < arr[i]:
        swap(arr, parent, i)
        sift_up(arr, parent)


def build_heap_bottom_up(arr):
    """Builds a heap from a mutable array in a bottom-up manner"""
    start = int(len(arr) / 2) - 1

    for i in reversed(range(0, start + 1)):
        sift_down(arr, i)


def insert(heap, elem):
    heap.append(elem)
    sift_up(heap, len(heap) - 1)


def extract(heap):
    swap(heap, 0, len(heap) - 1)
    heap.pop()
    sift_down(heap, 0)


def build_heap_top_down(arr):
    heap = []
    for elem in arr:
        insert(heap, elem)
    for i in range(0, len(heap)):
        arr[i] = heap[i]


if __name__ == "__main__":
    # testing
    arr = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    arr2 = list(arr)
    build_heap_bottom_up(arr)
    build_heap_top_down(arr2)
    print(arr)
    print(arr2)
