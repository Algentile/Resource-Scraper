from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import re


class Scraper(object):

    def __init__(self, webdriver='chrome'):
        self.webdriver = webdriver

    def convert_to_csv(self, filename, dict):
        df = pd.Dataframe.from_dict(dict, orient='index')
        return df.to_csv(filename + '{}', str(time.ctime()))


"""
Webscraper for autism speaks website
"""
class AutismSpeaksScraper(Scraper):

    def __init__(self):
        self.base_url = 'https://www.autismspeaks.org'
        self.site_url = 'https://www.autismspeaks.org/resource-guide/state/'
        self.state_list = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
                           "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                           "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                           "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                           "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    """
    Scrape for resource links on page and store in a dictionary of 
    hyper link values.

    State (str): The two letter character code for the US state.
    """

    def _process_state_page(self, state):
        href_dict = {}
        content_block = None
        resource_url = self.site_url + state
        soup = BeautifulSoup(requests.get(resource_url).content)
        resource_block = soup.find(
            'div', class_='sharethis').find_next_sibling('ul')

        for tag in resource_block:
            next_tag = tag.find_next_sibling()
            if(tag.name == 'li' and next_tag.name == 'ul'):
                content_block = tag.get_text()
                href_dict[content_block] = []
            if(tag.name == 'ul'):
                for li_tag in tag.findAll('li'):
                    li_tag_content = li_tag.find('a').get('href')
                    self.get_location_info(li_tag_content)
        return href_dict
    
    """
    Grab the location links from the view taxonomy block
    endpoint (str): Endpoint url for veiw taxonomy block by-state info
    """
    def _process_organization_info(self, url):
        organization_list = []
        soup = BeautifulSoup(requests.get(url).content)
        view_taxonomy_block = soup.find('div', class_='view-taxonomy-listing-by-state')

        for tr in view_taxonomy_block.findAll('tr'):
            location_endpoint = tr.find('a').get('href')
            city = tr.find('td', class_='views-field-city') 
            if(city != None and location_endpoint != None):
                organization_list.append((location_endpoint, city.contents[0].strip('\n')))
        return organization_list
    
    """
    TODO: Get Location Data Block
    """
    def get_location_info(self, endpoint):
        location_url = self.base_url + endpoint
        organization_list = self._process_organization_info(location_url)
        for (endpoint, city) in organization_list:
            print(self.base_url + endpoint)
            soup = BeautifulSoup(requests.get(self.base_url + endpoint))
            location_block = soup.find('div', class_='node-content')
            print(location_block)

    """
    Test function for processing single state
    """
    def process_test_page(self):
        return self._process_state_page('AL')
    
    """
    Grab the resource links for each state in
    the state_list supported by Autism Speaks.
    """

    def get_resource_links(self):
        resource_links = {}
        for state in self.state_list:
            href_dict = self._process_state_page(state)
            resource_links[state] = href_dict
            time.sleep(15) #Wait 15 seconds after each process request
        return resource_links


if __name__ == '__main__':
    x = AutismSpeaksScraper()
    href_dict = x.process_test_page()
    
