from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import random
from app import db
from app.models import Game

def fetch_game_data_instant_gaming():
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    page_number = 1
    
    while True:
        url = f"https://www.instant-gaming.com/ru/search/?platform%5B0%5D=1&type%5B0%5D=&sort_by=&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&min_price=0&max_price=200&noprice=1&gametype=all&search_tags=0&query=&page={page_number}"
        driver.get(url)

        scroll_pause_time = random.uniform(1, 3)
        max_scrolls = 12

        for _ in range(max_scrolls):
            ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(scroll_pause_time)
        
        wait = WebDriverWait(driver, 10)
        games = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".item.force-badge")))
        
        if not games:
            print("No games found on this page. Ending extraction.")
            break

        for game in games:
            names = game.find_elements(By.CSS_SELECTOR, ".title")
            prices = game.find_elements(By.CSS_SELECTOR, ".price")
        
            for name, price in zip(names, prices):
                game_name = name.text
                game_price = price.text
                store = 'Instant Gaming'
                date = datetime.utcnow()
                
                try:
                    game_price = float(game_price.replace('€', '').replace(',', '.').strip())
                except ValueError:
                    continue 

                latest_game = Game.query.filter_by(name=game_name, store=store).order_by(Game.date.desc()).first()
                if latest_game is None or latest_game.price != game_price:
                    game_record = Game(name=game_name, price=game_price, store=store, date=date)
                    db.session.add(game_record)

        db.session.commit()

        page_number += 1
        time.sleep(3) 
    
    driver.quit()