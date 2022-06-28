from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from selenium import webdriver 
import pandas as pd
import time

class InstaScraper:
    def __init__(self):
        self.driver = ''
        # self.questions = []
        # self.answers = []
        self.links = []
        self.soup = ''
    
    def start_driver(self):
        self.driver = webdriver.Chrome('H:\DOWNLOADS\chromedriver.exe')

    def close_driver(self):
        self.driver.close()

    def open_url(self, url):
        self.driver.get(url)

    def login(self,UName,PWord):
        self.open_url('https://www.instagram.com/accounts/login/')

        time.sleep(5)
        email_element = self.driver.find_element(By.CSS_SELECTOR,"input[name='username']")
        password_element = self.driver.find_element(By.CSS_SELECTOR,"input[name='password']")
        time.sleep(5)
        email_element.send_keys(UName)
        time.sleep(5)
        password_element.send_keys(PWord)
        time.sleep(5)
        password_element.send_keys(Keys.ENTER)

        not_now = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()
        not_now2 = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()
        
    def open_new(self,keyword):
        page = self.driver.get("https://www.instagram.com/explore/tags/" + keyword)
        self.driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(5)

    def get_soup(self):
        html = self.driver.page_source
        self.soup = bs(html,'html.parser')

    def get_links(self):
        
        data = self.soup.findAll('div',attrs={'class':'_aabd _aa8k _aanf'})
        for div in data:
            lin = div.findAll('a')
            for a in lin:
                self.links.append('https://www.instagram.com/'+a.get('href')) 

if __name__ == "__main__":
    scraper = InstaScraper()
    scraper.start_driver()
    username = "USERNAME"
    password = "PASSWORD"
    scraper.login(username,password)
    keyword = "Python"
    scraper.open_new(keyword)
    scraper.get_soup()
    scraper.get_links()
    scraper.close_driver()
