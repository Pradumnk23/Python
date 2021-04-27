from PIL import Image

baby = Image.open("Screenshot (80).png")
sqaure_baby = baby.resize((100, 100))
flip_baby = baby.transpose(Image.FLIP_LEFT_RIGHT)
spin_baby = baby.transpose(Image.ROTATE_90)

baby.show()
sqaure_baby.show()
flip_baby.show()
spin_baby.show()
