import pytest

from day1 import reorder_list, combine_lists, find_bigger_number, difference_between_ids


def test_reorder_list():
    assert reorder_list([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_combine_lists():
    assert combine_lists([1, 2, 3], [1, 2, 3]) == [(1, 1), (2, 2), (3, 3)]
    ...


def test_find_bigger_number():
    assert find_bigger_number(10, 2) == (10, 2)
    assert find_bigger_number(10, 20) == (20, 10)


def test_difference_between_ids():
    assert difference_between_ids(10, 2) == 8
    assert difference_between_ids(2, 10) == 8
    assert difference_between_ids(20, 10) == 10
    assert difference_between_ids(10, 20) == 10
