from bs4 import BeautifulSoup
from selenium import webdriver
import requests

class Scraper(object):

    def __init__(self, webdriver='chrome'):
        self.webdriver = webdriver

class AutismSpeaksScraper(Scraper):
    
    def __init__(self, site_url, state_list):
        self.site_url = 'https://www.autismspeaks.org/resource-guide/state/'
        self.state_list = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    
    def process_state_page():
        for state in self.state_list:
            soup = BeautifulSoup(requests.get(self.url + state).content)
            