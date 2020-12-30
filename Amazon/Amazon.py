import time

from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument("user-data-dir=C:\\Users/DELL/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(options=options,
                          executable_path="D:\chromedriver.exe")

url = "https://www.amazon.in/?ext_vrnc=hi&tag=googhydrabk-21&ascsubtag=_k_Cj0KCQiAtqL-BRC0ARIsAF4K3WGnhNt1Cl6CAVQkzheMhtGyo2XhYwPYOzhXz_1DuLEIS0IlbosVez8aAmENEALw_wcB_k_&ext_vrnc=hi&gclid=Cj0KCQiAtqL-BRC0ARIsAF4K3WGnhNt1Cl6CAVQkzheMhtGyo2XhYwPYOzhXz_1DuLEIS0IlbosVez8aAmENEALw_wcB"
driver.get(url)

# Search Url..
search_url = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')

# Keyword You Want To Search...
search_url.send_keys("mobile")

# Search Button Press...
driver.find_element_by_xpath('//*[@id="nav-search-submit-text"]/input').click()
time.sleep(1)
x = 1
for j in range(x, 10):

    if j == 3:
        sed = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[19]/span/div/div/ul/li[4]/a')
        sed.click()
        time.sleep(2)
    elif j != x:
        sed = driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[2]/div[20]/span/div/div/ul/li[3]/a')
        sed.click()
        time.sleep(2)

    for i in range(2, 21):
        default_xpath = "/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[2]/div["
        full_xpath = default_xpath + "2]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span"
        try:

            if i == 2:
                data = driver.find_element_by_xpath(
                    full_xpath)
                dt = data.text
                print(dt)
                with open("amazon-mobile.txt",'a+') as fp:
                    fp.write("\n"+dt)
                time.sleep(1)

            else:
                data_x = driver.find_element_by_xpath(
                    default_xpath + str(i) + "]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span")
                dt = data_x.text
                print("\n",dt)
                with open("amazon-mobile.txt", 'a+') as fp:
                    fp.write("\n"+dt)

                time.sleep(1)
        except Exception:
            pass

