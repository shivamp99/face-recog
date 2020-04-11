from pymongo import MongoClient
from db_layer import * 
from recognise import *
from detect import *
client = MongoClient(port=27017)

collection = client.face_recog.persons

temp = recognise_face('/home/shivam/Desktop/software_engineering/face-recog-master/unknown_images/3.jpeg')
print(temp)