from counting_sort import counting_sort_by_ith_digit
from math import log
from math import floor


def radix_sort(arr, base=10):
    """Sorts a mutable array of integers in a given base.
    :param arr: The array
    :param base: The base of the numbers in the array. Defaults to decimal.
    """
    # get the highest exponent's order for sorting
    m_num = max(arr)
    n = floor(log(m_num, base))

    # use stable sort according to every digit from LSD to MSD
    for i in range(0, n+1):
        counting_sort_by_ith_digit(arr, base ** i, base)


if __name__ == "__main__":
    arr = [45643, 1568, 9234, 6743, 8786, 4757]
    print("Before:", arr)
    radix_sort(arr)
    print("After:", arr)
