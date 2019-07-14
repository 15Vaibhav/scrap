from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.common.exceptions import TimeoutException
import time
import csv
index =1
def wplogin(driver):
        driver.get("https://medium.com/")
        time.sleep(3)
        driver.find_element_by_link_text('Sign in').click() 
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/section/div[1]/div/button[1]').click()   
        time.sleep(3)
        driver.find_element_by_id('identifierId').send_keys("vp612512")  
        driver.find_element_by_id('identifierNext').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys("9891299859")
        driver.find_element_by_id('passwordNext').click()
        time.sleep(3)
        address =driver.find_elements_by_css_selector('.streamItem.streamItem--extremeAdaptiveSection.js-streamItem')
        print(address)
        # voting =driver.find_elements_by_css_selector('.ta-right.floating.search_result_rating.col-s-4.clearfix')
        # cusines = driver.find_elements_by_css_selector('.col-s-11.col-m-12.nowrap.pl0')
        # costfortwo =driver.find_elements_by_css_selector('.res-cost.clearfix')
        # i=0
        # for  x in name:
        #     try:
              
        #         rating_1 =voting[i].text
        #         rating_2 = rating_1.replace('\n', ' ').replace('\r', '') 
        #         rating_3 = rating_2.split(' ')
        #         print(rating_2)
        #         row =[]
        #         rs = (costfortwo[i].text)
        #         mystring = rs.replace('\n', '').replace('\r', '')
        #         stri = mystring.split(':')[-1]
        #         last = stri[1:]
        #         index +=1
        #         row.append("{} name: {}, address: {}, rating: {}, cost for two: {}, CUISINES: {} ".format(index,x.text,address[i].text,rating_2,last,cusines[i].text))
        #         with open('scrap.csv', 'a') as csvFile:
        #                 writer = csv.writer(csvFile)
        #                 writer.writerow(row)    
        #         print(row)
        #         csvFile.close()
        #         i +=1
        #     except Exception:
        #              pass





chrome_options = Options()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome('/home/virus/project/python/scrap/chromedriver',chrome_options=chrome_options)
action = ActionChains(driver) 
wplogin(driver)   
# driver.close()