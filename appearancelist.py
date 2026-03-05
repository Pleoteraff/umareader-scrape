import json
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
with open("links.json", "r") as f:
    links = json.load(f)
driver = webdriver.Chrome()
element_num = 1
names = []
# links = ['https://umareader.idsmile.xyz/en/transcript/501004303?characterId=1004&storyType=career']

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Event Title", "Appearances"])

for i in links:
    driver.get(i)

    while len(driver.find_elements(By.XPATH, '//*[@id="dialogue-1"]/div/div[1]')) == 0:
        time.sleep(0.05)
    title = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]').text
    print(title)

    while True:
        bubble = driver.find_elements(By.XPATH, '//*[@id="dialogue-' + str(element_num) + '"]/div/div[1]')
        if len(bubble) == 1:
            if bubble[0].rect['height'] == 40:
                name = bubble[0].text
                names.append(name)
                # print(name)
            element_num +=1
        else:
            element_num = 1
            break
    names = list(set(names))
    names.sort()
    names = ", ".join(names)
    print(names)
    with open('data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([title.encode('utf-8'), names.encode('utf-8')])
    names = []