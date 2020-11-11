import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..models import AbstractObject

### A basic wrapper to selenium for scraping data
## - driver - the selenium web browser driver
## - username - username for login
## - password - password for login
## - url_home - The url to navigate to when the browser is created
## - url_login - The url to use when we login.
## - url_post_login - The url to navigate to after login

## - actions - A list of actions to do at given urls.

## - get_url() - get current url
## - set_url() - Navigate to a new url



         
   
### An abstract wrapper for selenium. 
### This will allow selenium to preform basic actions, 
### for which there is a list that requires some customization, with some basic navigation.
### Because we inherit from AbstractObject this class too can be customized and expanded very easily.
### Adding a key to the _attrs dict will result in a new variable inside the object.
### A named action list will allow functions to be added on the fly even after creation of an object.
class SeleniumHandler(AbstractObject):
    _attrs = {
        'driver':None, # Selenium webdriver
        'username':'', # for login
        'password':'', # for login
        'url_home':'', # The sites home url
        'url_login':'', # The url used to login to the site (sometimes can be the same as home url)
        'url_post_login':'', # The url we want to navigate to after login
        'nav_time':2, # How long we wait after we go to a new url
        'actions':{}, # Custom actions called by controller (scraper.py)
        'is_logged_in': False,
        'login_action_name': 'Login',
    }
    
    def __init__(self, **kwargs):
        for var, val in SeleniumHandler._attrs.items():
            if var not in kwargs:
                kwargs[var] = val
                 
        super(SeleniumHandler, self).__init__(**kwargs)
        if (self.driver):
            self.driver
    
    def add_action(self, action_class):
        action = action_class(self)
        self.actions[action.name] = action
        self.__setattr__(action.name, action)
        print ("[+] ", action_class.__name__)        
        
    def get(self, url):
        if (url == ""): return
        self.driver.get(url)
        time.sleep(self.nav_time)
        
    def home(self):
        self.get(self.url_home)
    
    
    ### Call the login action only if there is one.
    ### We can do this from the home page if this site can login from the home site
    ### Otherwise go to login url if there is one.
    
    def login(self, redirect = True):
        results = None
        if self.login_action_name not in self.actions.keys(): return results
        
        # the action here is the login action. It is an object. We can call action.Login() on it.
        action = self.actions[self.login_action_name]

        # Login if we are at the home page and we can login from the home page
        if self.is_home() and self.can_login_from_home():
                        
            results = action.invoke(post_login_redirect = redirect)
            
        # Otherwise          
        else: 
            self.get(self.url_login)
            results = action.invoke(post_login_redirect = redirect)
            if (results is not None):
                self.is_logged_in = True
            
        return results
        
        
    def is_home(self): return self.current_url == self.url_home
    def current_url(self): return self.driver.current_url
    def can_login_from_home(self): return self.url_home == self.url_login







