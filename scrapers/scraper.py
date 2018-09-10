from bs4 import BeautifulSoup
import pandas as pd
import requests
import ctime
import re

class Scraper(object):

    def __init__(self, webdriver='chrome'):
        self.webdriver = webdriver

    
    def convert_to_csv(filename, dict):
        df = pd.Dataframe.from_dict(dict, orient='index')
        return df.to_csv(filename + '{}', str(time.ctime()))

class AutismSpeaksScraper(Scraper):
    
    def __init__(self):
        self.site_url = 'https://www.autismspeaks.org/resource-guide/state/'
        self.state_list = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    
    """
<<<<<<< HEAD
    Process resources for each page 
    """
    def process_state_page(self):
        # for state in self.state_list:
        prev_tag = None
        href_dict = {}
        resource_url = self.site_url + 'AL'
        soup = BeautifulSoup(requests.get(resource_url).content)
        resource_block = soup.find('div', class_='sharethis').find_next_sibling('ul')
        for tag in resource_block:
            next_tag = tag.find_next_sibling()
            if(next_tag == 'li' and next_tag.find_next_sibling == 'ul'):
                prev_tag = next_tag
                href_dict[prev_tag] = ''
            elif(tag == 'ul'):
                for li in next_tag:
                    print(li)
                    href_dict[prev_tag] = li
        return href_dict

if __name__ == '__main__':
    x = AutismSpeaksScraper()
    bs4_dict = x.process_state_page()
    print(bs4_dict)
=======
    Converts Resource links to python dictionary of resource links
    """
    def process_state_page(self):
        resource_dict = {}
        for state in self.state_list:
            soup = BeautifulSoup(requests.get(self.site_url + state).content)
            for item in soup.find_all('a'):
                    
                
                
            


if __name__ == '__main__':
    x = AutismSpeaksScraper("", "")
    x.process_state_page()
            
>>>>>>> 7aeb3993ade06aa8f030cbfdbb9ac40bd5279440
