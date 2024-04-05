import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# maximum amount of connection requests
MAX_CONNECTIONS = 10
# time in ms to wait before requesting to connect
WAIT_TO_CONNECT = 2000
# time in ms to wait before new employees load after scroll
WAIT_AFTER_SCROLL = 3000
# message to connect (%EMPLOYEE% and %COMPANY% will be replaced with real values)

MESSAGE = f"Subject: Seeking Your Support for a Referral/n\nI hope this message finds you well. I recently came across your profile and was inspired by your work and career path. As a recent graduate eager to kickstart my career, I'm currently seeking opportunities that align with my passion and skills in software development./n\nI understand the value of being referred by someone as esteemed as yourself in the industry and would be grateful if you could consider referring me for any suitable roles within your network or organization./n\nThank you for considering my request. I'm looking forward to any advice or support you can offer./n\nBest regards,/nTushar"
# MESSAGE = f"Subject: Seeking Your Support for a Referral/n
# I hope this message finds you well. I recently came across your profile and was inspired by your work and career path. As a recent graduate eager to kickstart my career, I'm currently seeking opportunities that align with my passion and skills in software development./n
# I understand the value of being referred by someone as esteemed as yourself in the industry and would be grateful if you could consider referring me for any suitable roles within your network or organization./n
# Thank you for considering my request. I'm looking forward to any advice or support you can offer./n
# Best regards,
# Tushar"
# keywords to filter employees in specific positions
POSITION_KEYWORDS = [
    "software",
    "developer",
    "full stack",
    "back end",
    "front end",
]

COMPANY_NAME ='google'


# <--> //

def build_message(employee):
    company = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "org-top-card-summary__title"))
    ).get_attribute("title")

    replacements = {"%COMPANY%": company, "%EMPLOYEE%": employee}
    message = MESSAGE.replace("%EMPLOYEE%", replacements["%EMPLOYEE%"]).replace(
        "%COMPANY%", replacements["%COMPANY%"]
    )

    return message if len(message) <= 300 else ""

def get_button_elements():
    print('get_button 1.1')
    buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, 'artdeco-button__text')
        )

    )
    print("click kar rha h ")
    time.sleep(2)
    buttons[0].click()
    print('get_button 1.2')
    return [
        buttons
        # for button in buttons
        # if any(
        #     keyword.lower() in button.find_element(by= By.XPATH,value="..").text.lower()
        #     for keyword in POSITION_KEYWORDS
        # )
    ]
    

def fill_message_and_connect():
    employee = driver.find_element(by=By.ID,value="send-invite-modal").text.split(" ")[1]
    driver.find_element(By.ID,"custom-message").send_keys(build_message(employee))
    driver.find_element(by=By.XPATH,value="//button[contains(text(), 'Connect')]").click()
    print(f"🤝 Requested connection to {employee}")

def connect(button):
    print('enter into connect ')
    time.sleep(WAIT_TO_CONNECT / 1000)
    print(button)
    button.click()
    fill_message_and_connect()

def get_connect_buttons():
    while True:
        buttons = get_button_elements()
        print("buttons aa gye!!")
        # print(buttons)
        print(1.1)
        return buttons
        # if not buttons:
        #     break
        # for button in buttons:
        #     print('aa gya ander')
        #     yield button
        # load_more_buttons()

def load_more_buttons():
    print("⏬ Scrolling..")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(WAIT_AFTER_SCROLL / 1000)

# <--> //

print("⏳ Started connecting, please wait.")
driver = webdriver.Chrome()
url = "https://www.linkedin.com/login"
driver.get(url)
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

driver.get(f"https://www.linkedin.com/company/{COMPANY_NAME}/people/")

try:
    connections = 0
    totalButton = get_connect_buttons()
    print("1.2")
    print(totalButton.count)
    for button in totalButton:

        if connections >= MAX_CONNECTIONS:
            break
        connect(button)
        connections += 1
    print(
        f"✅ Done! Successfully requested connection to {connections} people."
    )
except Exception as e:
    print(
        f"⛔ Whoops, looks like something went wrong. \
		Please go to https://github.com/mariiio/linkedin_connect and follow the instructions."
    )
    print(e)

driver.quit()