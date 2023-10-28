from selenium import webdriver
import json
from dataclasses import dataclass

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
    spread: float = 0


chrome_driver_path = r"C:\Users\corlh\Downloads\chromedriver_win32\chromedriver.exe"


options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Para executar o navegador em segundo plano, sem uma janela visível


driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)


driver.get("https://veri.bet/odds-picks?filter=upcoming")


driver.implicitly_wait(10)


table_rows = driver.find_elements_by_xpath("//table[@id='odds-picks']//tr")


items = []


for row in table_rows[1:]:  
    data = row.find_elements_by_tag_name('td')
    if len(data) == 11:  
        item = Item(
            sport_league=data[0].text,
            event_date_utc=data[1].text,
            team1=data[2].text,
            team2=data[3].text,
            pitcher=data[4].text,
            period=data[5].text,
            line_type=data[6].text,
            price=data[7].text,
            side=data[8].text,
            team=data[9].text,
            spread=float(data[10].text) if data[10].text else 0.0
        )
        items.append(item)


print(json.dumps([vars(item) for item in items], indent=2))


driver.quit()