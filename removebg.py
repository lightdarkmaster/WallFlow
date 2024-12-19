from rembg import remove
from PIL import Image

input_path = './images/image1.jpg'
output_path = './outputImage/image1.png'
inp = Image.open(input_path)
output =    remove(inp)
output.save(output_path)
Image.open("image1.png")