'''
Things to do..
- make sure to have user enter country, zipcode, etc.-----
- now need to create loop in parsers so it runs the number of dealers times..
- click on each link individually -- unpack info
- write to excel file
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time



from page.dealers_page import DealerPage




chrome = webdriver.Chrome(executable_path = '/Users/aidanpak/Compsci/drivers/chromedriver')
chrome.get('https://cedia.net/find-a-cedia-integrator/')
page = DealerPage(chrome)

country_name = input('Enter desired country name. ')
zipcode = input('Enter desired zipcode. ')
radius= input('Enter desired radius. ')

#enter information
page.select_country(country_name)
page.zipcode_search(zipcode)
page.select_radius(radius)

#wait before hitting submit


#search
page.click_search_button()

time.sleep(3)

links = page.count_links()
data = []


for link in links:
    chrome.get(f'{link}')
    time.sleep(2)
    data.append(page.extract_dealer_info)
    chrome.close()

print(data)









