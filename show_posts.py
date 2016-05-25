import pages_and_posts
from pymongo import DESCENDING
from pprint import pprint
import sys
import constants

if len(sys.argv) > 1:
    date = sys.argv[1]
    start_time = '{}T00:00:00+0000'.format(date)
    end_time = '{}T23:59:59+0000'.format(date)

    for p in pages_and_posts.posts.find({"created_time": {
        "$gte": start_time,
        "$lt": end_time
    }}).sort(constants.LIKES_AMOUNT, direction=DESCENDING):
        pprint(p)
else:
    for p in pages_and_posts.posts.find().sort('created_time', direction=DESCENDING).limit(50):
        pprint(p)
