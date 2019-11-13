from PIL import Image

for n in range(1,2000):
    name = "old_image"+str(n)+".png"
    with Image.open(name) as image:
        width, height = image.size 
    image = image.convert('RGBA')
    image = image.resize((180, 180), resample=Image.ANTIALIAS)
    new_image = Image.new('RGBA', (360, 360), (0, 0, 0, 0))
    new_image.paste(image,(90,90))
    new_image.save("new/new_image"+str(n)+".png")



