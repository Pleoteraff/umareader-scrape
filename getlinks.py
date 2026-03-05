import json
from selenium import webdriver
from selenium.webdriver.common.by import By

links = ["https://umareader.idsmile.xyz/en/character/1001/"]
event_links = []
full_scrape = True
driver = webdriver.Chrome()
extra = ""


def get_links(xpath):
    element_num = 1
    while True:
        story = driver.find_elements(By.XPATH, xpath + '[' + str(element_num) + ']' + extra)
        if len(story) == 1:
            link = story[0].get_attribute("href")
            event_links.append(link)
            element_num +=1
            # print(story[0].text)
        else:
            element_num = 1
            # print("")
            break

# Get Links
if full_scrape:
    driver.get("https://umareader.idsmile.xyz/en/characters")
    get_links("/html/body/div[3]/div/a")
    driver.get("https://umareader.idsmile.xyz/en/cards")
    get_links("/html/body/div[3]/div/a")
    # driver.get("https://umareader.idsmile.xyz/en/events")
    # get_links("/html/body/div[3]/div/a")
    links = event_links
    event_links = []

for i in links:
    driver.get(i)
    extra = ""
    # Character Links
    get_links("/html/body/div[3]/div[3]/a")
    get_links("/html/body/div[3]/div[5]/div/a")
    get_links("/html/body/div[3]/div[6]/div/a")
    get_links("/html/body/div[3]/div[7]/div/a")
    # Card Links
    get_links("/html/body/div[3]/div[4]/div/a")
    get_links("/html/body/div[3]/div[3]/div/a")
    #Event Link
    if "event" in i:
        extra = "/a[1]"
        get_links("/html/body/div[3]/div[1]/div/div")

event_links = list(filter(None,event_links))
with open("links.json", "w") as f:
    json.dump(event_links, f)