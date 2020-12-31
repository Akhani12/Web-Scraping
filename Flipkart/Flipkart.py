import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class flipkart:
    def __init__(self):

        # I Used Here Default Chrome Reduce To Over And Over Login...
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:\\Users/DELL/AppData/Local/Google/Chrome/User Data")
        self.driver = webdriver.Chrome(options=options, executable_path="D:\chromedriver.exe")
        url = "https://www.flipkart.com/"
        self.driver.get(url)

        # Close Login Tab...
        try:
            self.driver.find_element_by_class_name('_2KpZ6l._2doB4z').click()
        except Exception:
            pass

        # Enter Keyword Which User Wants...
        search_bar = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
        key_word = input("Which Data You Need:")

        search_bar.send_keys(key_word)
        search_bar.send_keys(Keys.ENTER)

        time.sleep(2)

        pages_finder = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div[2]/div[1]/div[2]/div[26]/div/div/span[1]').text
        total_page = int(pages_finder.split(' ')[-1])
        current_page = 1

        content_list = []

        for x in range(current_page, total_page + 1):
            print("Current Page:", x)
            if x != current_page:
                next_finder = self.driver.find_elements(By.CLASS_NAME, '_1LKTO3')
                next_finder = next_finder[-1].text

                if next_finder.lower() == 'next':
                    self.driver.find_element_by_class_name('_1LKTO3').click()

                    time.sleep(2)

            for i in range(2, 26):
                x_path = '//*[@id="container"]/div/div[3]/div[2]/div[1]/div[2]/div['
                title_xpath = ']/div/div/div/a/div[2]/div[1]/div[1]'
                image_xpath = ']/div/div/div/a/div[1]/div[1]/div/div/img'
                price_xpath = ']/div/div/div/a/div[2]/div[2]/div[1]/div/div[1]'
                list_price_xpath = ']/div/div/div/a/div[2]/div[2]/div[1]/div/div[2]'
                offer_xpath = ']/div/div/div/a/div[2]/div[2]/div[1]/div/div[3]/span'
                review_xpath = ']/div/div/div/a/div[2]/div[1]/div[2]/span[2]/span/span[3]'

                title_full_path = x_path + str(i) + title_xpath
                image_full_path = x_path + str(i) + image_xpath
                price_full_path = x_path + str(i) + price_xpath
                list_price_full_xpath = x_path + str(i) + list_price_xpath
                offer_full_path = x_path + str(i) + offer_xpath
                review_full_path = x_path + str(i) + review_xpath

                # This Is For Product Url..
                try:
                    self.driver.find_element_by_xpath(title_full_path).click()
                    time.sleep(0.5)
                    self.driver.switch_to.window(self.driver.window_handles[-1])

                    product_url = str(self.driver.current_url)

                    self.driver.close()

                    self.driver.switch_to.window(self.driver.window_handles[0])
                except Exception:
                    product_url = None
                    pass
                content_list.append(product_url)

                # This Is For Product Title...
                try:
                    product_title = self.driver.find_element_by_xpath(title_full_path).text
                except Exception:
                    product_title = None
                    pass
                content_list.append(product_title)

                # This Is For Product Image...
                try:
                    p_image = self.driver.find_element_by_xpath(image_full_path)
                    product_image = str(p_image.get_attribute('src'))
                except Exception:
                    product_image = None
                    pass
                content_list.append(product_image)

                # This Is For Product Original Price...
                try:
                    product_price = self.driver.find_element_by_xpath(price_full_path).text
                except Exception:
                    product_price = None
                    pass
                content_list.append(product_price)

                # This Is For Product List Price...
                try:
                    product_list_price = self.driver.find_element_by_xpath(list_price_full_xpath).text
                except Exception:
                    product_list_price = None
                    pass
                content_list.append(product_list_price)

                # This Is For Product Reviews...
                try:
                    product_review = self.driver.find_element_by_xpath(review_full_path).text
                except Exception:
                    product_review = None
                    pass
                content_list.append(product_review)

                # This Is For Product Rating...
                try:
                    product_rating = self.driver.find_element_by_xpath(
                        '/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[' + str(
                            i) + ']/div/div/div/a/div[2]/div[1]/div[2]/span[1]/div').text
                except Exception:
                    product_rating = None
                    pass
                content_list.append(product_rating)

                # This is For Product Offer...
                try:
                    product_offer = self.driver.find_element_by_xpath(offer_full_path).text
                except Exception:
                    product_offer = None

                    pass
                content_list.append(product_offer)

                with open(r'flipkart.csv', 'a', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(content_list)
                content_list.clear()
                print("Completed:", i)


if __name__ == '__main__':
    flipkart()
