# provides functions for calling from gui and api
from pymongo import MongoClient
from shutil import copyfile
import os

# used to get the next number in serial order to assign to a new person
# input parameter: (pymongo) db.collection
# output: next serial number
def get_next_value(collection):
    result = collection.find_one({'uid':0})
    result = result['next_val']
    temp = collection.update_one({'uid':0},{"$set": { 'next_val': result+1 }})
    return result

# create a new id in the db and store the data
# input parameters: (pymongo) db.collection, (string) person name, (string) filepath of person's image
# output: response of database after insertion
# error to be thrown if same person already exists
def insert_person(collection,name,filepath):
    uid = get_next_value(collection)
    destination = '../known_images/'+name+'.jpeg'
    copyfile(filepath,destination)
    result = collection.insert_one({'uid':uid, 'name':name,'filepath':destination})
    return result

# remove a person from the db
# input parameters: (pymongo) db.collection, (string) person name
# functionality: record of person removed from database and photo from known_images
# output: None if person does not exist, (string) db response if person exists
def remove_person(collection,name):
    if collection.find_one({'name':name})==None:
        return None
    result = collection.delete_one({'name':name})
    # removing the photo of the person
    destination = '../known_images/'+name+'.jpeg'
    os.remove(destination)
    return result

# this function can be used to edit details of person, or add a new detail
# input parameters: (pymongo) db.collection, (string) person name, (string) fieldname, (string) new value
# output: response of database
def edit_details(collection,name,fieldname,value):
    result = collection.update_one({'name':name},{"$set":{fieldname:value}})
    return result

# view details of person 
# input parameters: (pymongo) db.collection, (string) person name
# output: (dict) the details of person 
def get_details(collection,name):
    result = collection.find_one({'name':name})
    return result

# view details of person from his filepath
# input parameters: (pymongo) db.collection, (string) photo file path from known_images
# output: (dict) the details of person 
def get_details_file(collection,filepath):
    result = collection.find_one({'filepath':filepath})
    return result


