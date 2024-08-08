import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MetaMaskPage:

    enter_password_field_ID= "password"
    click_unlock_btn_xpath= "//button[@data-testid='unlock-submit']"
    ethereum_chain_xpath= "//span[normalize-space()='Ethereum']"
    click_confirm_btn_css= ".btn--rounded.btn-primary"
    connect_wallet_xpath= "//button[normalize-space()='Connect Wallet']"

    def __init__(self,driver):
        self.driver= driver

    def click_connect_wallet(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            click_connect_wallet = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.connect_wallet_xpath)))
            click_connect_wallet.click()
        except:
            assert False, "Connect wallet button is not visible"

    def click_meta_mask_button(self):
        def expand_shadow_element(element):
            shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', element)
            return shadow_root

        wait = WebDriverWait(self.driver, 20)
        # Access the first shadow host and shadow root
        first_shadow_host = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "w3m-modal")))
        first_shadow_root = expand_shadow_element(first_shadow_host)

        # Access the second shadow host and shadow root
        second_shadow_host = first_shadow_root.find_element(By.CSS_SELECTOR, "wui-flex")
        second_shadow_root = expand_shadow_element(second_shadow_host)

        # Access the third shadow host and shadow root
        third_shadow_host = second_shadow_host.find_element(By.TAG_NAME, "wui-card")
        third_shadow_root = expand_shadow_element(third_shadow_host)

        forth_shadow_host = third_shadow_host.find_element(By.CSS_SELECTOR, "w3m-router")
        forth_shadow_root = expand_shadow_element(forth_shadow_host)

        # Access the fifth shadow host and shadow root
        fifth_shadow_host = forth_shadow_root.find_element(By.CSS_SELECTOR, "w3m-connect-view")
        fifth_shadow_root = expand_shadow_element(fifth_shadow_host)

        shadow_element = fifth_shadow_root.find_element(By.CSS_SELECTOR, "wui-list-wallet[name='MetaMask']")
        shadow_element.click()

        time.sleep(2)

    def switch_to_meta_mask(self):

        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
        except:
            assert False, "No MetaMask window available"

    def enter_password(self, password):

        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID,self.enter_password_field_ID))).send_keys(password)
        except:
            assert False, "Password field is not visible"

    def click_unblock_btn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,self.click_unlock_btn_xpath))).click()

    def switch_window(self):

        self.driver.switch_to.window(self.driver.window_handles[0])

    def validate_connection(self):

        try:
            select_chain= WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,self.ethereum_chain_xpath)))
            assert select_chain.is_displayed(), "The Wallet is not connected"
        except:
            assert False, "The Wallet is not connected successfully"

    def click_confirm_button(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.click_confirm_btn_css)))

        # click on the next button in MetaMask
        next_btn = self.driver.find_element(By.CSS_SELECTOR, self.click_confirm_btn_css)

        self.driver.execute_script('arguments[0].click()', next_btn)