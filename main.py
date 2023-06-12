from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

nn = input("Please, input your nickname --> ")
if nn:
    browser = webdriver.Firefox()
    url = f"https://twitter.com/{nn}"

    try:
        browser.get(url=url)
        strng = "//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div[2]/div/div[1]/span"
        elem = browser.find_element(by="xpath", value=strng)
        print(elem.text)

    except NoSuchElementException:
        try:
            strng = "//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div/div/div/span/span"
            elem = browser.find_element(by="xpath", value=strng)
            print(elem.text)

        except NoSuchElementException:
            print("Account exists and not suspended")

    finally:
        browser.close()
        browser.quit()
