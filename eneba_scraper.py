from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from app import db
from app.models import Game
import random

def fetch_game_data_eneba():
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    page_number = 1
    
    while True:
        url = f"https://www.eneba.com/es/store/games?drms[]=steam&page={page_number}&regions[]=global&regions[]=spain&types[]=game"
        driver.get(url)

        scroll_pause_time = random.uniform(1, 3)
        max_scrolls = 3

        for _ in range(max_scrolls):
            ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(scroll_pause_time)
        
        wait = WebDriverWait(driver, 10)
        games = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".pFaGHa.WpvaUk")))
        
        if not games:
            print("No games found on this page. Ending extraction.")
            break

        for game in games:
            names = game.find_elements(By.CSS_SELECTOR, ".YLosEL")
            prices = game.find_elements(By.CSS_SELECTOR, ".L5ErLT")
        
            for name, price in zip(names, prices):
                game_name = name.text
                game_price = price.text
                store = 'Eneba'
                date = datetime.utcnow()  
                
                try:
                    game_price = float(game_price.replace('₽', '').replace(',', '.').strip())
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