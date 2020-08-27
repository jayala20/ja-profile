from selenium import webdriver
from behave import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from time import sleep

# This scenario launches Amazon homepage
# @Given('^I am on the Amazon homepage')
# def i_am_on_the_amazon_homepage():
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://www.Amazon.com")

# This scenario takes user to click on the sign up option
# @And ('^I click on the link')
# def i_click_on_the_create_account_link():
action = ActionChains(driver)
sign_in_menu = driver.find_element_by_css_selector("#nav-link-accountList")
action.move_to_element(sign_in_menu).perform()
sign_in_sub_menu = driver.find_element_by_css_selector(".nav_pop_new_cust > a")
sign_in_sub_menu.click()

# A variable for the create account module is created to find the specified element selector
# @And ('^I am on the (\d+) page')
# def i_am_on_the_create_account_page():
driver.implicitly_wait(4)
create_account_module_title = driver.find_element_by_css_selector("h1.a-spacing-small")

# Send keys function is used to fill in user information into each field specified
# @And ('^I enter valid user information')
# def i_enter_valid_user_information():
name_field = driver.find_element_by_css_selector("#ap_customer_name")
name_field.send_keys("Flor Ayala")
# driver.execute_script("window.open('https://temp-mail.org/en/', 'new window')")
# print("Opened email generator in new tab")
# driver.implicitly_wait(10)
# copy_button = driver.find_element_by_css_selector("#click-to-copy")
email_field = driver.find_element_by_css_selector("#ap_email")
email_field.send_keys("rofofon813@synevde.com")
email_field.send_keys(Keys.TAB)
pwd_field = driver.find_element_by_css_selector("#ap_password")
pwd_field.send_keys("testing0123")
pwd_field.send_keys(Keys.TAB)
re_enter_pwd_field = driver.find_element_by_css_selector("#ap_password_check")
re_enter_pwd_field.send_keys("testing0123")
re_enter_pwd_field.send_keys(Keys.TAB)

# A variable is created for the Create Your Account button for the driver to click on upon specifying the element selector
# @When ('^I click on Create Your Amazon Account')
# def i_click_on_create_your_amazon_account_button():
create_account_button = driver.find_element_by_css_selector("#continue")
create_account_button.click()
driver.quit()
