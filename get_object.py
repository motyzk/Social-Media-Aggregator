from pprint import pprint
import facebook

with open("TOKEN.txt") as f:
    TOKEN = f.read().strip()

graph = facebook.GraphAPI(access_token=TOKEN, version='2.5')
