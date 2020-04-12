from pymongo import MongoClient
from db_layer import * 
from recognise import *
from detect import *
from PIL import Image
client = MongoClient(port=27017)

collection = client.face_recog.persons

# to insert person into the system
# input parameters: (string) name, filepath of photo
def insert(name,filepath):
    return insert_person(collection,name,filepath)

def recognise(filepath):
    person_photo_list = recognise_face(filepath)
    person_details_list = []
    for photo_name in person_photo_list:
        person_details = get_details_file(collection,photo_name)
        person_details_list.append(person_details)
    return person_details_list

def detect(filepath):
    detect_face(filepath)

def view(name):
    a = get_details(collection,name)
    if a==None:
        return
    print(a)
    filepath = a['filepath']
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    img=mpimg.imread(filepath)
    imgplot = plt.imshow(img)
    plt.show()
    return a

def remove(name):
    return remove_person(collection,name)

# temp = recognise_face('/home/shivam/Desktop/software_engineering/face-recog-master/unknown_images/3.jpeg')
# print(temp)