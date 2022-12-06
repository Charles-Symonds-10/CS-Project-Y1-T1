import matplotlib.pyplot as plt
import numpy as np


def find_red_pixels(*args, **kwargs):
    """Your documentation goes here"""
    image = plt.imread('data/map.png')
    new_image = []

    for x in image:
        temp = []
        for y in x:
            if y[0] * 255 > 100 and y[1] * 255 < 50 and y[2] * 255 < 50:
                temp.append([255, 255, 255])
            else:
                temp.append([0, 0, 0])
        new_image.append(temp)

    map_of_red_pixels = np.array(new_image)
    plt.imshow(map_of_red_pixels)
    plt.savefig('data/map_of_red_pixels.jpeg')

    return map_of_red_pixels


def find_cyan_pixels(*args, **kwargs):
    """Your documentation goes here"""
    image = plt.imread('data/map.png')
    new_image = []

    for x in image:
        temp = []
        for y in x:
            if y[0] * 255 < 50 and y[1] * 255 > 100 and y[2] * 255 > 100:
                temp.append([255, 255, 255])
            else:
                temp.append([0, 0, 0])
        new_image.append(temp)

    map_of_cyan_pixels = np.array(new_image)
    plt.imshow(map_of_cyan_pixels)
    plt.savefig('data/map_of_cyan_pixels.jpeg')

    return map_of_cyan_pixels


def detect_connected_components(*args, **kwargs):
    """Your documentation goes here"""
    # Your code goes here


def detect_connected_components_sorted(*args, **kwargs):
    """Your documentation goes here"""
    # Your code goes here

