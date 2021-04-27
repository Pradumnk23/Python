from PIL  import Image
from PIL import ImageFilter

tringu = Image.open("Screenshot (80).png")
blur = tringu.filter(ImageFilter.BLUR)
detail = tringu.filter(ImageFilter.DETAIL)
edges = tringu.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()