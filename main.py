from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_web_path = "/home/psingal/Desktop/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_web_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cockie = driver.find_element(By.XPATH, "//*[@id='cookie']")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_id =[item.get_attribute("id") for item in items]
print(item_id)
five_min = time.time() + 5*60
five_sec = time.time() + 5


while five_min > time.time():
    cockie.click()
    if time.time() > five_sec:
        all_price = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_price = []
        for p in all_price:
            price_element = p.text
            if price_element != "":
                price = int(price_element.split("-")[1].strip().replace(",", ""))
                item_price.append(price)
        cockie_upgarde = {}
        for n in range(len(item_price)):
            cockie_upgarde[item_price[n]] = item_id[n]

        cockie_count = driver.find_element(By.ID, "money").text
        if "," in cockie_count :
            cockie_count = cockie_count.replace(",", "")
        cockie_money = int(cockie_count)

        choice_upgrade = {}
        for cost,id in cockie_upgarde.items():
            if cockie_money > cost:
                choice_upgrade[cost] = id

        highest_price = max(choice_upgrade)
        bye_item = choice_upgrade[highest_price]
        driver.find_element(By.ID, bye_item).click()
        five_sec = time.time() + 5
    if time.time() > five_min:
        break


driver.close()

