from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def walmartScrappy():
    # Inicializar el driver de Selenium para Chrome
    driver = webdriver.Remote(
        'http://localhost:4444/wd/hub',
        desired_capabilities=webdriver.DesiredCapabilities.CHROME
    )

    # Navegar a la página de ejemplo
    driver.get("https://www.example.com")

    # Verificar el título de la página
    assert "Example Domain" in driver.title, "El título de la página no coincide"

    # Imprimir el título de la página para confirmar
    print("Título de la página:", driver.title)

    # Cerrar el navegador
    driver.close()
walmartScrappy()