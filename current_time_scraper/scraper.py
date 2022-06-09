import requests
from bs4 import BeautifulSoup

URL = "https://www.timeanddate.com/worldclock/"


def extract_date_from_soup(soup: BeautifulSoup) -> str:
    return soup.find(id="ct").text


def get_time_from_country(country: str) -> str:
    page = requests.get(URL + country)
    soup = BeautifulSoup(page.content, "html.parser")
    return extract_date_from_soup(soup)
