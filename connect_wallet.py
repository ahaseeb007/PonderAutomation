# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options as ChromeOptions
#
#
# chrome_options = ChromeOptions()
# chrome_options.add_argument("user-data-dir=F:\\testing\\Ponder")
# # chrome_options.add_extension("meta.crx")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#
# driver.maximize_window()
#
# # Open the web page
# driver.get("https://app.ponder.one/advance/bridge")
#
# # Get the title of the web page
# page_title = driver.title
#
# # Verify the page title
# expected_title = "Ponder"
# if page_title == expected_title:
#     print("Title is correct: ", page_title)
# else:
#     print("Title is incorrect: ", page_title)
#
# wait = WebDriverWait(driver, 20)
# click_connect_wallet = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Connect Wallet']")))
# click_connect_wallet.click()
#
# # Function to get shadow root
# def expand_shadow_element(element):
#     shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
#     return shadow_root
#
# # Access the first shadow host and shadow root
# first_shadow_host = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "w3m-modal")))
# first_shadow_root = expand_shadow_element(first_shadow_host)
#
# # Access the second shadow host and shadow root
# second_shadow_host = first_shadow_root.find_element(By.CSS_SELECTOR, "wui-flex")
# second_shadow_root = expand_shadow_element(second_shadow_host)
#
# # Access the third shadow host and shadow root
# third_shadow_host = second_shadow_host.find_element(By.TAG_NAME, "wui-card")
# third_shadow_root = expand_shadow_element(third_shadow_host)
#
# forth_shadow_host = third_shadow_host.find_element(By.CSS_SELECTOR, "w3m-router")
# forth_shadow_root = expand_shadow_element(forth_shadow_host)
#
# # Access the fifth shadow host and shadow root
# fifth_shadow_host = forth_shadow_root.find_element(By.CSS_SELECTOR, "w3m-connect-view")
# fifth_shadow_root = expand_shadow_element(fifth_shadow_host)
#
# shadow_element = fifth_shadow_root.find_element(By.CSS_SELECTOR, "wui-list-wallet[name='MetaMask']")
# shadow_element.click()
#
# time.sleep(2)
#
# driver.switch_to.window(driver.window_handles[1])
#
# # driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html")
#
# time.sleep(2)
#
# enter_password = wait.until(EC.presence_of_element_located((By.ID, "password")))
# enter_password.send_keys("Farhan@1234")
#
# unlock_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='unlock-submit']")))
# unlock_button.click()
#
# driver.switch_to.window(driver.window_handles[0])
#
# time.sleep(2)
#
# user_wallet = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/span[1]")))
# print(user_wallet.text)
#
# time.sleep(10)