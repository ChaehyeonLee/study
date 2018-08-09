#lxml로 스크레이핑하기
import lxml.html

tree = lxml.html.parse('full_book_list.html')
html = tree.getroot()

for a in html.cssselect('a'):
    print(a.get('href'), a.text)