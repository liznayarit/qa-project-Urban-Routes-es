# Nombre: Liz Pabon
# Sprint 8. Grupo 17

# Proyecto Urban Routes

## Descripción  
**Urban Routes** es una aplicación de servicio de taxi en linea, diseñada para que los usuarios puedan 
solicitar un taxi con diferentes opciones de tarifas y servicios adicionales. 
El objetivo de este proyecto es probar de manera automatizada el proceso completo de pedir un taxi,
para que funcione correctamente desde la dirección actual aportada hasta la de destino.
Ademas de solicitar los distintos métodos de pago con selección de tarifas segun la opción que prefiera 
el cliente, asi como el tiempo de llegada del conductor.

# Descripción de tecnologías Utilizadas
  Lenguaje Python,
  Paquete pytest,
  Selenium,
  WebDriver,
  Pycharm.

# Descripción de técnicas Utilizadas
Actualmente, las pruebas se están desarrollando en:
Lenguaje de programación Python, utilizando PyCharm como entorno de desarrollo. 
Para automatizar las pruebas se esta utilizando Selenium y webDriver, además de 
los paquetes de pytest para correr el proyecto.

# Ejecución de las pruebas y archivos a ejecutar:
Asegurarse de tener instalado el lenguaje Python, utiliza el administrador de paquetes 
para instalar pytest.
O tambien puedes usar la terminal colocando: 
pip install pytest, 
pip install selenium. 

Las pruebas utilizarán el navegador Chrome, así que asegúrate de tenerlo instalado.
Puedes ajustar las configuraciones del navegador en el método setup_class de la 
clase TestUrbanRoutes.

URL : https://cnt-ceb50922-71b3-4a55-9cc9-81afd559838e.containerhub.tripleten-services.com?lng=es

Se deben automatizar cada una de las siguientes acciones o pruebas:
1. Configurar la dirección.
2. Seleccionar la tarifa Comfort.
3. Rellenar el número de teléfono.
4. Agregar una tarjeta de crédito. 
5. Escribir un mensaje para el controlador.
6. Pedir una manta y pañuelos.
7. Pedir 2 helados.
8. Aparece el modal para buscar un taxi.

Reemplazar la URL de Urban Routes del servidor actualizada o iniciada en el archivo data.py
para poder ejecutar las pruebas, es decir puedan correr en el IDE de Pycharm.
En el archivo de PageLocators.py se deben buscar los localizadores y elegir selectores unicos, 
generando cada una por separado para luego ejecutar los metodos correspondientes en orden.
Por ultimo en el archivo PagTest.py se deben colocar cada uno de los casos de pruebas para 
proceder a correrlos por separado. 


# Ejecución de las pruebas en la terminal:
cd,
mkdir projects,
cd projects,
$ git clone git@github.com:liznayarit/qa-project-Urban-Routes-es.git.

