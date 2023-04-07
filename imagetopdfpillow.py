from PIL import Image

img = Image.open("0.jpg")

rgb_img = img.convert("RGB")

rgb_img.save("0.pdf")