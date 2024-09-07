from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service

# Configuración de opciones y perfil de Firefox
firefox_options = webdriver.FirefoxOptions()
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.dir", "./projects/")
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/zip")
firefox_options.profile = profile

# Inicializar el navegador Firefox
service = Service(executable_path='/snap/bin/geckodriver')
driver = webdriver.Firefox(service=service, options=firefox_options)
def click_elemento_seleccionado(selectores):
    for selector in selectores:
        try:
            elemento = driver.find_element(By.CSS_SELECTOR, selector)
            if elemento:
                elemento.click()
                return True
        except Exception as e:
            print(f"Error al intentar encontrar y hacer clic en el elemento: {e}")
    return False

# Función para ejecutar cada acción descrita en el JSON
def ejecutar_acciones(acciones):
    for accion in acciones:
        if accion['type'] == 'click':
            selectors = accion['selectors']
            offset_x = accion['offsetX']
            offset_y = accion['offsetY']
            if click_elemento_seleccionado(selectors):
                print(f"Clic realizado en el elemento con selectores {selectors}")
            else:
                print(f"No se pudo hacer clic en el elemento con selectores {selectors}")

# JSON simulado con las acciones a ejecutar
acciones_json = [
    {
        "type": "click",
        "selectors": [
            "div:nth-of-type(3) > span > span",
            "xpath///*[@id=\"app\"]/div/div[2]/div[1]/div[1]/div[3]/span/span",
            "pierce/div:nth-of-type(3) > span > span",
            "text/File"
        ],
        "offsetY": 3,
        "offsetX": 5.171875
    },
    {
        "type": "click",
        "selectors": [
            "li:nth-of-type(4) > span",
            "xpath///*[@id=\"app\"]/div/div[2]/div[1]/div[1]/div[3]/div/ul/li[4]/span",
            "pierce/li:nth-of-type(4) > span",
            "text/Save to your"
        ],
        "offsetY": 7,
        "offsetX": 90.171875
    }
]

# Nombre del archivo que contiene las URLs
archivo_urls = 'batch_master_id.txt'

# Obtener las URLs desde el archivo
urls = leer_urls_desde_archivo(archivo_urls)

# Descargar cada proyecto desde las URLs obtenidas
for url in urls:
    driver.get(url)
    
    # Ejecutar las acciones definidas en el JSON
    ejecutar_acciones(acciones_json)

# Cerrar el navegador al finalizar
driver.quit()


