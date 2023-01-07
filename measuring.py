from PIL import Image
import time

from image_processing import resize, rotate
from interpolation import nearest_neighbor, bilinear, bicubic
from utils import calculate_mean_squared_error, get_image_difference


def measure(image_name: str, interpolation):
    """
    Measure mean squared error between original image and resized twice, calculate execution time of
    resizing and rotating with given interpolation method.

    :param image_name: Name of the original image
    :param interpolation: Interpolation function
    """
    original_image = Image.open(image_name)
    execution_start = time.time()
    generated_image = resize(
        image=original_image, scale_factor=0.5, interpolation=interpolation
    )
    resize_execution_time = time.time() - execution_start
    generated_image = resize(
        image=generated_image, scale_factor=2, interpolation=interpolation
    )
    generated_image.save(f"{interpolation.__name__}_resized.bmp")
    mse = calculate_mean_squared_error(generated_image, original_image)
    diff = get_image_difference(generated_image, original_image)
    diff.save(f"{interpolation.__name__}_diff.bmp")

    execution_start = time.time()
    generated_image = rotate(
        image=original_image, angle=60, interpolation=interpolation
    )
    rotate_execution_time = time.time() - execution_start
    generated_image.save(f"{interpolation.__name__}_rotated.bmp")

    print(
        f"{interpolation.__name__}:\nmean squared error: {mse}\nresize execution time: {resize_execution_time}\nrotate execution time: {rotate_execution_time}"
    )
    original_image.close()


if __name__ == "__main__":
    image_name = "original.bmp"
    measure(image_name, bicubic)
    measure(image_name, nearest_neighbor)
    measure(image_name, bilinear)
