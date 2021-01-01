import time
from selenium import webdriver

url = "https://www.instagram.com/?hl=en"


class InstaFollowers:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:\\Users/DELL/AppData/Local/Google/Chrome/User Data")
        # options.add_argument("headless")
        self.driver = webdriver.Chrome(options=options, executable_path="D:\chromedriver.exe")
        self.driver.get(url)

        time.sleep(2)

        username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        uname = input("Enter Your Username:")
        username.send_keys(uname)

        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        pname = input("Enter Your Password:")
        password.send_keys(pname)

        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()

        try:
            veri = self.driver.find_element_by_xpath('//*[@id="slfErrorAlert"]').text
            print(veri, "and run this program again.")
        except Exception:
            pass

        time.sleep(2)

        print("If You Enable Two Way Authentication Press 1 , And If Not Then Press Any Number")

        choice = int(input("Enter Your Choice:"))
        if choice == 1:
            verification_code = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[1]/div/label/input')
            code_number = int(input("Enter Your Authentication Code:"))
            verification_code.send_keys(code_number)

        else:
            pass
        # Confirm Button click
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/button').click()

        time.sleep(10)
        # For Not Now To submit in instagram
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()

        time.sleep(5)

        try:
            # NoTurn On Notification
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        except Exception:
            pass
        time.sleep(5)

        self.driver.get("https://www.instagram.com/accounts/activity/?followRequests")

        numbers = int(input("Enter How Much You Add Followers:"))
        for i in range(numbers + 1):
            try:
                first_path = '//*[@id="react-root"]/section/main/div/div/div[1]/div/div['
                rest_path = ']/div[3]/div/div[1]/button'
                name_rest_path = ']/div[2]/div/a'
                full_xpath = first_path + str(i) + rest_path
                name_xpath = first_path + str(i) + name_rest_path
                person_name = self.driver.find_element_by_xpath(name_xpath).text
                print("Adding...", person_name)

                self.driver.find_element_by_xpath(full_xpath).click()
            except Exception as e:
                print(e)
                pass


if __name__ == '__main__':
    InstaFollowers()
