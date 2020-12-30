import time
import random
from scrapy import Selector
from selenium import webdriver
import mysql.connector
from selenium.webdriver.common.keys import Keys

k = 348
h = 1
mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password",
    database="dbname"
)
mycursor = mydb.cursor()


class Test:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument("user-data-dir=C:\\Users/DELL/AppData/Local/Google/Chrome/User Data")
        self.driver = webdriver.Chrome(options=options,
                                       executable_path="../ChromeDriver/chromedriver.exe")
        url = "https://www.spotern.com/en/search?mediaType=movie,instagram,tv,video,show&items=spot"

        self.driver.get(url)

        time.sleep(2)
        try:
            self.driver.find_element_by_xpath('//*[@id="pills-signup"]/form/div[7]/button[1]').click()
        except Exception:
            pass

        value_list = []
        try:
            nu = 0
            for j in range(k, 417):
                print("Current Page:",j)
                try:
                    if j != k:
                        try:
                            self.driver.find_element_by_xpath('//*[@id="paginationPage"]').click()
                            self.driver.find_element_by_xpath('//*[@id="paginationPage"]').send_keys(Keys.BACKSPACE)
                            self.driver.find_element_by_xpath('//*[@id="paginationPage"]').send_keys(Keys.BACKSPACE)
                            self.driver.find_element_by_xpath('//*[@id="paginationPage"]').send_keys(Keys.BACKSPACE)

                            self.driver.find_element_by_xpath('//*[@id="paginationPage"]').send_keys(j)

                            self.driver.find_element_by_xpath('//*[@id="paginationPage"]').send_keys(Keys.ENTER)
                        except Exception as e:
                            print(e)
                            pass

                        time.sleep(2)
                        try:
                            self.driver.find_element_by_xpath(
                                '//*[@id="pushWantedModal"]/div/div/div/div/button/span').click()
                        except Exception:
                            pass

                    if nu == 0:
                        nu = 1

                    for i in range(h, 27):
                        try:

                            def main_scrape(body):
                                # Id..
                                n = random.randint(0, 100000)
                                # print(n)
                                value_list.append(n)

                                # Product And Movie Discription...
                                ser = self.driver.find_element_by_xpath('/html/body/div[3]/h1/p').text

                                value_list.append(ser)

                                # Product Name...
                                try:

                                    dfs = Selector(text=body).xpath(
                                        '/html/body/div[3]/div[1]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[3]/a/text()').get()

                                    if dfs is None or len(dfs) <= 1:
                                        dfs = Selector(text=body).xpath(
                                            '/html/body/div[3]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[3]/p[2]/text()').get()
                                        if dfs is None or len(dfs) <= 1:
                                            dfs = Selector(text=body).xpath(
                                                '/html/body/div[3]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[3]/a/text()').get()


                                    value_list.append(dfs)

                                except Exception:
                                    pass

                                # Product Description....
                                try:

                                    pd = Selector(text=body).xpath(
                                        '/html/body/div[3]/div[1]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[3]/p[2]/text()').get()
                                    if pd is None or len(pd) <= 1:
                                        pd = Selector(text=body).xpath(
                                            '/html/body/div[3]/div[1]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[3]/a/text()').get()
                                        if pd is None or len(pd) <= 1:
                                            pd = Selector(text=body).xpath(
                                                '/html/body/div[3]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[3]/p[3]/text()').get()


                                    value_list.append(pd)

                                except Exception as e:
                                    print(e)
                                    pass

                                # price Of Product...
                                try:

                                    pp = Selector(text=body).xpath(
                                        '/html/body/div[3]/div[1]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[3]/p[4]/text()').get()

                                    if pp is None or len(pp) <= 1:
                                        pp = Selector(text=body).xpath(
                                            '/html/body/div[3]/div[1]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[3]/p[3]/text()').get()

                                        if pp is None or len(pp) <= 1:
                                            pp = Selector(text=body).xpath(
                                                '/html/body/div[3]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/p[4]/text()').get()



                                    value_list.append(pp)

                                except Exception:
                                    pass

                                # Movie Name..
                                try:

                                    pm = Selector(text=body).xpath(
                                        '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div[1]/a/text()').get()
                                    if pm is None or len(pm) <= 1:
                                        pm = Selector(text=body).xpath(
                                            '/html/body/div[3]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div[1]/a/text()').get()

                                        if pm is None or len(pm) <= 1:
                                            pm = Selector(text=body).xpath(
                                                '/html/body/div[3]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div[1]/a/text()').get()



                                    value_list.append(pm)

                                except Exception:
                                    pass

                                # Celebrity...
                                try:

                                    pc = Selector(text=body).xpath(
                                        '/html/body/div[3]/div[2]/div[1]/div[3]/div[2]/div/div/div[3]/div[1]/a/text()').get()

                                    if pc is None or len(pc) <= 1:
                                        pc = Selector(text=body).xpath(
                                            '/html/body/div[3]/div[1]/div[1]/div[3]/div[2]/div/div/div[3]/div[1]/a/text()').get()



                                    value_list.append(pc)

                                except Exception:
                                    pass

                                # Media type
                                try:


                                    pme = Selector(text=body).xpath(
                                        "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div[1]/p/text()").get()

                                    if pme is None or len(pme) <= 1:
                                        pme = Selector(text=body).xpath(
                                            "/html/body/div[3]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div[1]/p/text()").get()
                                    pme = pme.strip()


                                    value_list.append(pme)

                                except Exception as e:
                                    print(e)
                                    pass

                                # Episode..
                                try:

                                    pe = self.driver.find_element_by_xpath(
                                        "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div[1]/p/span").text

                                    value_list.append(pe)

                                except Exception:
                                    pe = None
                                    value_list.append(pe)
                                    pass

                                # For Image...
                                # 1st Image..
                                try:
                                    try:

                                        pi0 = self.driver.find_element_by_xpath(
                                            "/html/body/div[3]/div[2]/div[1]/div[1]/div[1]/div/img")
                                    except Exception:
                                        try:
                                            pi0 = self.driver.find_element_by_xpath(
                                                "/html/body/div[3]/div[1]/div[1]/div[1]/div[1]/div/img")
                                        except Exception:
                                            try:
                                                pi0 = self.driver.find_element_by_xpath(
                                                    "/html/body/div[3]/div[1]/div[1]/div[1]/img")
                                            except Exception:
                                                pi0 = self.driver.find_element_by_xpath(
                                                    "/html/body/div[3]/div[2]/div[1]/div[1]/img")


                                    img1 = pi0.get_attribute("src")

                                    value_list.append(img1)
                                except Exception:
                                    pass

                                # 2nd Image..
                                try:
                                    try:
                                        pi1 = self.driver.find_element_by_xpath(
                                            "/html/body/div[3]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[1]")
                                    except Exception:
                                        pi1 = self.driver.find_element_by_xpath(
                                            "/html/body/div[3]/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]")

                                    img2 = pi1.get_attribute("data-bg")
                                    img2 = img2.lstrip("url(")
                                    img2 = img2.rstrip(")")

                                    value_list.append(img2)

                                except Exception:
                                    pass

                                try:
                                    try:
                                        pb = self.driver.find_element_by_xpath(
                                            "/html/body/div[3]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/a[1]")
                                    except Exception:
                                        try:
                                            pb = self.driver.find_element_by_xpath(
                                                "/html/body/div[3]/div[1]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/a[1]")
                                        except Exception:
                                            pb = self.driver.find_element_by_xpath(
                                                "/html/body/div[3]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/a[1]")


                                    buyp = pb.get_attribute("href")

                                    value_list.append(buyp)
                                except Exception:
                                    pass
                                print(value_list)
                                try:
                                    sql = "INSERT INTO products (id, description ,product , productdisc, price, movie , celebrity ,media, episode , image1, image2,buy) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
                                    val = (tuple(value_list))
                                    mycursor.execute(sql, val)
                                    time.sleep(1)
                                    mydb.commit()
                                except Exception as e:
                                    print(e)
                                    pass


                                time.sleep(2)
                                self.driver.back()
                                time.sleep(2)
                                value_list.clear()

                            xpath = '//*[@id="listDesktop"]/div[' + str(i) + ']/a'
                            print("product", i)
                            self.driver.find_element_by_xpath(xpath).click()

                            time.sleep(2)
                            st = self.driver.page_source
                            main_scrape(st)

                        except Exception:
                            pass
                except Exception:
                    pass
                with open("Sportern.txt", "a+") as f:
                    f.writelines(" " + str(j))
                time.sleep(2)
        except Exception as e:
            print(e)
            pass

if __name__ == '__main__':
    Test()
