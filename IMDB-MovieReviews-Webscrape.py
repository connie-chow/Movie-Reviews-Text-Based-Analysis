
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import urllib3
import re
import time
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
#driver=webdriver.Chrome(chrome_options=options, executable_path=r'----insert path ----')
#driver = webdriver.Chrome()

driver = webdriver.Edge()
import urllib.request
import pickle
with open("test_movie_list", "rb") as fp:   # Unpickling
	b = pickle.load(fp)

# iterate through each movie
for stuff in b:
	# load the webpage containing the movie reviews
	url = f"https://www.imdb.com/title/{stuff}/reviews/?ref_=tt_ov_rt"
	with urllib.request.urlopen(url, None, 5) as u:
		html = u.read()
		#print(html)

	# convert it into something BeautifulSoup can parse through
	html_soup1 = BeautifulSoup(html, "html.parser")
	driver.get(url)
	# for each movie click load more until the end and get all the reviews for that movie, then parse it
	# click on the load more button X times until the end
	for n in range(5):
		# click on the load more button X times until the end
		#loadMoreButton = driver.find_element(By.ID, "load-more-trigger")
		try:
			#loadMoreButton = driver.find_element("xpath","/html/body/div[2]/div/div[2]/div[3]/div[1]/section/div[2]/div[4]/div/button")
			loadMoreButton = driver.find_element("xpath", "//*[@id='load-more-trigger']")

			#loadMoreButton = driver.find_element(By.CLASS_NAME, "ipl-load-more__button").find_element(By.ID,
		#																							  "load-more-trigger")
			time.sleep(2)
			loadMoreButton.click()
			time.sleep(5)
		except:
			print("exception on driver.find_element()")

	# now parse through the reviews
	review_containers = html_soup1.find_all('div', class_="lister-item-content")
	for container in review_containers:
		try:
			review = container.find('div', class_="text show-more__control").text
		except (AttributeError) as err:
			review = container.find('div', class_="text show-more__control clickable").text
		#reviews.append(review)
		try:
			rating = container.find('span', class_=None).text
		except:
			rating = None
			#ratings.append(rating)
			#j += 1
		#for k in range(0, j):
		#	print("1")
			#review_titles.append(titles[i])
		#try:
		#	for n in range(8):
		#		#loadMoreButton = driver.find_element_by_xpat
		#		loadMoreButton = driver.find_element(By.CLASS_NAME, "ipl-load-more__button").find_element(By.ID, "load-more-trigger")
		#		time.sleep(2)
		#		loadMoreButton.click()
		#		time.sleep(5)
		#		#WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "load-more-trigger")))
		#except TimeoutException:
		#	break
			#while True:
			#	try:
		#			WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "load-more-trigger"))).click()
	#			except TimeoutException:
#					break

driver.quit()
