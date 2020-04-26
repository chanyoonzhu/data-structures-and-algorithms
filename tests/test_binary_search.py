from data_structures_and_algorithms import __version__
from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import array_binary_search

def test_version():
    assert __version__ == '0.1.0'

def test_array_binary_search_1():
    arr = [1, 2, 3, 4]
    actual = array_binary_search(arr, 1)
    expected = 0
    assert actual == expected

def test_array_binary_search_2():
    arr = [1, 2, 3, 4]
    actual = array_binary_search(arr, 2)
    expected = 1
    assert actual == expected

def test_array_binary_search_3():
    arr = [1, 2, 3, 4]
    actual = array_binary_search(arr, 3)
    expected = 2
    assert actual == expected

def test_array_binary_search_4():
    arr = [1, 2, 3, 4]
    actual = array_binary_search(arr, 4)
    expected = 3
    assert actual == expected

def test_array_binary_search_5():
    arr = [1, 2, 3, 4, 5]
    actual = array_binary_search(arr, 1)
    expected = 0
    assert actual == expected

def test_array_binary_search_6():
    arr = [1, 2, 3, 4, 5]
    actual = array_binary_search(arr, 2)
    expected = 1
    assert actual == expected

def test_array_binary_search_7():
    arr = [1, 2, 3, 4, 5]
    actual = array_binary_search(arr, 3)
    expected = 2
    assert actual == expected

def test_array_binary_search_8():
    arr = [1, 2, 3, 4, 5]
    actual = array_binary_search(arr, 4)
    expected = 3
    assert actual == expected

def test_array_binary_search_9():
    arr = [1, 2, 3, 4, 5]
    actual = array_binary_search(arr, 5)
    expected = 4
    assert actual == expected

def test_array_binary_search_10():
    arr = [1, 2, 3, 4, 5]
    actual = array_binary_search(arr, 6)
    expected = -1
    assert actual == expected

def test_array_binary_search_11():
    arr = [1, 2, 3, 4, 5]
    actual = array_binary_search(arr, 0)
    expected = -1
    assert actual == expected

def test_array_binary_search_12():
    arr = [1, 2, 3, 4]
    actual = array_binary_search(arr, 5)
    expected = -1
    assert actual == expected

def test_array_binary_search_13():
    arr = [1, 2, 3, 4]
    actual = array_binary_search(arr, 0)
    expected = -1
    assert actual == expected

def test_array_binary_search_14():
    arr = [1, 2, 3, 4]
    actual = array_binary_search(arr, 2.5)
    expected = -1
    assert actual == expected
