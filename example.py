from PIL import Image

from image_processing import resize, rotate
from interpolation import nearest_neighbor, bilinear, bicubic

if __name__ == "__main__":
    img = Image.open("i.bmp")
    nn = resize(image=img, scale_factor=2, interpolation=nearest_neighbor)
    nn.save("nn_2.bmp")
    nn03 = resize(image=img, scale_factor=0.3, interpolation=nearest_neighbor)
    nn03.save("nn_0_3.bmp")
    rotated_nn = rotate(image=img, angle=45, interpolation=nearest_neighbor)
    rotated_nn.save("rotated_nn_45.bmp")

    bil = resize(image=img, scale_factor=3, interpolation=bilinear)
    bil.save("bil_3.bmp")
    bil03 = resize(image=img, scale_factor=0.3, interpolation=bilinear)
    bil03.save("bil_0_3.bmp")
    rotated_bil = rotate(image=img, angle=45, interpolation=bilinear)
    rotated_bil.save("rotated_bil_45.bmp")

    bic = resize(image=img, scale_factor=3, interpolation=bicubic)
    bic.save("bic_3.bmp")
    bic03 = resize(image=img, scale_factor=0.3, interpolation=bicubic)
    bic03.save("bic_0_3.bmp")
    rotated_bic = rotate(image=img, angle=45, interpolation=bicubic)
    rotated_bic.save("rotated_bic_45.bmp")
