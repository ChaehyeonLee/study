import lxml.html
from pymongo import MongoClient

tree = lxml.html.parse('full_book_list.html')
html = tree.getroot()

client = MongoClient('localhost', 27017)
db = client.scraping
collection = db.links

collection.delete_many({})

for a in html.cssselect('a'):
    url = a.get('href')
    title = (a.text.strip() if a.text else '')
    collection.insert_one({
        'url': url,
	'title': title
    })

for link in collection.find().sort('_id'):
    print(link['_id'], link['url'], link['title'])
