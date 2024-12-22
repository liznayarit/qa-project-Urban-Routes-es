# Importa webdriver y la clase By para los localizadores
import data
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Declaramos la clase de objeto de la página
class UrbanRoutesPage:
    # Localizadores
    # 1. Configurar la dirección
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # 2.Seleccionar la tarifa Comfort.
    order_taxi = (By.XPATH, "//button[text()='Pedir un taxi']")
    # Correccion:
    comfort_button = (By.XPATH, "//div[@class='tcard-title'][contains(.,'Comfort')]")

    # 3.Rellenar el número de teléfono.
    input_phone = (By.CLASS_NAME, 'np-text')
    number_phone = (By.ID, 'phone')
    button_phone = (By.XPATH, '//*[contains(text(), "Siguiente")]')
    sms_code = (By.ID, 'code')
    confirm_button = (By.XPATH, '//*[contains(text(), "Confirmar")]')


    # 4. Agregar una tarjeta de crédito.
    input_card = (By.CLASS_NAME, 'pp-text')
    add_card = (By.XPATH, '//*[contains(text(), "Agregar tarjeta")]')
    card_field = (By.CLASS_NAME, 'card-input')
    cod_card = (By.NAME, 'code')
    agg_button = (By.XPATH, "//button[@type='submit' and text()='Agregar']")
    #cancel_button = (By.XPATH, "//button[@type='submit' and text()='Cancelar']")
    x_button = (By.CSS_SELECTOR, '.payment-picker.open .modal .section.active .close-button')

    # 5. Escribir un mensaje para el conductor.
    conductor_field = (By.ID, 'comment')

    # 6. Pedir una manta y pañuelos.
    req_button = (By.XPATH, "//div[@class='r-sw-label' and text()='Manta y pañuelos']/following-sibling::div[contains(@class, 'r-sw')]//span[@class='slider round']")
    slider = (By.CLASS_NAME, "switch-input")

    # 7.Pedir 2 helados.
    ice_cream_counter_plus = (By.XPATH, "(//div[@class='counter-plus'])[1]")
    ice_cream_counter_value = (By.CLASS_NAME, "counter-value")

    # 8.Aparece el modal para buscar un taxi.
    taxi_button = (By.CLASS_NAME, 'smart-button-wrapper')
    modal = (By.XPATH, '//*[contains(text(), "El conductor llegará en")]')

    # 9.Esperar a que aparezca la información del conductor en el modal (opcional).
    wait_screen = (By.CSS_SELECTOR, ".order-header-content")

    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 45)

    # Metodos
    # 1. Configurar la dirección
    def set_from(self, from_address):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.to_field))
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # 2.Seleccionar la tarifa Comfort.
    def click_order_taxi_button(self):
        WebDriverWait(self.driver, 20).until(
           EC.element_to_be_clickable(self.order_taxi))
        self.driver.find_element(*self.order_taxi).click()

    def click_tariff_comfort(self):
      comfort_tariff_button = WebDriverWait(self.driver, 50).until(
          EC.element_to_be_clickable(self.comfort_button))
      comfort_tariff_button.click()

    def is_tariff_selected(self):
        return self.driver.find_element(*self.comfort_button).is_enabled()

    # 3.Rellenar el número de teléfono.
    def click_input_phone(self):
        self.driver.find_element(*self.input_phone).click()

    def set_number_phone(self):
        self.driver.find_element(*self.number_phone).send_keys(data.phone_number)

    def click_button_phone(self):
        self.driver.find_element(*self.button_phone).click()

    def set_sms_code(self, code):
        self.driver.find_element(*self.sms_code).send_keys(code)

    def click_confirm_button(self, code):
        WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable(self.comfort_button))
        self.driver.find_element(*self.confirm_button).click()


    # 4. Agregar una tarjeta de crédito.
    def click_input_card(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pp-text')))
        self.driver.find_element(*self.input_card).click()

    def click_add_card(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Agregar tarjeta")]')))
        self.driver.find_element(*self.add_card).click()

    def click_card_field(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'card-input')))
        self.driver.find_element(*self.card_field).click()

    def set_card_field(self):
        self.driver.find_element(*self.card_field).send_keys(data.card_number)

    def click_cod_card(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, 'code')))
        self.driver.find_element(*self.cod_card).click()


    def set_cod_card(self):
        codigo_tarjeta_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.cod_card)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", codigo_tarjeta_field)
        codigo_tarjeta_field.send_keys(data.card_code)

    def press_tab_key(self):
        WebDriverWait(self.driver, 4).until(
            expected_conditions.visibility_of_element_located(self.cod_card)
        )
        self.driver.find_element(*self.cod_card).send_keys(Keys.TAB)

    def click_agg_button(self):
        self.driver.find_element(*self.agg_button).click()

    def click_x_button(self):
        self.driver.find_element(*self.x_button).click()

    # 5. Escribir un mensaje para el conductor.
    def set_conductor_field(self, message_for_driver):
        WebDriverWait(self.driver, 45).until(EC.visibility_of_element_located((By.ID, 'comment')))
        self.driver.find_element(*self.conductor_field).send_keys(data.message_for_driver)

    def get_comment_field(self):
        return self.driver.find_element(*self.conductor_field).get_attribute('value')

    # 6.Pedir una manta y pañuelos
    def click_req_button(self):
        self.driver.find_element(*self.req_button).click()

    # 7.Pedir 2 helados
    def click_ice_cream_counter(self):
        self.driver.find_element(*self.ice_cream_counter_plus).click()

    def double_click_counter_plus(self, clicks=2):  # Agrega un parámetro por defecto
        WebDriverWait(self.driver, 40).until(
        expected_conditions.element_to_be_clickable(self.ice_cream_counter_plus)
        )
        for _ in range(clicks):
            self.driver.find_element(*self.ice_cream_counter_plus).click()

    def get_selected_ice_cream_count(self):
        value_element = self.wait.until(expected_conditions.visibility_of_element_located(self.ice_cream_counter_value))
        value = value_element.text.strip()
        return int(value) if value else 0

    # 8.Aparece el modal para buscar un taxi
    def click_taxi_button(self):
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'smart-button-wrapper')))
        self.driver.find_element(*self.taxi_button).click()















