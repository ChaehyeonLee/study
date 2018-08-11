#feedparser로 RSS 스크레이핑하기

import feedparser

d = feedparser.parse('http://www.aladin.co.kr/rss/special_new/351')

for entry in d.entries:
    print('이름:', entry.title)
    print('링크: ', entry.link)
    print()