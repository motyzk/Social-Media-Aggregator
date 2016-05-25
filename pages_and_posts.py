import pymongo

client = pymongo.MongoClient()

db = client.get_database('socialagg')
# db = client['socialagg']

pages = db.get_collection('pages')
# pages = db['pages']

pages.create_index('id', unique=True)

posts = db.get_collection('posts')
# posts = db['posts']

posts.create_index('id', unique=True)
