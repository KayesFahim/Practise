from PIL import Image, ImageFilter

img = Image.open("fahim.jpg")
img.thumbnail((400, 400))
img.save('thumb.jpg')
print(img.size)