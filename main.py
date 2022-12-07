import time
import functions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import yaml

# decrypting file
loaded_key = functions.key_load('YOUR_KEY_FILE_NAME.key')
functions.file_decrypt(loaded_key, 'YOUR_CREDENTIALS_FILE.yml', 'YOUR_CREDENTIALS_FILE.yml')

# reading login credentials from yml file, you have to create login and password variables for each site individually
conf = yaml.full_load(open('YOUR_CREDENTIALS_FILE.yml'))
# example
YOUR_SITE_NAME_Email = conf['YOUR_SITE_NAME']['email']
YOUR_SITE_NAME_Password = conf['YOUR_SITE_NAME']['password']

# depending on a site you have to change how different elements are located, example of login function
# where username and password are located by ID but button doesn't have one, so you have to use CLASS_NAME to locate it
def login(url,usernameId, username, passwordId, password, submit_buttonId):
   driver.get(url)
   time.sleep(3)
   driver.find_element(By.ID, usernameId).send_keys(username)
   time.sleep(1)
   driver.find_element(By.ID, passwordId).send_keys(password)
   time.sleep(1)
   driver.find_element(By.CLASS_NAME, submit_buttonId).click()

# using random agent to minimalise probability of bot detection
ua = UserAgent()
userAgent = ua.random
# specifying webdriver options
options = Options()
options.add_experimental_option("detach", True)
options.add_argument(f'user-agent={userAgent}')
# path to your chromium based browser
options.binary_location = "PATH HERE"
driver = webdriver.Chrome(options=options)
# invoking login function
login('LINK TO WEBSITE LOGIN PAGE HERE', 'login', YOUR_SITE_NAME_Email, 'password', YOUR_SITE_NAME_Password, 'CLASS NAME FOR BUTTON')


# encrypting file
functions.file_encrypt(loaded_key, 'YOUR_CREDENTIALS_FILE.yml', 'YOUR_CREDENTIALS_FILE.yml')
