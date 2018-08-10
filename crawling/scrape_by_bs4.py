#Beautiful Soup로 스크레이핑하기

from bs4 import BeautifulSoup

with open('full_book_list.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

for a in soup.find_all('a'):
    print(a.get('href'), a.text)