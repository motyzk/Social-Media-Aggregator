#!/usr/bin/env python
import pages_and_posts
from pprint import pprint


for p in pages_and_posts.pages.find():
    pprint(p)
    print()
