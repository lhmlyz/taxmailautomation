import io
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select

clients = [{
    'client_name': '',
    'user_name': '',
    'user_password2': '',
    'user_password1': ''
}, {
    'client_name': '',
    'user_name': '',
    'user_password2': '',
    'user_password1': ''
}
]

driver = webdriver.Chrome(executable_path="chromedriver/chromedriver.exe")
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("--disable-popup-blocking")


def driver_engine():
    for i in range(len(clients)):
        driver.get("https://login.e-taxes.gov.az/login/#section2")
        driver.find_element_by_xpath("//a[@href='#Section2']").click()
        driver.implicitly_wait(1)

        u_name = driver.find_element_by_xpath("//input[@id='username']")
        u_name.send_keys(clients[i]['user_name'])

        u_password2 = driver.find_element_by_xpath("//input[@id='password2']")
        u_password2.send_keys(clients[i]['user_password2'])

        u_password1 = driver.find_element_by_xpath("//input[@id='password1']")
        u_password1.send_keys(clients[i]['user_password1'])

        drop_list = Select(driver.find_element_by_xpath("//select[@id='idare']"))
        drop_list.select_by_index(1)

        button = driver.find_element_by_xpath("//button[contains(@onclick,'formGonder();')]")
        button.click()

        time.sleep(10)

        soup = BeautifulSoup(driver.page_source, features="html.parser")

        with io.open(f"temp/{clients[i]['client_name']}-result.html", "w", encoding="utf-8") as file:
            file.write(str(soup.find('div', {'class': 'x-grid3-scroller'})))

        snout = driver.find_element_by_xpath("//*[contains(@id, 'x-auto-24')]")
        snout.click()
        btn_yes = driver.find_element_by_xpath("//button[contains(text(), 'Bəli')]")
        btn_yes.click()
    driver.quit()


driver_engine()
