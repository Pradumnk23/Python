from PIL import Image

img = Image.open("Screenshot (80).png")
print(img.size)
print(img.format)

# This is for cropeed img area and open that file
area = (180, 249, 280, 315)
cropped_img = img.crop(area)
img.show()
cropped_img.show()

# This is for split and add
r, g, b = img.split()
new_img = Image.merge("RGB", (b, g, r))
new_img.show()