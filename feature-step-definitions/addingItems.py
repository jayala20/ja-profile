from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from behave import *
#
# @Given('^I am on the Amazon homepage')
# def i_am_on_the_amazon_homepage():
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://www.Amazon.com")
sleep(2)

#
# @And('^I search for any item')
# def i_search_for_any_item():
search_text_box = driver.find_element_by_css_selector("#twotabsearchtextbox")
sleep(1)
search_text_box.send_keys("coffee")
search_text_box.send_keys(Keys.ENTER)
# search_submit_button = driver.find_element_by_css_selector("#nav-search span.nav-sprite")


# @And('^I add to my cart')
# def i_add_to_my_cart():
item = driver.find_element_by_css_selector("div#search div:nth-child(3) > div > span div:nth-child(3) a").click()
sleep(2)
cart_button = driver.find_element_by_css_selector("#a-autoid-20 > span").click()


# @When('^I navigate to my cart')
# def i_navigate_to_my_cart():
sleep(3)
nav_cart = driver.find_element_by_css_selector("a#nav-cart").click()


# @Then('^I see the correct item in my car')
# def i_see_the_correct_item_in_my_car():
item_validation= "AmazonFresh Colombia Ground Coffee, Medium Roast, 12 Ounce"
if item_validation!=item_validation:
    print("Item has different text, check")
else:
    print("Item is correct")
driver.quit()
