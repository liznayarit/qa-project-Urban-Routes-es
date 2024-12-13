from PageLocators import UrbanRoutesPage
from main import retrieve_phone_code
import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Methods:
    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.locators = UrbanRoutesPage

    # Metodos
    # 1. Configurar la dirección
    def set_from(self, from_address):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.locators.from_field))
        self.driver.find_element(*self.locators.from_field).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.locators.to_field))
        self.driver.find_element(*self.locators.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')


    # 2.Seleccionar la tarifa Comfort.
    def click_order_taxi_button(self):
        WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.button.round')))
        self.driver.find_element(*self.locators.order_taxi).click()

    def click_tariff_comfort(self):
        WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.tcard.active')))
        self.driver.find_element(*self.locators.tariff_comfort).click()

    def is_tariff_selected(self):
        try:
            self.driver.find_element(*self.locators.tariff_comfort)
            return True
        except:
            return False

    # 3.Rellenar el número de teléfono.
    def click_input_phone(self):
        self.driver.find_element(*self.locators.input_phone).click()

    def set_number_phone(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.input-container.error')))
        self.driver.find_element(*self.locators.number_phone).send_keys(data.phone_number)

    def click_button_phone(self):
        self.driver.find_element(*self.locators.button_phone).click()

    def set_sms_code(self, code):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//label[@for="code"]')))
        self.driver.find_element(*self.locators.sms_code).send_keys(code)

    def click_send_cod(self):
        self.driver.find_element(*self.locators.send_cod).click()

    def click_confirm_button(self):
        self.driver.find_element(*self.locators.confirm_button).click()


    # 4. Agregar una tarjeta de crédito.
    def click_input_card(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pp-text')))
        self.driver.find_element(*self.locators.input_card).click()

    def click_add_card(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Agregar tarjeta")]')))
        self.driver.find_element(*self.locators.add_card).click()

    def click_card_field(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'card-input')))
        self.driver.find_element(*self.locators.card_field).click()

    def set_card_field(self, card_number):
        self.driver.find_element(*self.locators.card_field).send_keys(data.card_number)

    def click_cod_card(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'card-code-input')))
        self.driver.find_element(*self.locators.cod_card).click()

    def set_cod_card(self, card_code):
        self.driver.find_element(*self.locators.cod_card).send_keys(data.card_code)

    def click_agg_button(self):
        self.driver.find_element(*self.locators.agg_button).click()

    def click_cancel_button(self):
        self.driver.find_element(*self.locators.cancel_button).click()

    def click_x_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.payment-picker.open.modal.section.active.close-button')))
        self.driver.find_element(*self.locators.x_button).click()

    # 5. Escribir un mensaje para el conductor.
    def set_conductor_field(self, message_for_driver):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'comment')))
        self.driver.find_element(*self.locators.conductor_field).send_keys(data.message_for_driver)

    def get_comment_field(self):
        return self.driver.find_element(*self.locators.conductor_field).get_attribute('value')


    # 6.Pedir una manta y pañuelos
    def click_req_button(self):
        self.driver.find_element(*self.locators.req_button).click()

    def click_slider(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.slider.round')))
        self.driver.find_element(*self.locators.slider).click()

    # 7.Pedir 2 helados
    def click_ice_cream_counter(self):
        self.driver.find_element(*self.locators.ice_cream_counter).click()

    def get_selected_ice_cream_count(self):
        ice_cream_count_element = self.driver.find_element(By.XPATH, "(//div[@class='counter-plus'])[1]")
        ice_cream_count = int(ice_cream_count_element.text)
        return ice_cream_count

    # 8.Aparece el modal para buscar un taxi
    def click_taxi_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'smart-button-wrapper')))
        self.driver.find_element(*self.locators.taxi_button).click()

    # 9.Esperar a que aparezca la información del conductor en el modal (opcional).
    def taxi_wait_screen(self):
        return self.driver.find_element(*self.locators.wait_screen).is_displayed()
