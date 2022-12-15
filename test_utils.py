import pytest
import utils as ut


def test_sum_values():
    ''' documentation '''

    assert ut.sumvalues([3, 5, 2, 6]) == 16

    assert type(ut.sumvalues([3, 2, 3])) == int

    with pytest.raises(TypeError):
        ut.sumvalues(['string', int, int])


def test_max_value():
    '''Doc'''

    assert ut.maxvalue([3, 5, 2, 6]) == 6

    assert type(ut.maxvalue([3, 2, 3])) == int

    with pytest.raises(TypeError):
        ut.maxvalue(['string', int, int])


def test_min_value():
    '''Doc'''

    assert ut.minvalue([3, 5, 2, 6]) == 2

    assert type(ut.minvalue([3, 2, 3])) == int

    with pytest.raises(TypeError):
        ut.minvalue(['string', int, int])


def test_mean():
    '''Doc'''

    assert ut.minvalue([3, 5, 2, 6]) == 4

    assert type(ut.minvalue([3, 2, 3])) == int

    with pytest.raises(TypeError):
        ut.minvalue(['string', int, int])


def test_count_value():
    '''Doc'''

    assert ut.countvalue([3, 5, 2, 6], 2) == 1
    assert ut.countvalue([3, 5, 2, 6], 'i') == 0

    assert type(ut.countvalue([3, 2, 3], 3)) == int

