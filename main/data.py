from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.id import ID
import os
# from dotenv import load_dotenv



""" Configuring Appwrite Client """
# Instantiating Appwrite Client
client = Client()
# To load environment variables
# load_dotenv()




# Configuring Appwrite Client
(client
 # Setting API Endpoint
 .set_endpoint('https://cloud.appwrite.io/v1')
 # Setting Project ID
 .set_project(os.getenv('PROJECT_ID'))
 # Setting API Key
 .set_key(os.getenv('API_KEY'))
 )

databases = Databases(client)


def add_doc(document):
    document_id = ID.unique()
    try:
        doc = databases.create_document(
            database_id=os.getenv('DB_ID'),
            collection_id=os.getenv('C_ID'),
            document_id=document_id,
            data=document
        )

        return True

    except Exception as e:
        return False


def get_doc():
    result = databases.list_documents(
        os.getenv('DB_ID'), os.getenv('C_ID'))["documents"]
    data = []
  
    for each in result:
        l = {"Name": each["Name"],
                             
                             "Ratings": each["Ratings"],
                             "Custom_msg": each["Custom_msg"],
                             "id":each["$id"]
                             }
        data.append(l)
    data=data[::-1]
    return data


def delete_doc(doc_id):
    try:
        databases.delete_document(
            os.getenv('DB_ID'), os.getenv('C_ID'), doc_id)
    except:
        return False
    return True


