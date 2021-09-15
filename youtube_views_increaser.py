import time
from IPython.display import clear_output
import random
header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
from webdriver_manager.chrome import ChromeDriverManager

for i in range(1,100):
    driver = webdriver.Chrome(executable_path="./drivers/chromedriver")
    driver.get("https://www.youtube.com/watch?v=xncym6xdleg")
    timeDelay = random.randrange(0, 5)
    time.sleep(timeDelay) 