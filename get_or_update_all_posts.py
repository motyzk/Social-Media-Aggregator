#!/usr/bin/env python
import pages_and_posts
import get_object
import facebook
import time
import concurrent.futures
import constants

# TODO add testing
NUM_OF_THREADS = 5


def retrieve_posts(page):
    try:
        d = get_object.graph.get_object('{}/posts?limit=100'.format(page['id']))
        updated_posts_num, inserted_posts_num, total_likes = 0, 0, 0
        for post in d['data']:
            summary = get_object.graph.get_object('{}/likes?summary=true'.format(post['id']))['summary']
            total_likes += summary['total_count']
            post[constants.LIKES_AMOUNT] = summary['total_count']
            upsert_summary = pages_and_posts.posts.update_one({'id': post['id']}, {"$set": post}, upsert=True)
            if upsert_summary.upserted_id:
                inserted_posts_num += 1
            else:
                updated_posts_num += 1
        print('Updating page "{}". Inserted {} posts, updated {} posts. total likes: {}'.format(page['name'],
                                                                                                inserted_posts_num,
                                                                                                updated_posts_num,
                                                                                                total_likes))
    except facebook.GraphAPIError:
        print('"{}" is not a page'.format(page['name']))

t0 = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_OF_THREADS) as executor:
    for page in pages_and_posts.pages.find():
        executor.submit(retrieve_posts, page)

print("Done. operation took {0:.2f} seconds".format(time.time() - t0))
