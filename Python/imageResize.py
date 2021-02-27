from PIL import Image, ImageFilter

img = Image.open("fahim.jpg")

img_filter = img.resize((500, 500))

img_filter.save("500x500.png", "png")