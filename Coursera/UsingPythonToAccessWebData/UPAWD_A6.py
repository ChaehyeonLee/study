import urllib.request, urllib.parse, urllib.error
import json

while True:
    url = input('Enter location: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    info = json.loads(data)

    comment_num = len(info['comments'])
    comment_counts_sum = 0
    
    for item in info['comments']:
        comment_counts_sum += int(item['count'])

    print("Count: ", comment_num)
    print("Sum: ", comment_counts_sum)
    ask_continue = input("Do you want to continue?(y/n): ")
    if ask_continue == 'n':
        break
