#!/usr/bin/env python
import pages_and_posts
import get_object
import facebook
import time
import concurrent.futures

# TODO add testing
num_of_threads = 5


def retrieve_posts(page):
    try:
        d = get_object.graph.get_object('{}/posts?limit=100'.format(page['id']))
        updated_posts_num, inserted_posts_num = 0, 0
        for post in d['data']:
            upsert_summary = pages_and_posts.posts.update_one({'id': post['id']}, {"$set": post}, upsert=True)
            if upsert_summary.upserted_id:
                inserted_posts_num += 1
            else:
                updated_posts_num += 1
        print('Updating page "{}". Inserted {} posts, updated {} posts.'.format(page['name'],
                                                                                inserted_posts_num,
                                                                                updated_posts_num))
    except facebook.GraphAPIError:
        print('"{}" is not a page'.format(page['name']))

t0 = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=num_of_threads) as executor:
    for page in pages_and_posts.pages.find():
        executor.submit(retrieve_posts, page)

print("Done. operation took {0:.2f} seconds".format(time.time() - t0))
