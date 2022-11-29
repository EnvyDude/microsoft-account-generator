from itertools import count
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from faker import Faker
import random
import time
import os
from colorama import Fore
from selenium.webdriver.support import expected_conditions as EC

os.system('cls')

print("[+]Starting Gen!")

def intro():
    os.system('cls')
    os.system('color 4')
    print(""" /$$$$$$$$ /$$$$$$$$  /$$$$$$  /$$      /$$        /$$$$$$  /$$$$$$
|__  $$__/| $$_____/ /$$__  $$| $$$    /$$$       /$$__  $$|_  $$_/
   | $$   | $$      | $$  \ $$| $$$$  /$$$$      | $$  \ $$  | $$  
   | $$   | $$$$$   | $$$$$$$$| $$ $$/$$ $$      | $$$$$$$$  | $$  
   | $$   | $$__/   | $$__  $$| $$  $$$| $$      | $$__  $$  | $$  
   | $$   | $$      | $$  | $$| $$\  $ | $$      | $$  | $$  | $$  
   | $$   | $$$$$$$$| $$  | $$| $$ \/  | $$      | $$  | $$ /$$$$$$
   |__/   |________/|__/  |__/|__/     |__/      |__/  |__/|______/
                                                                   """)
    os.system('color')
    print("Discord: Ai-Phantom#1337")
    print('')


fake = Faker()
def create():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    intro()
    first_name = fake.first_name()
    last_name = fake.last_name()
    random_number = random.randint(1, 1000)
    password = f"{first_name}!{last_name}--{random_number}!"
    driver.get("https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&ct=1665557053&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d360b6449-437d-e38d-538a-dc0c141d304f&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&contextid=5A0E12A9010A5112&bk=1665557053&uiflavor=web&lic=1&mkt=EN-US&lc=1033&uaid=c49d32026b3f42dbb2fd85976911894f")
    print("Waiting for Page 1-")
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.ID, "MemberName")))
    os.system('cls')
    intro()
    creationpage = driver.find_element(by=By.ID, value="MemberName")
    creationpage.send_keys(f"{first_name}{last_name}{random_number}")
    os.system("color 2")
    print(Fore.RED + f"[+]Fetched outlook :{first_name}{last_name}{random_number}@outlook.com"+Fore.RESET)
    signupmoment = driver.find_element(by = By.ID ,value = "iSignupAction")
    signupmoment.click()
    print(f"[+]Clicked Button: iSignupAction")
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.ID, "PasswordInput")))
    driver.find_element(by = By.ID ,value = "PasswordInput").send_keys(str(password))
    print(Fore.CYAN + f"[+]Fetched password : [{password}]"+Fore.RESET)
    uff = driver.find_element(by = By.ID , value = "iSignupAction")
    uff.click()
    months = ['January','February','March','April','June','July','August','September','October',"November","December"]
    days = ['1','2','3']
    years = ['2000','2001','1998','1999','1987','1986','1984']
    print(f"[+]Clicked Button: iSignupAction")
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.ID, "FirstName")))
    driver.find_element(by = By.ID,value ="FirstName").send_keys(str(first_name))
    driver.find_element(by = By.ID,value ="LastName").send_keys(str(last_name))
    print(f"[+]Filled FirstName : {first_name} and LastName: {last_name} ")
    idk = driver.find_element(by = By.ID,value ="iSignupAction")
    print(f"[+]Clicked Button : iSignupAction")
    idk.click()
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.ID, "BirthMonth")))
    driver.find_element(by = By.ID , value = "BirthMonth").send_keys(random.choice(months))
    driver.find_element(by = By.ID , value = "BirthDay").send_keys(random.choice(days))
    driver.find_element(by = By.ID , value = "BirthYear").send_keys(random.choice(years))
    driver.find_element(by = By.ID , value = "iSignupAction").click()
    print('[+]Filled out birthdate')
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "enforcementFrame"))).is_displayed()
    except:
        print("Ip flagged , couldnt load captcha ...[Change Ip using vpn]")
        driver.quit()
        exit(0)
    os.system('cls')
    print(Fore.LIGHTMAGENTA_EX+"Complete the bot verification to continue...")
    WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.ID, "KmsiCheckboxField"))).click()
    with open("accounts.txt", "a") as file:
        file.write(f"{first_name}{last_name}{random_number}@outlook.com:{password}\n")
        os.system('color a')
        print('User Solved captcha succesfully')
        print('Saved Details to accounts.txt')
        time.sleep(1)
        driver.quit()

create()
