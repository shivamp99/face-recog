# Run this file first to setup the folders and database for functionality
from pymongo import MongoClient
from db_layer import * 
myclient = MongoClient(port=27017)

mydb = myclient["face_recog"]
mycollection = mydb["persons"]

# collection does not get created until it gets content, so pushing
# a dummy value 

if mycollection.count()==0:
    result = mycollection.insert_one({'uid':0, 'next_val':1, 'name':'dummy','filepath':'/dummy/'})
    print(result)
# now check if collection exists
print(mydb.list_collection_names())

# now create the folders to store persons images
import os
try:  # replace try with if blocks bcoz error in middle will cause failure at that point
    os.mkdir('../known_images') 
    os.mkdir('../unknown_images') 
    os.mkdir('../identified')
    os.mkdir('../detected')
except OSError as error:  
    print(error)
