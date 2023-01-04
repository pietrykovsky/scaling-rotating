import numpy as np


def nearest_neighbor(pixel_array: np.array, x: int, y: int) -> int:
    """
    Interpolate pixel value with nearest neighbor algorithm.

    :param pixel_array: pixel matrix
    :param x: row index of the pixel
    :param y: column index of the pixel
    :return: pixel value
    """
    rows, cols = pixel_array.shape[:2]
    # Make sure the input coordinates are within the bounds of the array
    if x < 0 or x > rows - 1 or y < 0 or y > cols - 1:
        return 0
    # Find the coordinates of the nearest neighbor
    x_, y_ = int(np.round(x)), int(np.round(y))
    return pixel_array[x_, y_]


def bilinear(pixel_array: np.array, x: int, y: int) -> int:
    """
    Interpolate pixel value with bilinear algorithm.

    :param pixel_array: pixel matrix
    :param x: row index of the pixel
    :param y: column index of the pixel
    :return: pixel value
    """
    rows, cols = pixel_array.shape[:2]
    # Make sure the input coordinates are within the bounds of the array
    if x < 0 or x > rows - 1 or y < 0 or y > cols - 1:
        return 0
    # Get the coordinates of the nearest pixels
    x0, y0 = x, y
    x1, y1 = x + 1, y + 1
    # Check the boundaries
    if x1 > rows - 1:
        x1 = x0
    if y1 > cols - 1:
        y1 = y0
    # Calculate the weights
    wx, wy = x - x0, y - y0
    wx1, wy1 = 1 - wx, 1 - wy
    pixel_value = (
        wx1 * wy1 * pixel_array[x0, y0]
        + wx * wy1 * pixel_array[x1, y0]
        + wx1 * wy * pixel_array[x0, y1]
        + wx * wy * pixel_array[x1, y1]
    )
    return pixel_value


def bicubic(pixel_array: np.array, x: int, y: int) -> int:
    """
    Interpolate pixel value with bicubic algorithm.

    :param pixel_array: pixel matrix
    :param x: row index of the pixel
    :param y: column index of the pixel
    :return: pixel value
    """
    rows, cols = pixel_array.shape[:2]
    # Make sure the input indices are within the bounds of the array
    if x < 0 or x > rows - 1 or y < 0 or y > cols - 1:
        return 0
    # Get the coordinates of the nearest pixels
    x0, y0 = x, y
    x1, y1 = x + 1, y + 1
    x2, y2 = x + 2, y + 2
    x3, y3 = x + 3, y + 3
    # Check if the coordinates are out of bounds
    if x1 > rows - 1:
        x1 = x0
    if x2 > rows - 1:
        x2 = x0
    if x3 > rows - 1:
        x3 = x0
    if y1 > cols - 1:
        y1 = y0
    if y2 > cols - 1:
        y2 = y0
    if y3 > cols - 1:
        y3 = y0
    # Calculate the weights for the pixels
    wx, wy = x - x0, y - y0
    wx1, wy1 = (wx**2) * (3 - 2 * wx), (wy**2) * (3 - 2 * wy)
    wx2, wy2 = (wx**3) - (wx**2) + 1, (wy**3) - (wy**2) + 1
    wx3, wy3 = -(wx**3) + 2 * (wx**2) + wx, -(wy**3) + 2 * (wy**2) + wy
    # Interpolate the value of the original pixel
    pixel_value = (
        wx1 * wy1 * pixel_array[x0, y0]
        + wx2 * wy1 * pixel_array[x1, y0]
        + wx3 * wy1 * pixel_array[x2, y0]
        + wx1 * wy2 * pixel_array[x0, y1]
        + wx2 * wy2 * pixel_array[x1, y1]
        + wx3 * wy2 * pixel_array[x2, y1]
        + wx1 * wy3 * pixel_array[x0, y2]
        + wx2 * wy3 * pixel_array[x1, y2]
        + wx3 * wy3 * pixel_array[x2, y2]
    )
    return pixel_value
