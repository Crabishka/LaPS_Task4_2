from bs4 import BeautifulSoup
import requests


def number_to_string(number):
    url = 'https://wordnum.ru/d/' + str(number)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('span')
    return quotes[1].text
