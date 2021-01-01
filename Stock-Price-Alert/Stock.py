# options.add_argument("--incognito")
# options.add_argument("headless")
import re
import time
from datetime import datetime
import functools
import operator
import psycopg2
from selenium import webdriver
from telethon import TelegramClient

# Website Url....
url = "https://www.google.com/finance#wptab=s:H4sIAAAAAAAAAOPQeMSozC3w8sc9YSmpSWtOXmMU4RJyy8xLzEtO9UnMS8nMSw9ITE_l2cXEHekfGhQfHOLv7B28iJU9DaIGAAUYQO1AAAAA"

# Postgres Parameters...
PGHOST = "localhost"
PGDATABASE = "dbname"
PGUSER = "user"
PGPASSWORD = "pswrd"

# Telegram Parameters...

api_id = int("your id")
api_hash = 'hash id'
client = TelegramClient('+919428940465', api_id, api_hash)
client.connect()

# Postgres Connection...
postgresConnection = psycopg2.connect(database=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST)
postgresConnection.autocommit = True

# Active Cursor...
cursor = postgresConnection.cursor()


# Stock Class...
class Stock():
    def __init__(self):
        options = webdriver.ChromeOptions()
        # Using By Default Browser...
        options.add_argument("user-data-dir=C:\\Users/DELL/AppData/Local/Google/Chrome/User Data")

        # Active Driver...
        self.driver = webdriver.Chrome(options=options, executable_path="E:\chromedriver.exe")
        self.driver.get(url)

        time.sleep(3)
        # While Loop...
        while True:
            # Checking For 4 o'clock...

            start = time.time()
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            # If its a 4 o'clock then loop exists...

            if current_time > "16:00":
                # from termcolor import colored
                # final_data = colored('Closing Price', 'blue', attrs=['bold'])

                cursor.execute("SELECT * FROM stock_data")
                query_results = cursor.fetchall()
                final_data = ''
                for i in query_results:
                    final_data = final_data + "\n\n" + str(i)
                print(final_data)
                async def main():
                    await client.send_message('receiver number or username', final_data)
                    await client.send_message('receiver number or username', final_data)
                with client:
                    client.loop.run_until_complete(main())
                break
            setu = ''
            for i in range(9):
                try:
                    first_path = '//*[@id="knowledge-finance-wholepage__financial-entities-list"]/div['
                    numbers = str(i)
                    name_last_path = ']/message_stag-link/a/div/span[1]'
                    price_last_path = ']/message_stag-link/a/div/span[2]/span[2]/span[1]'

                    # Name Full Path...
                    name_full_xpath = first_path + numbers + name_last_path

                    # Price Full Path...
                    price_full_path = first_path + numbers + price_last_path

                    # Find Text By Xpath...
                    text_abc = self.driver.find_element_by_xpath(name_full_xpath)

                    # Find Price By Xpath...
                    price_abc = self.driver.find_element_by_xpath(price_full_path)

                    # Get Stock Name...
                    stock_name = text_abc.text

                    # Get Stock Price...
                    stock_price = price_abc.text

                    # For Price Treamming...
                    trim = re.compile(r'[,]+')
                    stock_price = float(trim.sub('', stock_price))

                    # Compare Price....
                    cursor.execute("SELECT stock_price FROM stock_data WHERE stock_name = '" + stock_name + "'")
                    query_results = cursor.fetchone()

                    query_results = functools.reduce(operator.add, (query_results))

                    # Cheking If Price Change Or Not...
                    if query_results < stock_price or stock_price < query_results:
                        str_data = stock_name + ':' + str(stock_price) + "\n\n"
                        setu = setu + str_data
                        # Query To Insert Data Into Database...
                        # "UPDATE stock_data SET stock_price =" + str(stock_price) +"WHERE stock_name =" + stock_name
                        query = "UPDATE stock_data SET stock_price =" + str(
                            stock_price) + " WHERE stock_name ='" + stock_name + "'"
                        cursor.execute(query)
                        postgresConnection.commit()

                except Exception:

                    pass

            # Get Final Data From The DataBase...
            # cursor.execute("SELECT * FROM stock_data")
            # query_results = cursor.fetchall()
            #
            # final_data = ''
            # for i in query_results:
            #     final_data = final_data + "\n\n" + str(i)
            # print(final_data)

            # Sending Message From Telegram...
            try:
                async def main():
                    await client.send_message('receiver number or username', setu)
                    await client.send_message('receiver number or username', setu)
                with client:
                    client.loop.run_until_complete(main())



            except Exception:
                pass

            self.driver.refresh()
            end = time.time()

            print(f"Runtime of the program is {end - start}")
            time.sleep(2)


if __name__ == '__main__':
    Stock()
