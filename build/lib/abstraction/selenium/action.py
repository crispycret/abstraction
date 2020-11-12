import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions



def isEqual(elem, _type):
    return elem == _type


def WaitForElement(handler, xpath, timeout=7):
    
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)        
    
    element = WebDriverWait(handler, timeout, ignored_exceptions=ignored_exceptions)\
        .until(expected_conditions.presence_of_element_located((By.XPATH, xpath))) 




# An action is every change and event that happens in a process. 
class Action(object):
    def __init__(self, name="Action", handler=None):
        self.name = name
        self.handler = handler
        
    # Does nothing
    def invoke(self): pass

    def FromHandler_FindIFrame(self):
        return self.handler.driver.find_elements_by_xpath("//iframe")[0]
    
    def FromHandler_FindElement(self, xpath): 
        return self.handler.driver.find_element_by_xpath(xpath)
        
    def FromHandler_FindElements(self, xpath): 
        return self.handler.driver.find_elements_by_xpath(xpath)
    
    def FromHandler_FindElementAttribute(self, xpath, attribute):
        return self.FromHandler_FindElement(xpath).get_attribute(attribute)
        
        
    # Abstract method, given a function and its parameters call it inside of a try excpet block, return the results
    def TRY(self, func, verbose=True, *args, **kwargs):
        if (verbose): print("[!] -- TRY - %s()" % (func.__name__), ', '.join(args))
        results = None        
        try:
            results = func(*args, **kwargs)
            if (verbose): print(results)            
        except Exception as e: 
            if (verbose): print ('error', e)
            return None
        return results
        
    # Same concept as the TRY() method but loops over a number of times upon errors and returns results immeditaley if successful.
    def TRY_LOOP(self, func, times=3, verbose=True, *args, **kwargs):
        results = None
        while (times > 0):    
            if (verbose): print("[!] -- TRY_LOOP %d - %s()" % (times, func.__name__), ', '.join(args))
            try:
                times = 0
                results = func(*args, **kwargs)    
     
            except Exception as e: 
                times -= 1
                if (verbose): print ('error', e)
        return results

        
    def TRY_FINDING_ELEMENT(self, path, verbose=True):
        return self.TRY(self.FromHandler_FindElement, verbose, path)

    def TRY_FINDING_ELEMENT_LOOP(self, path, times=3, verbose=True):
        return self.TRY_LOOP(self.FromHandler_FindElement, times, verbose, path)

    def TRY_FINDING_ELEMENT_ATTRIBUTE(self, path, attribute, verbose=True):
        return self.TRY(self.FromHandler_FindElementAttribute, verbose, path, attribute)
    

        
    def TRY_FINDING_ELEMENTS(self, path, verbose=True):
        return self.TRY(self.FromHandler_FindElements, verbose, path)

    def TRY_FINDING_ELEMENTS_LOOP(self, path, times=3, verbose=True):
        return self.TRY_LOOP(self.FromHandler_FindElements, times, verbose, path)

    
    
    



