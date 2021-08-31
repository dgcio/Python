# Import the module that will allow you to use Selenium
from selenium import webdriver

# Import the module that will allow you to use the up, down, left, and right keys on your keyboard
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def play2048( times ):
    #1
    driver = webdriver.Firefox()
    driver.get('https://gabrielecirulli.github.io/2048/')

    tag = driver.find_element_by_tag_name("html")

    #2, 3
    for i in range(times):
        ActionChains(driver)\
            .send_keys_to_element(tag, Keys.ARROW_UP, Keys.ARROW_RIGHT, Keys.ARROW_DOWN, Keys.ARROW_LEFT).perform()


    final_score =  driver.find_element_by_class_name("score-container").text.split()
    #4
    print("Final Score: " + final_score[0])

    # 1. opens a game of 2048 from the URL: https://gabrielecirulli.github.io/2048/

    # 2. uses the parameter 'times' to determine how many times your code will try to play the game

    # 3. for each 'time', press these keys in this order: UP, RIGHT, DOWN, LEFT

    # 4. print the final score after all tries to the screen
    