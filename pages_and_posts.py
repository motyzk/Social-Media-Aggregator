from pprint import pprint
import pymongo
import get_object

client = pymongo.MongoClient()

db = client.get_database('socialagg')
# db = client['socialagg']

pages = db.get_collection('pages')
# pages = db['pages']

pages.create_index('id', unique=True)

posts = db.get_collection('posts')
# pages = db['pages']

posts.create_index('id', unique=True)
