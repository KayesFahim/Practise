from PIL import Image, ImageFilter

img = Image.open("fahim.jpg")

img_filter = img.convert('L')

img_filter.save("B&W.png", "png")