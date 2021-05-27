import re

from locators.dealers_information_locators import DealerInformation




class PageParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Company {self.dealer_name}>'


    @property
    def dealer_name(self):
        locator = DealerInformation.DEALER_NAME
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def address_line(self):
        locator = DealerInformation.ADDRESS_LINE
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def address_city(self):
        locator = DealerInformation.ADDRESS_CITY
        return self.parent.find_elements_by_css_selector(locator)

    @property
    def dealer_website(self):
        locator = DealerInformation.DEALER_WEBSITE
        return self.parent.find_elements_by_css_selector(locator)

    @property
    def dealer_description(self):
        locator = DealerInformation.DESCRIPTION
        return self.parent.find_elements_by_css_selector(locator)

    @property
    def return_page(self):
        locator = DealerInformation.RETURN_PAGE
        element = self.parent.find_elements_by_css_selector(locator)
        element.click()




