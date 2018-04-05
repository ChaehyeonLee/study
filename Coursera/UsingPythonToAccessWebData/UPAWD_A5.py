import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

while True:
    url = input('Enter location: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)

    results = tree.findall('.//comment')
    comment_num = len(results)
    comment_counts_sum = 0
    for i in range(len(results)):
        comment_counts_sum += int(results[i].find('count').text)

    print("Count: ", comment_num)
    print("Sum: ", comment_counts_sum)
    ask_continue = input("Do you want to continue?(y/n): ")
    if ask_continue == 'n':
        break
