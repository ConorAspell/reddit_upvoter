from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.select import Select
import pandas as pd
import time

def make_account():
    url = 'https://old.reddit.com/'
    credentials = pd.read_csv('credentials.csv')
    first_name = df.sample(1).name.tolist()[0].split(' ')[0]
    field['first_name'] = first_name

    second_name = df.sample(1).name.tolist()[0].split(' ')[1]
    field['second_name'] = second_name
    number = max(credentials.number)+1
    field['number'] = number
    email = 'aspellibe+'+str(number)+'@gmail.com'
    field['email'] = email
    password = '4562433Ss'
    field['password'] = password
    team_name = first_name +' ' + second_name + "'s team"
    all_fields.append(field.copy())
    df2  = pd.DataFrame(all_fields)
    credentials = credentials.append(df2)
    credentials.to_csv('credentials.csv', index=False)
    
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(1)
    first_name_box = driver.find_element_by_class_name('first_name')
    second_name_box = driver.find_element_by_class_name('last_name')
    first_email_box = driver.find_element_by_class_name('email')
    second_email_box = driver.find_element_by_class_name('confirm_email')
    password_box = driver.find_element_by_class_name('password')
    second_password_box =driver.find_element_by_class_name('passwordConfirm')
    fantasy_team_box = driver.find_element_by_xpath('//*[@id="c64_team_name"]')
    terms_and_conditions = driver.find_element_by_xpath('//*[@id="c64_terms"]')
    continue_button = driver.find_element_by_xpath('//*[@id="js-submit-step"]')

    first_name_box.send_keys(first_name)
    second_name_box.send_keys(second_name)
    first_email_box.send_keys(email)
    second_email_box.send_keys(email)
    password_box.send_keys(password)
    second_password_box.send_keys(password)
    fantasy_team_box.send_keys(team_name)
    y = terms_and_conditions.location['y']
    x = terms_and_conditions.location['x']
    driver.execute_script('window.scrollTo('+str(x)+', '+str(y) +')')
    action = ActionChains(driver)
    driver.execute_script("document.getElementById('c64_terms').click()")
    print(terms_and_conditions.get_attribute("type"))
    continue_button.click()
    return driver

def upvote_account(account_name, driver):
    driver.get("https://old.reddit.com/")
    driver.get("https://old.reddit.com//u/"+account_name)
    while True:
        upvotes = driver.find_elements_by_css_selector("div.arrow.up")
        if len(upvotes) == 0:
            break
        for vote in upvotes:
            vote.click()
        next_button = driver.find_element_by_xpath('//*[@id="siteTable"]/div[51]/span/span/a')
        next_button.click()

def upvote_post(driver):
    url='https://old.reddit.com/r/leagueoflegends/comments/gyffy2/lols_mandela_effect_green_item_that_made_you/'
    driver.get(url)
    vote = driver.find_element_by_css_selector("div.arrow.up")
    vote.click()

def sign_in():
    credentials = pd.read_csv('credentials.csv')
    for x in credentials.iterrows():
        url = "https://www.reddit.com/login/"
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        #chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options,executable_path='/Users/caspell/Downloads/chromedriver')
        driver.get(url)
        username = driver.find_element_by_id("loginUsername")
        password = driver.find_element_by_id('loginPassword')
        name = x[1]['name']
        username.send_keys(name)
        password_ = x[1]['password']
        password.send_keys(password_)
        log_in = driver.find_element_by_class_name('AnimatedForm__submitButton')
        log_in.click()
        time.sleep(3)
        upvote_post(driver)
        upvote_account("concueta", driver)



sign_in()

make_account()