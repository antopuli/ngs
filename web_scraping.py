
import logging as LOG
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# logging configuration 

LOG.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=LOG.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

LOGGING = LOG.getLogger(__name__)
LOGGING.setLevel(LOG.DEBUG)


# web driver configuration 

options = Options()
driver = webdriver.Edge(options=options)


# get source 

source = 'https://reteidrometeo.protezionecivile.puglia.it/polarisopen/viewer/report?guest=pubblico'
driver.get(source)
LOGGING.info('Web page accessed successfully.')


# select all stations

station = driver.find_element(
    By.XPATH,
    '/html/body/section/section/div/div/div[1]/h3/a'
)
station.click()
LOGGING.info('Stations acquired successfully.')


# generate table

gen_table = driver.find_element(
    By.XPATH,
    '/html/body/section/section/div/form[2]/div/div[2]/button[1]'
)
gen_table.click()
LOGGING.info('Table created.')


# switch to the other window

driver.switch_to.window(driver.window_handles[1])


# select period

select_period = driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div[1]/form/div/div[1]/div[1]/span/span[1]/span/span[2]'
)
select_period.click()
selected = driver.find_element(
    By.XPATH,
    '/html/body/span/span/span[1]/input'
)
selected.send_keys('Giornaliero')
selected.send_keys(Keys.RETURN)
LOGGING.info('Period successfully selected.')


# refresh data

driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div[1]/form/div/div[1]/div[3]/a'
).click()


# download data

download = driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div[1]/form/div/div[2]/div/button'
)
download.click()

type_csv = driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div[1]/form/div/div[2]/div/ul/li/button[2]'
)
type_csv.click()

LOGGING.info('Data downloaded successfully.')


# quit session

driver.quit()
