#!/usr/bin/env python
import pymongo
import sys

collection_name = sys.argv[1]
client = pymongo.MongoClient()
db = client.get_database('socialagg')
does_collection_exist = collection_name in db.collection_names()
if does_collection_exist:
    collection = db.get_collection(collection_name)
    db.drop_collection(collection)
    if collection_name in db.collection_names():
        print("operation failed")
    else:
        print("collection deleted")
else:
    print("collection '{}' does not exist. didn't run operation".format(collection_name))
