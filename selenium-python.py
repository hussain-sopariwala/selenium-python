from selenium import webdriver
driver = webdriver.Chrome()

driver.get('http://saucedemo.com')

username = driver.find_element_by_xpath('//*[@id="user-name"]')
username.send_keys('standard_user')

password=driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('secret_sauce')

login=driver.find_element_by_xpath('//*[@id="login-button"]')
login.click()

item1=driver.find_element_by_xpath('//*[@id="inventory_container"]/div/div[1]/div[3]/button')
item1.click()

item2=driver.find_element_by_xpath('//*[@id="inventory_container"]/div/div[2]/div[3]/button')
item2.click()


item3=driver.find_element_by_xpath('//*[@id="inventory_container"]/div/div[3]/div[3]/button')
item3.click()


item4=driver.find_element_by_xpath('//*[@id="inventory_container"]/div/div[4]/div[3]/button')
item4.click()

cart=driver.find_element_by_xpath('//*[@id="shopping_cart_container"]/a/span')
cart.click()

checkout=driver.find_element_by_xpath('//*[@id="cart_contents_container"]/div/div[2]/a[2]')
checkout.click()

firstname=driver.find_element_by_xpath('//*[@id="first-name"]')
firstname.send_keys('Hussain')

lastname=driver.find_element_by_xpath('//*[@id="last-name"]')
lastname.send_keys('Sopariwala')

zipcode=driver.find_element_by_xpath('//*[@id="postal-code"]')
zipcode.send_keys('327001')

continuee=driver.find_element_by_xpath('//*[@id="checkout_info_container"]/div/form/div[2]/input')
continuee.click()

finish=driver.find_element_by_xpath('//*[@id="checkout_summary_container"]/div/div[2]/div[8]/a[2]')
finish.click()
