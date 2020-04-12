import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore
from firebase import Firebase
import datetime
# from getpass import getpass

#   parameters: account_info (dictionary)
#   output:     0 for expired subscription
#               1 for active subscription
#   the function would check if the user is an active subscriber

def check_active_subscription(account_info):
    name = account_info['name']
    registered_date = account_info['registered']
    period = int(account_info['period'])

    registered_date = datetime.datetime.strptime(registered_date, '%Y-%m-%d' ).date()                                                                                                                                                                                                                                                                                                                                               

    current_date = datetime.datetime.now().date()

    used = (current_date-registered_date).days

    print("User : " + name)

    if used > period:
        print("Product expired!!")
        return 0
    
    else:
        print("Product subscribed for " + str(period-used) + " days")
        return 1


#   parameters: email, password
#   output:     -1 for failed sign in
#                0 for expired subscription
#                1 for active subscription
#   the function would take inputs and sign in a user and
#   subsequently check for active subscription by calling 
#   check_active_subscription()

def user_signin(email, password):
    cred = credentials.Certificate("firebase-sdk.json")
    default_app = firebase_admin.initialize_app(cred,[])

    config = {
        "apiKey": "AIzaSyClkYXaXc4HfmhFPlDoA1RC1GujPLa6gVQ",
        "authDomain": "facial-recognition-27dae.firebaseapp.com",
        "databaseURL": "https://facial-recognition-27dae.firebaseio.com",
        "projectId": "facial-recognition-27dae",
        "storageBucket": "facial-recognition-27dae.appspot.com",
        "messagingSenderId": "451809109876",
        "appId": "1:451809109876:web:8547802714bc1f58b16e21",
        "measurementId": "G-106E1H6H9K"}

    firebase = Firebase(config)

    auth = firebase.auth()

    # email = input("Email: ")
    # password = getpass()

    flag = 1
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("Authentication successful")
    except:
        print("Login failed")
        flag = 0

    if flag == 0:
        return -1

    if flag == 1:

        db = firebase_admin.firestore.client()

        user = firebase_admin.auth.get_user_by_email(email)

        doc_ref = db.collection(u'users').document(user.uid)

        account_info = doc_ref.get().to_dict()      
        #dict type object having all customer details

        return check_active_subscription(account_info)