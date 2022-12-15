import matplotlib.pyplot as plt
import numpy as np


def find_red_pixels(map_filename='map.png', upper_threshold=100, lower_threshold=50):
    """Your documentation goes here"""
    image = plt.imread(f'data/{map_filename}')
    new_image = np.empty((image.shape[0], image.shape[1], 3), np.float)
    array = np.zeros(shape=(image.shape[0], image.shape[1]))

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if image[x, y, 0] * 255 > upper_threshold and image[x, y, 1] * 255 < lower_threshold and image[x, y, 2] * 255 < lower_threshold:
                new_image[x, y] = [1, 1, 1]
                array[x, y] = 1
            else:
                new_image[x, y] = [0, 0, 0]

    plt.imsave('data/map-red-pixels.jpg', new_image)

    return array


def find_cyan_pixels(map_filename='map.png', upper_threshold=100, lower_threshold=50):
    """Your documentation goes here"""
    image = plt.imread(f'data/{map_filename}')
    new_image = np.empty((image.shape[0], image.shape[1], 3), np.float)
    array = np.zeros(shape=(image.shape[0], image.shape[1]))

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if image[x, y, 0] * 255 < lower_threshold and image[x, y, 1] * 255 > upper_threshold and image[x, y, 2] * 255 > upper_threshold:
                new_image[x, y] = [1, 1, 1]
                array[x, y] = 1
            else:
                new_image[x, y] = [0, 0, 0]

    plt.imsave('data/map-cyan-pixels.jpg', new_image)

    return array


def detect_connected_components(img='data/map-red-pixels.jpg'):
    """Your documentation goes here"""
    image = plt.imread(img)
    f = open("data/cc-output-2a.txt", "w+")
    mark = np.empty((image.shape[0], image.shape[1]), np.int)
    queue = np.empty((0, 2), np.int32)
    outer_count = 1

    for row in range(image.shape[0]):
        for colum in range(image.shape[1]):
            if image[row][colum][0] >= 200 and mark[row, colum] == 0:
                mark[row, colum] = 1
                queue = np.append(queue, [[row, colum]], axis=0)
                pixels = []
                while len(queue) > 0:
                    cu_row = queue[0, 0]
                    cu_colum = queue[0, 1]
                    pixels.append([cu_row, cu_colum])
                    queue = np.delete(queue, 0, axis=0)
                    for var in range(-1, 2):
                        for var1 in range(-1, 2):
                            if -1 < cu_row + var < image.shape[0] and -1 < cu_colum + var1 < image.shape[1]:
                                if image[cu_row + var][cu_colum + var1][0] >= 200 and mark[cu_row + var, cu_colum + var1] == 0:
                                    mark[cu_row + var, cu_colum + var1] = 1
                                    queue = np.append(queue, [[cu_row + var, cu_colum + var1]], axis=0)

                f.write(f'Connected Component {outer_count}, number of pixels = {len(pixels)} \n')
                outer_count += 1

    f.close()
    return mark


def detect_connected_components_sorted(mark):
    """Your documentation goes here"""

    mark1 = np.empty((mark.shape[0], mark.shape[1]), np.int)
    queue = np.empty((0, 2), np.int32)
    connected_components = []

    for row in range(mark.shape[0]):
        for colum in range(mark.shape[1]):
            if mark[row, colum] == 1 and mark1[row, colum] == 0:
                mark1[row, colum] = 1
                queue = np.append(queue, [[row, colum]], axis=0)
                pixels = []
                while len(queue) > 0:
                    cu_row = queue[0, 0]
                    cu_colum = queue[0, 1]
                    pixels.append([cu_row, cu_colum])
                    queue = np.delete(queue, 0, axis=0)
                    for var in range(-1, 2):
                        for var1 in range(-1, 2):
                            if -1 < cu_row + var < mark.shape[0] and -1 < cu_colum + var1 < mark.shape[1]:
                                if mark[cu_row + var, cu_colum + var1] == 1 and mark1[cu_row + var, cu_colum + var1] == 0:
                                    mark1[cu_row + var, cu_colum + var1] = 1
                                    queue = np.append(queue, [[cu_row + var, cu_colum + var1]], axis=0)
                connected_components.append(pixels)

    n = len(connected_components)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if len(connected_components[j]) < len(connected_components[j + 1]):
                connected_components[j], connected_components[j + 1] = connected_components[j + 1], connected_components[j]
                already_sorted = False
        if already_sorted:
            break

    f = open('data/cc-output-2b.txt', "w+")
    for x in range(len(connected_components)):
        f.write(f'Connected Component {x}, number of pixels = {len(connected_components[x])} \n')
    f.close()

    new_image = np.empty((mark.shape[0], mark.shape[1], 3), dtype=np.float)
    array = np.zeros((mark.shape[0], mark.shape[1]))

    for x in connected_components[0]:
        new_image[x[0], x[1]] = [1, 1, 1]
        array[x[0], x[1]] = 1
    for x in connected_components[1]:
        new_image[x[0], x[1]] = [1, 1, 1]

    plt.imsave('data/cc-top-2.jpg', new_image)
    return array
