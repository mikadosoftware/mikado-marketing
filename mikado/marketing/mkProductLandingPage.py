"""
Publishing and bootstrap etc

Marketing landing page:
Adjust the image to blue fade using PIL below
Use the index.html as a landing page 
Write up how in the chapters (bootstrap.html)
Then how to convert to a book-like view 

perhaps use:
https://css4.pub/

"""
from PIL import Image, ImageFilter  # imports the library


im = Image.open("kelly-sikkema-1345376-unsplash.jpg")
alpha = Image.new("L", im.size, 0)


from PIL import ImageEnhance, ImageOps

#enhancer = ImageEnhance.Color(im)
#im = enhancer.enhance(.9)
BLUE = (60,60,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
grayscale = ImageOps.grayscale(im)
grayscale = ImageOps.colorize(grayscale, BLACK, BLUE)
grayscale.putalpha(160)#99
grayscale.save('blackblue.png')
im.save('test.png')

