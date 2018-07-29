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
    
    def __init__(self, site_url, state_list):
        self.site_url = 'https://www.autismspeaks.org/resource-guide/state/'
        self.state_list = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    
    """
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
            