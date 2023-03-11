

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.support.wait import WebDriverWait

PATH = "/home/boran/chromedriver"
driver_service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=driver_service)

amazon_price = "";
trendyol_price = "";
alibaba_price = "";

product_name = "JBL FLIP 5"

driver.get("https://www.amazon.com/")

search = driver.find_element("id", "twotabsearchtextbox")
search.send_keys(product_name)
search.send_keys(Keys.RETURN)
price_symbol = driver.find_element(By.CLASS_NAME, "a-price-symbol")
price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")
amazon_price = price_symbol.text + price_whole.text + "." + price_fraction.text
print("Amazon: " + amazon_price)

driver.execute_script("window.open('about:blank', 'secondtab');")
driver.switch_to.window("secondtab")
driver.get("https://www.trendyol.com/butik/liste/1/kadin?gads=true&tyutm_source=google&tyutm_medium=cpc&tyutm_campaign=new_gl_trendyol_2_x:brand-pure_excl_istanbul&gclid=EAIaIQobChMI_7SUiKmD_AIVQtKGCh3Y4g35EAAYASAAEgIhWfD_BwE")
search2 = driver.find_element(By.CLASS_NAME, "vQI670rJ")
search2.send_keys(product_name)
search2.send_keys(Keys.RETURN)
price = driver.find_element(By.CLASS_NAME, "prc-box-dscntd")
trendyol_price = price.text
print("Trendyol: " + trendyol_price)

driver.execute_script("window.open('about:blank', 'thirdtab');")
driver.switch_to.window("thirdtab")
driver.get('https://www.alibaba.com/?src=sem_ggl&field=UG&from=sem_ggl&cmpgn=9922923046&adgrp=97780319742&fditm=&tgt=kwd-784652173659&locintrst=&locphyscl=1012763&mtchtyp=e&ntwrk=g&device=c&dvcmdl=&creative=432272608465&plcmnt=&plcmntcat=&aceid=&position=&gclid=EAIaIQobChMI-c-yvrCD_AIVZYxoCR2VIwE3EAAYASAAEgIfBfD_BwE')
search3 = driver.find_element(By.CLASS_NAME, "ui-searchbar-keyword")
search3.send_keys(product_name)
search3.send_keys(Keys.RETURN)
price3 = driver.find_element(By.CLASS_NAME, "elements-offer-price-normal__promotion")
alibaba_price = price3.text
print("Alibaba: " + alibaba_price)

driver.quit()







