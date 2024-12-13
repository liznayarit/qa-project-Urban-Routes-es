from PageMethods import Methods
import data
import main
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





# Casos de pruebas
class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.routes_page = Methods(cls.driver)


    # 1.Configurar la dirección
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_from(address_from)
        self.routes_page.set_to(address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    # 2.Seleccionar la tarifa Comfort.
    def test_select_tariff(self):
        self.routes_page.click_order_taxi_button()
        self.routes_page.click_tariff_comfort()
        assert self.routes_page.is_tariff_selected(), 'Comfort tariff not selected'

    # 3.Rellenar el número de teléfono.
    def test_phone_number(self):
        self.routes_page.click_input_phone()
        self.routes_page.set_number_phone()
        self.routes_page.click_button_phone()
        code = main.retrieve_phone_code(self.driver)
        self.routes_page.click_confirm_button(code)
        phone_input_value = self.driver.find_element(*self.routes_page.locators.number_phone).get_attribute("value")
        assert phone_input_value == data.phone_number

    # 4.Agregar una tarjeta de crédito.
    def test_add_credit_card(self):
        self.routes_page.click_input_card()
        self.routes_page.click_add_card()
        self.routes_page.click_card_field()
        self.routes_page.set_card_field(data.card_number)
        self.routes_page.click_cod_card()
        self.routes_page.set_cod_card(data.card_code)
        self.routes_page.click_agg_button()
        self.routes_page.click_cancel_button()
        self.routes_page.click_x_button()


    # 5.Escribir un mensaje para el controlador.
    def test_comment_for_driver(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page = Methods(self.driver)
        self.routes_page.set_conductor_field(data.message_for_driver)

        assert self.routes_page.get_comment_field() == data.message_for_driver

    # 6.Pedir una manta y pañuelos
    def test_select_slider(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page = Methods(self.driver)
        self.routes_page.click_req_button()
        self.routes_page.click_slider()
        #La opción haya sido seleccionada
        assert self.driver.find_element(*self.routes_page.locators.slider).is_selected()

    # 7.Pedir 2 helados
    def test_select_two_ice_creams(self):
        self.driver.get(data.urban_routes_url)
        routes_page = Methods(self.driver)
        routes_page.click_ice_cream_counter()
        selected_ice_cream_count = routes_page.get_selected_ice_cream_count()

        assert selected_ice_cream_count == 2


    # 8.Aparece el modal para buscar un taxi
    def test_taxi_search_modal(self):
        self.driver.get(data.urban_routes_url)
        routes_page = Methods(self.driver)
        routes_page.click_taxi_button()

    # Verificar si el modal ha aparecido (usando la presencia de algún elemento del modal)
        modal_displayed = self.driver.find_element(By.CSS_SELECTOR, '.order-header-title').is_displayed()

    # 9.Esperar a que aparezca la información del conductor en el modal (opcional).
    def test_driver_information_screen(self):
        routes_page = Methods(self.driver)
        assert routes_page.taxi_wait_screen() == True


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
