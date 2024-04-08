from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def login(driver):
    username = driver.find_element_by_id("login-email")
    username.send_keys("your_username")
    password = driver.find_element_by_id("login-password")
    password.send_keys("your_password")
    driver.find_element_by_id("login-submit").click()

def goto_network(driver):
    # search = driver.find_element(value='global-nav-search').click()
    # click_c = driver.find_element(by =By.CLASS_NAME,value='search-global-typeahead__input')
    # click_c.send_keys("Jaipur Engineering Collage and Research Center")
    # time.sleep(2)
    # click_b = driver.find_element(by=By.XPATH,value="//span[@class='search-global-typeahead-hit__text t-16 t-black']")
    # click_b.click()
    # time.sleep(5)
    # click_b = driver.find_element(by=By.XPATH,value="//button[contains(@class,'artdeco-pill artdeco-pill--slate artdeco-pill--choice artdeco-pill--2 search-reusables__filter-pill-button')][normalize-space()='People']")
    # click_b.click()
    driver.get("https://www.linkedin.com/search/results/people/?keywords=jaipur%20engineering%20collage%20and%20research%20center&origin=SWITCH_SEARCH_VERTICAL&searchId=1da30568-4e9e-40f0-80ef-241b366c6003&sid=x7D")

    time.sleep(5)

  
    connection_action = driver.find_elements(By.CLASS_NAME, 'QwblvjTPjrtIkZBZFEtbcSwAEDbrXqMlxjCNaY')
    for button in connection_action:
        print(button)
        hello=button.find_element(By.XPATH,"//button[@id='ember72']//span[@class='artdeco-button__text'][normalize-space()='Connect']")
        print(hello)
        print('click on button')
        time.sleep(1)
    time.sleep(5)

  

    
    # coordinates = connection.location_once_scrolled_into_view  # returns dict of X, Y coordinates
    # driver.execute_script("window.scrollTo(%s, %s);" % (coordinates['x'], coordinates['y']))
    # time.sleep(5)
    # connection_action.click()
    time.sleep(5)

    # time.sleep(5)
    
    # print('hello')
   
    # time.sleep(2)
    

# def send_requests(driver, n):
#     for i in range(n):
#         pag.click(880, 770)
#     print("Done!")

def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options=options)

    url = "https://www.linkedin.com/login"
    # urlPage ="https://www.linkedin.com/search/results/people/?keywords=jaipur%20engineering%20collage%20and%20research%20center&origin=SWITCH_SEARCH_VERTICAL&searchId=1da30568-4e9e-40f0-80ef-241b366c6003&sid=x7D" 
    driver.get(url)
    # goto_network(driver)
    username= driver.find_element(value="username")
    time.sleep(2)
    print("find something!!")
    username.send_keys('tusharch6577@gmail.com')
    time.sleep(2)
    password = driver.find_element(value="password")
    password.send_keys('65776577')
    time.sleep(1)
    button = driver.find_element(by =By.CLASS_NAME, value='login__form_action_container')
    button.click()
    
    print(driver.title)
    time.sleep(2)
    goto_network(driver)
   

    # tag = driver.find_element(by =By.CLASS_NAME,value="search-reusables__primary-filter"
  
    driver.quit()
if __name__ == '__main__':
    main()