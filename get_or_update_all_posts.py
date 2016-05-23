#!/usr/bin/env python
import pages_and_posts
import get_object
import facebook

try:
    d = get_object.graph.get_object('DonaldTrump',
                                    fields="posts")
    # pages_and_posts.posts.update({'id': d['id']},
    #                              d,
    #                              upsert=True)
    print('Updating page "donald trump". Inserted 10 posts, update 90 posts.'.format(d['id'], d['fan_count']))
except facebook.GraphAPIError:
    print('Not a page')

