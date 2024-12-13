# Importa webdriver y la clase By para los localizadores
import data
from selenium import webdriver
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
    order_taxi = (By.CSS_SELECTOR, '.button.round')
    tariff_comfort = (By.CSS_SELECTOR, '.tcard.active')

    # 3.Rellenar el número de teléfono.
    input_phone = (By.CLASS_NAME, 'np-text')
    number_phone = (By.CSS_SELECTOR, '.input-container.error')
    button_phone = (By.XPATH, '//*[contains(text()="Siguiente")]')
    sms_code = (By.XPATH, '//label[@for="code"]')
    send_cod = (By.XPATH, '//*[contains(text(), "Vuelve a enviar el código")]')
    confirm_button = (By.XPATH, '//*[contains(text(), "Confirmar"])')


    # 4. Agregar una tarjeta de crédito.
    input_card = (By.CLASS_NAME, 'pp-text')
    add_card = (By.XPATH, '//*[contains(text(), "Agregar tarjeta")]')
    card_field = (By.CLASS_NAME, 'card-input')
    cod_card = (By.CLASS_NAME, 'card-code-input')
    agg_button = (By.XPATH, "//button[@type='submit' and text()='Agregar']")
    cancel_button = (By.XPATH, "//button[@type='submit' and text()='Cancelar']")
    x_button = (By.CSS_SELECTOR, '.payment-picker.open .modal .section.active .close-button')

    # 5. Escribir un mensaje para el conductor.
    conductor_field = (By.ID, 'comment')

    # 6. Pedir una manta y pañuelos.
    req_button = (By.CLASS_NAME, 'reqs-header')
    slider = (By.CSS_SELECTOR, '.slider.round')

    # 7.Pedir 2 helados.
    ice_cream_counter = (By.XPATH, "(//div[@class='counter-plus'])[1]")

    # 8.Aparece el modal para buscar un taxi.
    taxi_button = (By.CLASS_NAME, 'smart-button-wrapper')

    # 9.Esperar a que aparezca la información del conductor en el modal (opcional).
    wait_screen = (By.CSS_SELECTOR, ".order-header-content")


















