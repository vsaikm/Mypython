#unsplas.com website
from PIL import Image,ImageFilter

img = Image.open('4.jpg')
#print(img.size)#(5611, 5339)
img.thumbnail((300,300))#aspect ratio is changed the image is blurred so we use thumbnail method thumbnail keeps the aspect ratio 
img.save('thumbnail.jpg')
