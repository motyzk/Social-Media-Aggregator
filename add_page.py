#!/usr/bin/env python
import sys
import pages_and_posts
import get_object
import facebook

page = sys.argv[1].split('/')[-1]
try:
    d = get_object.graph.get_object(page, fields="website, fan_count, name")
    print(d)
    pages_and_posts.pages.update({'id': d['id']}, d, upsert=True)
    print("OK, added page id #{} with {} fans.".format(d['id'], d['fan_count']))
except facebook.GraphAPIError:
    print('Not a page')

