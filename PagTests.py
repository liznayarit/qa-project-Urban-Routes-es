import data
import helpers
import PageLocators
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


# Casos de pruebas
class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = Options()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(50)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = PageLocators.UrbanRoutesPage(cls.driver)


    def teardown_method(self, method):
        self.driver.delete_all_cookies()  # Esto limpiará cookies y sesión
        self.driver.refresh()  # Refrescará la página para empezar desde cero


    # 1.Configurar la dirección
    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_from(address_from)
        self.routes_page.set_to(address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    # 2.Seleccionar la tarifa Comfort.
    def test_select_tariff(self):
        self.routes_page.set_from(data.address_from)
        self.routes_page.set_to(data.address_to)
        self.routes_page.click_order_taxi_button()
        self.routes_page.click_tariff_comfort()
        #Correccion:
        comfort_status = self.routes_page.is_tariff_selected()
        assert comfort_status == True

    # 3.Rellenar el número de teléfono.
    def test_phone_number(self):
        self.routes_page.set_from(data.address_from)
        self.routes_page.set_to(data.address_to)
        self.routes_page.click_order_taxi_button()
        self.routes_page.click_tariff_comfort()
        self.routes_page.click_input_phone()
        self.routes_page.set_number_phone()
        self.driver.implicitly_wait(30)
        self.routes_page.click_button_phone()
        code = helpers.retrieve_phone_code(self.driver)
        self.routes_page.click_confirm_button(code)
        self.driver.implicitly_wait(30)
        #Correccion:
        phone_input_value = self.driver.find_element(*self.routes_page.input_phone).get_attribute("value")
        self.driver.implicitly_wait(30)
        return phone_input_value == data.phone_number


    # 4.Agregar una tarjeta de crédito.
    def test_add_credit_card(self):
        self.routes_page.set_from(data.address_from)
        self.routes_page.set_to(data.address_to)
        self.routes_page.click_order_taxi_button()
        self.routes_page.click_tariff_comfort()
        self.routes_page.click_input_phone()
        self.routes_page.set_number_phone()
        self.routes_page.click_button_phone()
        code = helpers.retrieve_phone_code(self.driver)
        self.routes_page.set_sms_code(code)
        self.routes_page.click_confirm_button(code)
        self.routes_page.click_input_card()
        self.routes_page.click_add_card()
        self.routes_page.click_card_field()
        self.routes_page.set_card_field()
        self.routes_page.click_cod_card()
        self.routes_page.set_cod_card()
        self.routes_page.press_tab_key()
        #Correccion:
        card_input_value = self.driver.find_element(*self.routes_page.card_field).get_attribute("value")
        assert card_input_value == data.card_number
        self.routes_page.click_agg_button()
        #self.routes_page.click_cancel_button()
        self.routes_page.click_x_button()


    # 5.Escribir un mensaje para el controlador.
    def test_comment_for_driver(self):
        self.routes_page.set_from(data.address_from)
        self.routes_page.set_to(data.address_to)
        self.routes_page.click_order_taxi_button()
        self.routes_page.click_tariff_comfort()
        self.routes_page.set_conductor_field(data.message_for_driver)
        assert self.routes_page.get_comment_field() == data.message_for_driver

    # 6.Pedir una manta y pañuelos
    def test_select_slider(self):
        self.routes_page.set_from(data.address_from)
        self.routes_page.set_to(data.address_to)
        self.routes_page.click_order_taxi_button()
        self.routes_page.click_tariff_comfort()
        self.routes_page.click_req_button()
        #La opción haya sido seleccionada
        assert self.driver.find_element(*PageLocators.UrbanRoutesPage.slider).is_selected() == True

    # 7.Pedir 2 helados
    def test_select_two_ice_creams(self):
        self.routes_page.set_from(data.address_from)
        self.routes_page.set_to(data.address_to)
        self.routes_page.click_order_taxi_button()
        self.routes_page.click_tariff_comfort()
        self.routes_page.click_ice_cream_counter()
        routes_page = PageLocators.UrbanRoutesPage(self.driver)
        routes_page.double_click_counter_plus(2)
        selected_ice_cream_count = routes_page.get_selected_ice_cream_count()
        assert selected_ice_cream_count == 2


    # 8.Aparece el modal para buscar un taxi
    def test_taxi_search_modal(self):
        self.routes_page.set_from(data.address_from)
        self.routes_page.set_to(data.address_to)
        self.routes_page.click_order_taxi_button()
        self.routes_page.click_tariff_comfort()
        self.routes_page.click_input_phone()
        self.routes_page.set_number_phone()
        self.routes_page.click_button_phone()
        code = helpers.retrieve_phone_code(self.driver)
        self.routes_page.set_sms_code(code)
        self.routes_page.click_confirm_button(code)
        self.routes_page.click_input_card()
        self.routes_page.click_add_card()
        self.routes_page.click_card_field()
        self.routes_page.set_card_field()
        self.routes_page.click_cod_card()
        self.routes_page.set_cod_card()
        self.routes_page.press_tab_key()
        self.routes_page.click_agg_button()
        self.routes_page.click_x_button()
        self.routes_page.set_conductor_field(data.message_for_driver)
        self.routes_page.click_req_button()
        self.routes_page.click_ice_cream_counter()
        routes_page = PageLocators.UrbanRoutesPage(self.driver)
        routes_page.double_click_counter_plus(2)
        routes_page.get_selected_ice_cream_count()
        routes_page = PageLocators.UrbanRoutesPage(self.driver)
        # Correccion:
        routes_page.click_taxi_button()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
