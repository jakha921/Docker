import requests
import googletrans
import random
from bs4 import BeautifulSoup


def main():
    # Translator
    translator = googletrans.Translator()
    #
    # # Random advice
    res = requests.get('https://api.adviceslip.com/advice')
    res = res.json()
    text = res['slip'].get('advice')
    tr_text = translator.translate(text, dest='ru', scr='auto')
    print("Совет:", tr_text.text, end='\n\n')

    # # Hacker rank news
    res = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    item = random.choice(res.json())
    news_res = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{item}.json?print=pretty')
    news = news_res.json()
    tr_news = translator.translate(news.get('title'), dest='ru', scr='auto')
    print("Новости:", tr_news.text, end='\n\n')

    # Parse site
    res = requests.get('https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/')
    soup = BeautifulSoup(res.text, 'html.parser')
    soup = soup.select('section > div > p')
    soup = str(soup[1])
    words = soup.replace('<br/>', ' ').replace("</p>", '').replace("<p>", '').split(" ")
    word = random.choice(words)
    tr_word = translator.translate(word, dest='ru', scr='auto')
    print(f'Одно из самых часто употребляемых слова "{word}" переводиться как "{tr_word.text}"', end='\n\n')


if __name__ == "__main__":
    main()
