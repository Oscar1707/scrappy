from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# URL del hub del Grid de Selenium Standalone
grid_url = "http://localhost:4444/wd/hub"

# Configura las opciones del controlador para usar con el Grid
options = webdriver.ChromeOptions()
# Opciones adicionales si es necesario
# options.add_argument("--headless")

# Inicia el driver remoto utilizando el Grid y las opciones configuradas
driver = webdriver.Remote(
    command_executor=grid_url,
    options=options
)

# Ejemplo de cómo usar el driver
driver.get("https://www.ejemplo.com")

# Realiza las acciones que necesites en tu prueba...

# Cierra el navegador al finalizar
#driver.quit()

#