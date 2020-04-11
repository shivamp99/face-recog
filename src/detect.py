import face_recognition
from PIL import Image
import os

# input parameter: (string) path of the photo 
# output: saves a photo in detected folder with the face features outlined
def detect_face(filepath):
    image = face_recognition.load_image_file(filepath)
    face_locations = face_recognition.face_locations(image)
    filename = os.path.basename(filepath)
    (dirname, ext) = os.path.splitext(filename)
    if len(face_locations)>0:
        try:
            os.mkdir('../detected/'+dirname)
        except:
            print()
    for i in range(len(face_locations)):
        top, right, bottom, left = face_locations[i]
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.save("../detected/"+dirname+"/"+str(i)+".jpeg")


