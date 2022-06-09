from current_time_scraper.scraper import get_time_from_country
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <country_name>")
    else:
        time = get_time_from_country(sys.argv[1])
        print(f"Current time in {sys.argv[1]}: {time}")
