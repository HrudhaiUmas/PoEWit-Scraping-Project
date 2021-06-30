'''
This file uses the chromedriver to gather data from cedia.org -- MAKE SURE TO PASTE IN PATH OF YOUR CHROME DRIVER INTO chrome VAR
It returns a list of all the links of the individual dealer pages.
'''

from selenium import webdriver
import time


from page.dealers_page import DealerPage



#paste correct path to driver
chrome = webdriver.Chrome(executable_path = '/Users/aidanpak/Compsci/drivers/chromedriver')
chrome.get('https://cedia.net/find-a-cedia-integrator/')
page = DealerPage(chrome)



country_name = 'USA'
zipcode = '0'
radius= '25 Miles'

message = '\nScraping Cedia.org please wait....\n'

print(message)

#enter information
page.select_country(country_name)
page.zipcode_search(zipcode)
page.select_radius(radius)

#wait before hitting submit


#search
page.click_search_button()

time.sleep(3)



links = page.count_links()
chrome.close()
print('\nNow visiting individual dealer pages....\n')







