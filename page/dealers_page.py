from selenium import webdriver
from selenium.webdriver.support.ui import Select


from locators.dealers_page_locators import DealersPageLocators
from locators.dealers_information_locators import DealerInformation
from parsers.parsers import PageParser

'''
This program wil.
'''

class DealerPage:
    def __init__(self, browser):
        self.browser = browser


    @property
    def country_dropdown(self):
        element = self.browser.find_element_by_css_selector(DealersPageLocators.COUNTRY)
        return Select(element)

    def select_country(self, country_name: str):
        self.country_dropdown.select_by_visible_text(country_name)


    def zipcode_search(self, number):
        element = self.browser.find_element_by_css_selector(DealersPageLocators.ZIPCODE)
        element.send_keys(number)

    @property
    def radius_dropdown(self):
        element = self.browser.find_element_by_css_selector(DealersPageLocators.RADIUS)
        return Select(element)

    def select_radius(self, radius: str):
        self.radius_dropdown.select_by_visible_text(radius)

    def click_search_button(self):
        element=self.browser.find_element_by_css_selector(DealersPageLocators.SEARCH_BUTTON)
        element.click()


    def count_links(self):
        links = []
        boxes = self.browser.find_elements_by_css_selector(DealersPageLocators.DEALER_CONTAINERS)
        length = len(boxes)
        for i in range(length):
            container = self.browser.find_element_by_css_selector(f'a#subMainContent_CompaniesGrid_rptResult_HyperLink1_{i}')
            link = container.get_attribute('href')
            links.append(link)
        return links













