import pytest
import intelligence as intel
import numpy as np
import matplotlib.pyplot as plt


def test_find_red_pixels():
    '''doc'''

    image = plt.imread('data/map.png')
    assert type(intel.find_red_pixels()) == np.ndarray

    assert intel.find_red_pixels().shape[0] == image.shape[0]
    assert intel.find_red_pixels().shape[1] == image.shape[1]


def test_find_cyan_pixels():
    '''doc'''

    image = plt.imread('data/map.png')
    assert type(intel.find_cyan_pixels()) == np.ndarray

    assert intel.find_cyan_pixels().shape[0] == image.shape[0]
    assert intel.find_cyan_pixels().shape[1] == image.shape[1]


def test_detect_connected_components():
    '''doc'''

    image = plt.imread('data/map.png')
    assert type(intel.detect_connected_components()) == np.ndarray

    assert intel.detect_connected_components().shape[0] == image.shape[0]
    assert intel.detect_connected_components().shape[1] == image.shape[1]


def test_detect_connected_components_sorted():
    '''doc'''

    mark = intel.detect_connected_components()

    image = plt.imread('data/map.png')
    assert type(intel.detect_connected_components_sorted(mark)) == np.ndarray

    assert intel.detect_connected_components_sorted(mark).shape[0] == image.shape[0]
    assert intel.detect_connected_components_sorted(mark).shape[1] == image.shape[1]

