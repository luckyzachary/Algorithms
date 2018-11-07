from textbook.sort import *
def test_quick_sort():
    arr = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert quick_sort.quick_sort(arr, 0, 9) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]