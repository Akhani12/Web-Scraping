# x is for pages
# y is for products

import random
import time
import mysql.connector
from scrapy import Selector
from selenium import webdriver

mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="dbname"
)
mycursor = mydb.cursor()

x = 802
y = 1


class Shopurtv:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        # options.add_argument("user-data-dir=C:\\Users/DELL/AppData/Local/Google/Chrome/User Data")
        self.driver = webdriver.Chrome(options=options,
                                       executable_path="../ChromeDriver/chromedriver.exe")
        url = "https://www.shopyourtv.com/"
        self.driver.get(url)

        # First Click Gone To Project

        # This List Is For Mysql Values....
        value_list = []

        # This Loop Is For Page...
        for i in range(x, 2344):

            # This Is For Pagination Click...
            if i != x:
                bd = self.driver.page_source
                page_link = Selector(text=bd).css('a.alt-font.text-small').xpath('@href').extract()[-1]
                self.driver.get(page_link)
                time.sleep(2)

            print("Page No:", i)
            with open("Completed", 'a+') as fps:
                fps.writelines("\n" + "Page No: " + str(i) + "\n" + "Products: ")

                # This Is For Products...

            for j in range(y, 34):
                try:
                    def sut_main(body):
                        # Id Generator...
                        n = random.randint(0, 1000000)
                        value_list.append(n)

                        try:
                            # Product Whole Description...
                            try:
                                description = self.driver.find_element_by_xpath(
                                    '/html/body/div[4]/section[2]/div/div/div/ul/li[3]/span').text
                              


                            except Exception:
                                description = self.driver.find_element_by_xpath(
                                    '/html/body/div[3]/div/div[2]/section[2]/div/div/div/ul/li[3]/span').text
                            value_list.append(description)


                            "Main Content Which Is Changeable...."
                            try:
                                sd = self.driver.find_element_by_xpath(
                                    '/html/body/div[4]/section[3]/div/div/div/div[2]/div[1]/ul/li[1]/strong').text
                            except Exception:
                                sd = self.driver.find_element_by_xpath(
                                    '/html/body/div[3]/div/div[2]/section[3]/div/div/div/div[2]/div[1]/ul/li[1]/strong').text
                            sd = sd.replace(':', '')
                            cross_text = sd.lower()
                            if cross_text == 'character':
                                l1, l2, l3, l4, l5, l6 = 2, 3, 4, 5, 6, 7
                            elif cross_text == 'actor':
                                l1, l2, l3, l4, l5, l6 = 1, 2, 3, 4, 5, 6
                            else:
                                l1, l2, l3, l4, l5, l6 = 0, 1, 2, 3, 4, 5

                            scx = '/html/body/div[3]/div/div[2]/section[3]/div/div/div/div[2]/div[1]/ul/li['

                            # Actor...

                            pa = Selector(text=body).xpath(
                                '/html/body/div[4]/section[3]/div/div/div/div[2]/div[1]/ul/li[' + str(
                                    l1) + ']/text()').get()
                            if pa is None or len(pa) <= 1:
                                pa = Selector(text=body).xpath(
                                    scx + str(l1) + ']/text()').get()
                            value_list.append(pa)

                            # Show of Product...
                            pm = Selector(text=body).xpath(
                                '/html/body/div[4]/section[3]/div/div/div/div[2]/div[1]/ul/li[' + str(
                                    l2) + ']/text()').get()
                            if pm is None or len(pm) <= 1:
                                pm = Selector(text=body).xpath(
                                    scx + str(l2) + ']/text()').get()
                            value_list.append(pm)

                            # Episode of current product...
                            pe = Selector(text=body).xpath(
                                '/html/body/div[4]/section[3]/div/div/div/div[2]/div[1]/ul/li[' + str(
                                    l3) + ']/text()').get()
                            if pe is None or len(pe) <= 1:
                                pe = Selector(text=body).xpath(
                                    scx + str(l3) + ']/text()').get()
                            value_list.append(pe)

                            # Product Of Brand...
                            pb = Selector(text=body).xpath(
                                '/html/body/div[4]/section[3]/div/div/div/div[2]/div[1]/ul/li[' + str(
                                    l4) + ']/text()').get()
                            if pb is None or len(pb) <= 1:
                                pb = Selector(text=body).xpath(
                                    scx + str(l4) + ']/text()').get()
                            value_list.append(pb)

                            # Buy link...
                            try:
                                buylink = self.driver.find_element_by_xpath(
                                    '/html/body/div[4]/section[3]/div/div/div/div[2]/div[1]/ul/li[' + str(
                                        l5) + ']/p[1]/a')

                                bl = buylink.get_attribute('href')
                            except Exception:
                                try:
                                    buylink = self.driver.find_element_by_xpath(
                                        scx + str(l5) + ']/p[1]/a')
                                    bl = buylink.get_attribute('href')
                                except Exception:
                                    bl = None
                            value_list.append(bl)

                            # Price of product...

                            pp = Selector(text=body).xpath(
                                '/html/body/div[4]/section[3]/div/div/div/div[2]/div[1]/ul/li[' + str(
                                    l5) + ']/p[1]/text()').get()
                            if pp is None or len(pp) <= 1:
                                pp = Selector(text=body).xpath(
                                    '/html/body/div[4]/section[3]/div/div/div/div[2]/div[1]/ul/li[' + str(
                                        l5) + ']/p[1]/span/span').get()
                                if pp is None or len(pp) <= 1:
                                    pp = Selector(text=body).xpath(
                                        '/html/body/div[4]/section[3]/div/div/div/div[2]/div[1]/ul/li[' + str(
                                            l5) + ']/p[1]/text()[2]').get()
                                    if pp is None or len(pp) <= 1:
                                        pp = Selector(text=body).xpath(
                                            '/html/body/div[4]/section[3]/div/div/div/div[2]/div[1]/ul/li[' + str(
                                                l5) + ']/p/text()[1]').get()
                            try:
                                pp = pp.replace('–', '').replace(' ', '')
                            except Exception:
                                pass
                            value_list.append(pp)
                            # Product Description...

                            pd = Selector(text=body).xpath(
                                '/html/body/div[4]/section[3]/div/div/div/div[2]/div[1]/ul/li[' + str(
                                    l6) + ']/text()').get()
                            if pd is None or len(pd) <= 1:
                                pd = Selector(text=body).xpath(scx + str(l6) + ']/text()').get()

                            value_list.append(pd)

                            # Image Of Product...
                            try:
                                pi = self.driver.find_element_by_xpath(
                                    '/html/body/div[4]/section[3]/div/div/div/div[1]/div[1]/img')
                                image = pi.get_attribute('src')
                            except Exception:
                                image = None
                            value_list.append(image)

                            # Insert Data Into Database....

                            sql = "INSERT INTO shopurtv (id, description ,celebrity , movie, episode, brand , buy ,price, productdisc , image1) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            val = (tuple(value_list))
                            mycursor.execute(sql, val)
                            time.sleep(1)
                            mydb.commit()
                        except Exception:
                            # print(e)
                            pass

                        print(value_list)
                        value_list.clear()
                        with open("Completed", 'a+') as dps:
                            dps.writelines(" " + str(j))
                        self.driver.back()
                        time.sleep(2)

                    xpath = "/html/body/section[1]/div/div/div/div[2]/div[1]/div[" + str(j) + "]/div[2]/h2/a"
                    self.driver.find_element_by_xpath(xpath).click()
                    try:
                        self.driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/svg/path[1]').click()

                    except Exception:
                        pass
                    print("Product No:", j)
                    time.sleep(2)
                    body = self.driver.page_source
                    sut_main(body)
                except Exception as e:
                    print(e)
                    value_list.clear()
                    # self.driver.back()
                    # time.sleep(2)
                    pass


if __name__ == '__main__':
    Shopurtv()
