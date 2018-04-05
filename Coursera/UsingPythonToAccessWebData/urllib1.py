import urllib.request

fhand = urllib.request.urlopen('https://github.com/ChaehyeonLee')
for line in fhand:
    print(line.decode().strip())
