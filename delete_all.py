import pymongo

client = pymongo.MongoClient()
client.drop_database('socialagg')

