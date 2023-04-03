from PIL import Image


def pixel(input_file, pixel_size):
    image = Image.open(input_file)
    # print(image)
    image = image.resize((image.size[0] // pixel_size, image.size[1] // pixel_size), Image.NEAREST)
    # print(image)
    image = image.resize((image.size[0]*pixel_size, image.size[1]*pixel_size), Image.NEAREST)
    # print(image)
    # print(Image.NEAREST)

    image.show()

pixel("0.jpg", 7)