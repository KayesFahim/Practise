from PIL import Image, ImageFilter

img = Image.open("fahim.jpg")

img_filter = img.convert('L')

box = (100,100, 400, 400) 

img_crop = img_filter.crop(box)

img_crop.save("crop.png", "png")