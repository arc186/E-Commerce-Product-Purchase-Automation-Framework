import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    Laptop_notebook_link_text = "Laptops & Notebooks"
    Show_AllLaptops_Notebooks_link_text = "Show AllLaptops & Notebooks"
    hp_product_link_text = "HP LP3065"
    img_hp_xpath = "(//img[@title='HP LP3065'])[1]"
    closed_button_xpath = "//button[@class='mfp-close']"
    add_to_cart_id = "button-cart"
    calendar_button_id = "input-option225"
    quantity_xpath = "input-quantity"
    add_to_item_xpath = "//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']"
    checkout_xpath = "//a[@title='Checkout']"
    guest_account_xpath = "//input[@value='guest']"
    guest_button_id = "button-account"
    billing_xpath = "//h4[.='Step 2: Billing Details ']"
    fname_id = "input-payment-firstname"
    lname_id = "input-payment-lastname"
    email_id = "input-payment-email"
    telephone_id = "input-payment-telephone"
    company_id = "input-payment-company"
    address1_id = "input-payment-address-1"
    address2_id = "input-payment-address-2"
    city_id = "input-payment-city"
    post_code_id = "input-payment-postcode"
    payment_country_id = "input-payment-country"
    state_id = "input-payment-zone"
    continue_id = "button-guest"
    delivery_id = "button-shipping-method"
    agree_name = "agree"
    payment_button_id = "button-payment-method"
    button_confirm_id = "button-confirm"
    continue_xpath = "//a[@class='btn btn-primary']"

    def select_laptop(self):
        # -----select laptop (HP LP3065)-----
        self.driver.find_element(By.LINK_TEXT, self.Laptop_notebook_link_text).click()
        self.driver.find_element(By.LINK_TEXT, self.Show_AllLaptops_Notebooks_link_text).click()
        self.driver.find_element(By.LINK_TEXT, self.hp_product_link_text).click()
        self.driver.find_element(By.XPATH, self.img_hp_xpath).click()
        time.sleep(2)
        img_hp = allure.attach(self.driver.get_screenshot_as_png(), name="Hp_product",
                               attachment_type=AttachmentType.PNG)
        return img_hp



    def add_to_cart(self):
        self.driver.find_element(By.XPATH, self.closed_button_xpath).click()
        add_to_cart_2 = self.driver.find_element(By.ID, self.add_to_cart_id)
        add_to_cart_2.location_once_scrolled_into_view
        # -----select delivery date: 2024-23-11-----
        date_field = self.driver.find_element(By.ID, self.calendar_button_id)
        self.driver.execute_script("arguments[0].value='2024-23-11'", date_field)
        # -----select laptop quantity -2-----
        self.driver.find_element(By.ID, self.quantity_xpath).clear()
        self.driver.find_element(By.ID, self.quantity_xpath).send_keys("2")
        add_to_cart_2.click()
        self.driver.find_element(By.XPATH, self.add_to_item_xpath).click()

    def guest_account_and_purchase_product(self):
        self.driver.find_element(By.XPATH, self.checkout_xpath).click()
        self.driver.find_element(By.XPATH, self.guest_account_xpath).click()
        self.driver.find_element(By.ID, self.guest_button_id).click()
        self.driver.find_element(By.XPATH, self.billing_xpath)
        self.driver.find_element(By.ID, self.fname_id).send_keys("test_fname")
        self.driver.find_element(By.ID, self.lname_id).send_keys("test_lname")
        self.driver.find_element(By.ID, self.email_id).send_keys("uio@gmail.com")
        self.driver.find_element(By.ID, self.telephone_id).send_keys("123456")
        self.driver.find_element(By.ID, self.company_id).send_keys("test_con")
        self.driver.find_element(By.ID, self.address1_id).send_keys("test_street")
        self.driver.find_element(By.ID, self.address2_id).send_keys("test_street2")
        self.driver.find_element(By.ID, self.city_id).send_keys("Mumbai")
        self.driver.find_element(By.ID, self.post_code_id).send_keys("400056")
        country = self.driver.find_element(By.ID, self.payment_country_id)
        drop_down_field1 = Select(country)
        drop_down_field1.select_by_value("99")
        state = self.driver.find_element(By.ID, self.state_id)
        drop_down_field1 = Select(state)
        drop_down_field1.select_by_value("1493")
        self.driver.find_element(By.ID, self.continue_id).click()
        self.driver.find_element(By.ID, self.delivery_id).click()

    def payment_product(self):
        # print the total price
        self.driver.find_element(By.NAME, self.agree_name).click()
        self.driver.find_element(By.ID, self.payment_button_id).click()
        time.sleep(2)
        img_payment = allure.attach(self.driver.get_screenshot_as_png(), name="payment",
                                    attachment_type=AttachmentType.PNG)
        return img_payment

    def order_confirmation(self):
        # confirm order
        self.driver.find_element(By.ID, self.button_confirm_id).click()
        time.sleep(2)
        img_confirmation_order = allure.attach(self.driver.get_screenshot_as_png(), name="confirmation_order",
                                               attachment_type=AttachmentType.PNG)
        return img_confirmation_order
