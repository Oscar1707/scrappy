from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def walmartScrappy():
    # Inicializar el driver de Selenium para Chrome
    driver = webdriver.Chrome()

    # Navegar a la página de ejemplo
    driver.get("https://www.example.com")

    # Verificar el título de la página
    assert "Example Domain" in driver.title, "El título de la página no coincide"

    # Imprimir el título de la página para confirmar
    print("Título de la página:", driver.title)

    # Cerrar el navegador
    driver.close()
