import urllib.request  # used to send requests basically https requests
from bs4 import BeautifulSoup  # used to parse xml and html pages so that we can extract data from webpages. It
# creates a parse tree for webpages
import time
from plyer import notification

if __name__ == '__main__':
    url = "https://www.dictionary.com/e/word-of-the-day/"  # any url can be inserted here as u wish
    html_file = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_file, 'lxml')  # for documentation check this https://zetcode.com/python/beautifulsoup/

    soup1 = soup.find(class_="otd-item-headword__word")  # inspect the page and find the specific data to crawl the
    # data from the html code

    try:
        soup1 = soup1.get_text()
    except AttributeError:
        print('No words for today. You have learnt enough')
        exit()


    txt10 = soup1.rstrip()  # The rstrip() method returns a copy of the string by removing the trailing characters
    # specified as argument.
    soup2 = soup.find(class_="otd-item-headword__pos")
    soup2 = soup2.get_text()
    txt11 = soup2.rstrip()
    soup3 = soup.find(class_="wotd-item-origin__content wotd-item-origin__content-full")
    txt = soup3.get_text()
    txt1 = txt.rstrip()

    notification.notify(
        title="*** WORD OF THE DAY ***" + "\n" + ' '.join(txt10.split()) + "\n",
        message="MEANING:" + ' '.join(txt11.split()),
        # app_icon=r"C:\Users\HP\PycharmProjects\MyProjects\book.ico",
        timeout=60
    )
    time.sleep(60*60)
