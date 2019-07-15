from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.common.exceptions import TimeoutException
import pymongo
import time
import csv
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.blogs
selected_list=[]
def wplogin(driver):
        link_list =[]
# # **********************************************************Medium************************************************************************
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
        time.sleep(10)
        links =driver.find_elements_by_css_selector('.ui-h2.ui-xs-h4.ui-clamp3')
        alink = driver.find_elements_by_css_selector('.ds-link.ds-link--stylePointer.u-overflowHidden.u-flex0.u-width100pct')
        print("Medium")
        index =0
        for x in links:
                link_list.append({'title':x.text,'link':alink[index].get_attribute('href')})
                index +=1
# # **********************************************************FreeCodeCamp************************************************************************
        driver.get("https://www.freecodecamp.org/news/")
        time.sleep(3)
        links_1 =driver.find_elements_by_css_selector('.post-card-title')
        alink_1 = driver.find_elements_by_xpath('//*[@class="post-card-title"]/a')
        index=0
        print("freecodecamp")
        for x in links_1:
                 link_list.append({'title':x.text,'link':alink_1[index].get_attribute('href')})
                 index +=1
#  **********************************************************Dev.TO************************************************************************
        driver.get("https://dev.to/")
        time.sleep(3)
        links_2 =driver.find_elements_by_css_selector('.content')
        alinks_2 =driver.find_elements_by_css_selector('.index-article-link')
        index=0
        time.sleep(3)
        print("dev.to")
        for x in links_2:
                link_list.append({'title':x.text,'link':alinks_2[index].get_attribute('href')})
                index +=1
# **********************************************************HeckerNoon************************************************************************
        driver.get("https://community.hackernoon.com/c/Software-Development")
        time.sleep(3)
        links_3 =driver.find_elements_by_css_selector('.title.raw-link.raw-topic-link')
        print("hackernoon")
        index=0
        for x in links_3:
                 link_list.append({'title':x.text,'link':links_3[index].get_attribute('href')})
                 index +=1

        # print("Data::",link_list)
        keys =['javascript','angular','angularjs','reactjs','nodejs','node.js']
        for k in keys:
                for x in link_list:
                        if k in x['title'].casefold():
                                selected_list.append(x)
        print(selected_list)

      



chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome('/home/decision/python/python/Medium/scrap/chromedriver',chrome_options=chrome_options)
action = ActionChains(driver) 
wplogin(driver)   
driver.close()
posts = db.links
for x in selected_list:
        post_id = posts.insert_one(x).inserted_id        
