import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore
import datetime
# from getpass import getpass

#   parameters: email, password, name, subscription_period
#   output:     1 for user created
#               0 for user already present
#   the function would take inputs and create a user in the database


def register_user(email, password, name, period):
    cred = credentials.Certificate("firebase-sdk.json")
    default_app = firebase_admin.initialize_app(cred)

    flag = 1

    # email = input("Email: ")
    # password = getpass()
    # name = input("Name: ")
    # period = str(input("Period: "))

    try:
        auth.create_user(
            email = email,
            password = password
        )
        print("New user created")
    except:
        print("User already in database")
        flag = 0

    if flag == 0:
        return 0        #User already in database

    if flag != 0:
        user = auth.get_user_by_email(email)

        date = str(datetime.datetime.now().date())

        db = firestore.client()

        doc_ref = db.collection(u'users').document(user.uid)
        doc_ref.set(
            {
                u'name' : name,
                u'period' : period,
                u'registered' : date
            }
        )

        return 1
