from PIL import Image,ImageFilter 

#img = Image.open("1.jpg","rb")
img = Image.open('1.jpg')


'''
print(img.format)#JPEG
print(img.resize)
print(img.size)#(320,298)
print(img.mode)#RGB
'''

'''
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png" , 'png')   
'''
'''
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("SHARPEN.png",'png')
'''

'''
filtered_img = img.convert('L')

crooked = filtered_img.rotate(180)

crooked.save("grey.png",'png')
#filtered_img.show()
'''
'''
filtered_img = img.convert('L')

resize = filtered_img.resize((100, 100))#resize accepts tuple format 
resize.save("grey.png",'png')
'''
filtered_img = img.convert('L')

resize = filtered_img.resize((320, 298))#resize accepts tuple format 
resize.save("grey.png",'png')
box = (100, 100, 400, 400)
region = resize.crop(box)
region.save("grey.png",'png')

