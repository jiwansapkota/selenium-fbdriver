from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json

import constant
import time
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})


PATH= '/home/jiwan/Documents/chromedriver'
driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)


def delay( timeValue):
    time.sleep(timeValue)

links = [
    'https://www.facebook.com/photo?fbid=2492985161007026&set=a.1376703995968487',
    'https://www.facebook.com/photo?fbid=2488418144797061&set=a.1376703995968487',
    'https://www.facebook.com/photo?fbid=2352021528436724&set=a.1376703995968487',
    'https://www.facebook.com/photo?fbid=2167086913596854&set=a.1376703995968487',
    'https://www.facebook.com/photo?fbid=2023711151267765&set=a.1376703995968487'
]


driver.get("https://www.facebook.com/")
driver.maximize_window()

Email="sapkotazeewan13@gmail.com"
mail=driver.find_element_by_xpath('//*[@id="email"]')
mail.send_keys(Email)


pwd=driver.find_element_by_xpath('//*[@id="pass"]')
pwd.send_keys(constant.passd)
pwd.send_keys(Keys.ENTER)

delay(5)
likersData = [] 

for link in links:
    driver.get(links[links.index(link)])
    delay(2)

    #clicking likers using
    # likersSpan = driver.find_elements_by_class_name("oajrlxb2")
    #likersSpan.click()

    #clicked likers count using console
    driver.execute_script('document.getElementsByClassName("oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l gmql0nx0 ce9h75a5 ni8dbmo4 stjgntxs")[0].click()')

    #tried scrolling using scrollintoview
    # driver.execute_script("""
    #     let y = document.getElementsByClassName("nqmvxvec j83agx80 cbu4d94t tvfksri0 aov4n071 bi6gxh9e l9j0dhe7");
    #     console.log(y);
    #     y[y.length-1].scrollIntoView();
    #     """)
    delay(2)
    #scrolled using spacebar
    actions = ActionChains(driver)
    for _ in range(22):
        actions.send_keys(Keys.SPACE).perform()
        time.sleep(1)
        
    #Tried loop controling using spacebar and while loop
    # present=0
    # while True:
    #     print("Entered while loop")
    #     previous=present
    #     delay(1)
    #     present=len(driver.find_elements_by_class_name("ue3kfks5"))
    #     print(present)
    #     if(present==previous):
    #         break

    likers = driver.find_elements_by_class_name("lrazzd5p")

    for liker in likers:
        href = liker.get_attribute('href')
        try:
            if href != None :
                likersData.append({
                    "url": href,
                    "name": liker.text
                })
        except:
            print("here is nothing")


    print(likersData)



    



    # print(likers)

    # driver.get("https://www.twitter.com/")


    



with open('data.json', 'w') as f1:
        json.dump(likersData, f1, ensure_ascii=False, indent = 3)









