import current_time_scraper.scraper as scraper
import re
import pytest
from bs4 import BeautifulSoup


def test_extract_date_from_soup():
    soup = BeautifulSoup("<html><span id='ct'>00:00:00</span></html>", "html.parser")
    assert scraper.extract_date_from_soup(soup) == "00:00:00"


@pytest.mark.parametrize("country", ["poland", "germany", "netherlands"])
def test_get_time_from_country(country: str):
    time = scraper.get_time_from_country(country)
    assert re.search(r"^\d{2}:\d{2}:\d{2}", time) is not None
