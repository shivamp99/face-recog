import face_recognition
from PIL import Image
import os

#   parameters: path of file to be processed
#   input:      ../known_images/ as the database of known persons
#   output:     ../identified/
#   returns: list of filepaths of the persons who have been recognised
#   all the identified persons are put in folder 'identified/<filename>'
#   identified persons photo is extracted with their name as .jpeg
def recognise_face(filepath):
    known_name = []
    known_images = []
    known_files = []

    known_entries = os.listdir('../known_images/')
    for entry in known_entries:
        image = face_recognition.load_image_file('../known_images/'+entry)
        try:
            known_images.append(face_recognition.face_encodings(image)[0])
        except:
            print("No face found in this image")
        name = os.path.splitext(entry)[0]
        known_name.append(name)
        known_files.append('../known_images/'+entry)
    unknown_image = []

    # f = open('identified/'+os.path.splitext(entry)[0]+'.txt', 'w')
    filename = os.path.basename(filepath)
    (dirname, ext) = os.path.splitext(filename)
    try:
        os.mkdir('../identified/'+dirname)
    except:
        t = 0
        # print()
    image = face_recognition.load_image_file(filepath)
    try:
        unknown_image = face_recognition.face_encodings(image)
        face_locations = face_recognition.face_locations(image)
    except:
        print("No face found in this image")

    t = 0
    unknownf = 0
    recognised_files = []
    for unk in unknown_image:
        results = face_recognition.compare_faces(known_images, unk)
        i = 0
        flag = 0
        for j in range(len(known_name)):
            if(str(results[i]) == 'True'):
                # f.write(name+'\n')
                flag = 1
                top, right, bottom, left = face_locations[t]
                face_image = image[top:bottom, left:right]
                pil_image = Image.fromarray(face_image)
                pil_image.save("../identified/"+dirname+"/"+known_name[j]+".jpeg")
                recognised_files.append(known_files[j])
            i+=1

        if flag == 0:
            top, right, bottom, left = face_locations[t]
            face_image = image[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
            fn = os.path.splitext(entry)[0]
            pil_image.save("../identified/"+dirname+"/unknown_"+str(unknownf)+".jpeg")
            unknownf+=1
        t+=1
        # f.close()
    return recognised_files