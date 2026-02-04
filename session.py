import os
from dotenv import load_dotenv
from selenium import webdriver
from datetime import datetime as dt
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

load_dotenv()

class Session():

	def __init__(self):

		self.driver = None
	
		self.user_name = os.getenv("ACCOUNT_EMAIL")
		self.password = os.getenv("ACCOUNT_PASSWORD")
		self.site_url = os.getenv("GYM_SITE")

		self.navigate_to_website()

		self.wait = WebDriverWait(self.driver, timeout=5)


	def navigate_to_website(self):
		chrome_options = webdriver.ChromeOptions()

		chrome_options.add_experimental_option("detach", True)

		# Directory where user's profile is saved everytime the browser is closed
		user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
		chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

		self.driver = webdriver.Chrome(options = chrome_options)	

		self.driver.get(self.site_url)	
	
	def login_to_gym_site(self):

		self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Home_heroTitle__o1MWM")))
		login_button = self.driver.find_element(By.ID, value = "login-button")
		login_button.click()

		self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Login_pageTitle__j_4ga")))

		user_name_field = self.driver.find_element(By.ID, value = "email-input")
		password_field = self.driver.find_element(By.ID, value = "password-input")
		login_button = self.driver.find_element(By.ID, value = "submit-button")

		user_name_field.send_keys(self.user_name)
		password_field.send_keys(self.password)
		login_button.click()

	def book_gym_class(self, class_to_book, class_booking_date, class_booking_time):

		selector_class_name_suffix = class_to_book.lower()
		class_time_suffix = class_booking_time.strftime("%H%M")

		try:
			self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Schedule_scheduleTitle__zfZxg")))

			book_class_button = self.driver.find_element(By.ID, value = f"book-button-{selector_class_name_suffix}-{class_booking_date}-{class_time_suffix}")

		except TimeoutException:
			
			titles = self.driver.find_elements(By.XPATH, "//*[starts-with(@id, 'day-title')]")

			for t in titles:
				print(t.get_attribute("id"))
			
			# self.driver.quit()
		except NoSuchElementException:
			print("Sorry! No booking available for this date")
			# self.driver.quit()
		else:
			book_class_button.click()
