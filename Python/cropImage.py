from PIL import Image, ImageFilter

img = Image.open("fahim.jpg")

img_filter = img.convert('L')

img_crop = img_filter.crop((100,100,500,500))

img_crop.save("crop.png", "png")