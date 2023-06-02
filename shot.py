import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)


import warnings
warnings.filterwarnings("ignore")


class Scrapper:
   def pageGet(self, url)->list:
       self._driver.get(url)
       for i in range(10):
           self._driver.save_screenshot("artifacts/image"+str(i)+".png");
           time.sleep(1)
   def close(self):
       self._driver.close()
   def __init__(self):
       self._chrome_options = Options()
       self._chrome_options.add_argument("--headless")
       self._driver = webdriver.Chrome(options=self._chrome_options)

class ScrapperLayer:
   def __exit__(self, exc_type, exc_value, traceback):
       self._scrapper.close()
   def __enter__(self):
       self._scrapper = Scrapper()
       return self._scrapper

with ScrapperLayer() as scrapper:
 
    scrapper.pageGet("file://"+os.getcwd()+sys.argv[1])

