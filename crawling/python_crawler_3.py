import requests
import lxml.html

def main():
    """
    크롤러의 메인 처리
    """
    session = requests.Session()
    response = requests.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
    urls = scrape_list_page(response)

    for url in urls:
        print(url)

def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('.view_box .book_tit a'):
        url = a.get('href')
        yield url

if __name__ == '__main__':
    main()
