import math
import numpy as np
from PIL import Image


def resize(image: Image, scale_factor: float, interpolation) -> Image:
    """
    Resize an image with given scale factor value using given interpolation function as an argument.

    :param image: Image to resize
    :param scale_factor: Scale factor
    :param interpolation: Interpolation function
    :return: Resized image
    """
    pixel_matrix = np.array(image)
    shape = np.array(pixel_matrix.shape)
    new_height, new_width = shape[:2] * scale_factor
    new_height, new_width = int(new_height), int(new_width)
    resized_image = np.zeros(shape=(new_height, new_width, shape[2]), dtype="uint8")
    for i in range(new_height):
        for j in range(new_width):
            resized_image[i, j] = interpolation(
                pixel_array=pixel_matrix,
                x=int(i / scale_factor),
                y=int(j / scale_factor),
            )
    return Image.fromarray(resized_image)


def rotate(image: Image, angle: float, interpolation) -> Image:
    """
    Rotate an image with given angle value using given interpolation function as an argument.
    Size of the retotated image remains the same as the original.

    :param image: Image to resize
    :param angle: Angle value to rotate
    :return: Rotated image
    """
    pixel_matrix = np.array(image)
    rows, cols, channels = pixel_matrix.shape
    x_center, y_center = rows // 2, cols // 2
    rotated_image = np.zeros(shape=(rows, cols, channels), dtype="uint8")
    radians = math.radians(angle)
    for i in range(rows):
        for j in range(cols):
            # Calculate the rotation matrix
            x = (i - x_center) * math.cos(radians) + (j - y_center) * math.sin(radians)
            y = -(i - x_center) * math.sin(radians) + (j - y_center) * math.cos(radians)
            # Add the center offset
            x = int(round(x) + x_center - 1)
            y = int(round(y) + y_center - 1)
            rotated_image[i, j] = interpolation(
                pixel_array=pixel_matrix,
                x=x,
                y=y,
            )
    return Image.fromarray(rotated_image)
