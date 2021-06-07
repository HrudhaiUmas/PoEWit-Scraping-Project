'''
This file uses the chromedriver to gather data from cedia.org
It returns a list of all the links of the individual dealer pages.
'''

from selenium import webdriver
import time


from page.dealers_page import DealerPage




chrome = webdriver.Chrome(executable_path = '/Users/aidanpak/Compsci/drivers/chromedriver')
chrome.get('https://cedia.net/find-a-cedia-integrator/')
page = DealerPage(chrome)

country_name = input('Enter desired country name. ')
zipcode = input('Enter desired zipcode. ')
radius= input('Enter desired radius. ')

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







