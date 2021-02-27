from PIL import Image, ImageFilter

img = Image.open("fahim.jpg")

img_filter = img.filter(ImageFilter.BLUR)

img_filter.save("Blur.png", "png")