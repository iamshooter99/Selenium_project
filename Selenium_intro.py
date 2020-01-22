import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class PostTest(unittest.TestCase):
	def setUp(self):
		time.sleep(5)
	def testUrlAccess(self):
		driver.get("http://www.atg.party/article/")
	def testTitle(self):
		driver.find_element(By.NAME,"title").send_keys("ATG Title By Tarun")
	def testDescription(self):
		driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[3]/div/form/div[2]/div/div[2]/div").send_keys("Hello this is my first test case")
	def testUploadImage(self):
		driver.find_element_by_name("profile_pic").send_keys("/home/slappy/Desktop/imageTest.png")
		#driver.find_element_by_id("featurebutton").click()


if __name__=="__main__":
	binary =FirefoxBinary('/etc/firefox/firefox')
	driver=webdriver.Firefox(firefox_binary=binary)
	driver.get("http://www.atg.party/")
	print("Opening the Url")
	driver.find_element_by_xpath("/html/body/header/div[1]/div[2]/div/ul/li[2]/a").click()
	print("Click on Login")
	driver.find_element_by_name("email").send_keys("wiz_saurabh@rediffmail.com")
	driver.find_element_by_name("password").send_keys("Pass@123")
	print("Login Id and PassWord Entered")
	driver.find_element_by_xpath("/html/body/header/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/form/div[3]/button").click()
	print("button Clicked")

	time.sleep(5)
	driver.get("http://www.atg.party/article/")
	print("Opening the Url")
	driver.find_element(By.NAME,"title").send_keys("ATG Title By Tarun")
	print("Title Entered")
	driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[3]/div/form/div[2]/div/div[2]/div").send_keys("Hello this is my first test case")
	print("Description Entered")
	driver.find_element_by_name("profile_pic").send_keys("/home/slappy/Desktop/imageTest.png")
	print("Image Uploaded")
	driver.find_element_by_id("featurebutton").click()
	print("Published")
	time.sleep(5)
	#driver.close()


	#unittest.main()


