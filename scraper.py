import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

URL = "https://mosir.elblag.eu/obiekt-sportowy/baseny/crw-dolinka/"

def get_people_count():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    count_element = soup.select_one(".details-icon-pool")  # np. <div class="people-count">23</div>
    count = int(count_element.text.strip())
    return count

def log_data(count):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([now, count])

if __name__ == "__main__":
    try:
        count = get_people_count()
        log_data(count)
        print(f"Zapisano: {count} osób")
    except Exception as e:
        print(f"Błąd: {e}")
