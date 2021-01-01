from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")


driver.get('https://www.linkedin.com')

username = driver.find_element_by_xpath('//*[@id="session_key"]')
username.send_keys('hthakkar657@gmail.com')

password = driver.find_element_by_xpath('//*[@id="session_password"]')
password.send_keys('Aa1@Bb2#')

log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')
log_in_button.click()

# Search By Specified Person...
driver.get("https://www.linkedin.com/in/shaneemoret/")


s = BeautifulSoup(driver.page_source, "html.parser")
person = s.find('li',{'class':'inline t-24 t-black t-normal break-words'})
person_name = person.text
print(person_name)


bio = s.find('h2',{'class':'mt1 t-18 t-black t-normal break-words'})
bio_name = bio.text
print(bio_name)

location = s.find('li',{'class':'t-16 t-black t-normal inline-block'})
location_name = location.text
print(location_name)

college = s.find('span',{'class':'text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view'})
college_name = college.text
print(college_name)

print("Name:",person_name,"Company:",bio_name,"Location:",location_name,"College:",college_name)



