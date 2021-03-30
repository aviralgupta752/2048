import webbrowser,sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = "/home/avi/Downloads/chromedriver"
browser = webdriver.Chrome(executable_path = driver)
# browser=webdriver.Chrome()
browser.get("https://gabrielecirulli.github.io/2048/")
e = browser.find_element_by_tag_name('html')
i=0
while(True):
	if(i==0):
		e = browser.find_element_by_tag_name('html')
	e.send_keys(Keys.UP)
	e.send_keys(Keys.RIGHT)
	e.send_keys(Keys.LEFT)
	e.send_keys(Keys.DOWN)
	i+=1

	if(i==100):
		i=0
		e=browser.find_element_by_link_text('Try again')
		e.click()







 