from selenium import webdriver
from locators.dealers_information_locators import DealerInformation




class PageParser:
    def __init__(self, parent):
        self.parent = parent


    @property
    def extract_dealer_info(self):
        dealer_name = self.parent.find_element_by_css_selector(DealerInformation.DEALER_NAME).text
        address = self.parent.find_element_by_css_selector(DealerInformation.ADDRESS_LINE).text
        city = self.parent.find_element_by_css_selector(DealerInformation.ADDRESS_CITY).text
        site = self.parent.find_element_by_css_selector(DealerInformation.DEALER_WEBSITE)
        website = site.get_attribute('href')
        dealer = [dealer_name, address, city, website]
        return dealer


