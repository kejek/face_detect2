import face_recognition
import json
from PIL import Image, ImageDraw

image = face_recognition.load_image_file("multi.jpg")
face_locations = face_recognition.face_locations(image)

all_locations = []

pil_image2 = Image.fromarray(image)

width = 5

for (top, right, bottom, left) in face_locations:
    all_locations.append([top, right, bottom, left])

    # Crop image out (save to CDN for recognition later?
    #face_image = image[top:bottom, left:right]
    #pil_image = Image.fromarray(face_image)
    #pil_image.show()

    # Create a Pillow ImageDraw Draw instance to draw with
    draw = ImageDraw.Draw(pil_image2)
    for i in range(0, width):
        draw.rectangle(((left+i, top+i), (right+i, bottom+i)), outline=(255, 0, 0))

print(json.dumps(['faces', all_locations]))

pil_image2.show()
