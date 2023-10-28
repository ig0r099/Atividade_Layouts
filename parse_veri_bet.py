from selenium import webdriver
from dataclasses import dataclass, asdict
import json
import time

@dataclass
class Item:
    sport_league: str = ''
    event_date_utc: str = ''
    team1: str = ''
    team2: str = ''
    pitcher: str = ''
    period: str = ''
    line_type: str = ''
    price: str = ''
    side: str = ''
    team: str = ''
    spread: float = 0.0


driver = webdriver.Chrome()


driver.get("https://veri.bet/simulator")


time.sleep(5)


button = driver.find_element_by_xpath("//button[contains(text(), 'Access Betting Simulator')]")
print(button)

button.click()


time.sleep(5)


items = []


example_item = Item(
    sport_league='Basketball',
    event_date_utc='2023-10-27T08:00:00Z',
    team1='Team A',
    team2='Team B',
    pitcher='',
    period='Full time',
    line_type='Moneyline',
    price='-110',
    side='',
    team='',
    spread=0.0
)

items.append(example_item)


items_dict_list = [asdict(item) for item in items]


print(json.dumps(items_dict_list, indent=4))


driver.quit()
