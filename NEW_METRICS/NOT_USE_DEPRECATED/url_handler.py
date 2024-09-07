from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains

# Opciones para configurar Firefox como navegador controlado por Selenium
firefox_options = webdriver.FirefoxOptions()

# Crear un perfil personalizado para manejar las descargas automáticamente en Firefox
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)  # 0: Desktop, 1: Default, 2: Directorio personalizado
profile.set_preference("browser.download.dir", "./projects/")  # Directorio donde se guardarán las descargas
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/zip")  # Tipos MIME para descargar automáticamente

# Agregar el perfil al objeto de opciones de Firefox
firefox_options.profile = profile

# Inicializar el navegador Firefox usando las opciones configuradas y WebDriver Manager para gestionar GeckoDriver
service = Service(executable_path='/snap/bin/geckodriver')
driver = webdriver.Firefox(service=service, options=firefox_options)

# Función para descargar el proyecto desde una URL de Scratch
def descargar_proyecto(url):
    try:
        # Abrir la URL del proyecto de Scratch
        driver.get(url)

        # Espera a que el elemento esté presente
        driver.implicitly_wait(10)

        # Encuentra el elemento utilizando un selector
        element = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div/ul/li[4]/span')

        # Mueve el cursor al elemento y haz clic
        ActionChains(driver).move_to_element(element).click().perform()

        # Captura la URL actual después del clic
        current_url = driver.current_url

        print(f'La URL capturada es: {current_url}')

    except Exception as e:
        print(f"Error: {str(e)}")

# Función para leer las URLs desde un archivo de texto
def leer_urls_desde_archivo(archivo):
    urls = []
    with open(archivo, 'r') as file:
        for line in file:
            urls.append(line.strip())
    return urls

# Nombre del archivo que contiene las URLs
archivo_urls = 'batch_master_id.txt'

# Obtener las URLs desde el archivo
urls = leer_urls_desde_archivo(archivo_urls)

# Descargar cada proyecto desde las URLs obtenidas
for url in urls:
    descargar_proyecto(url)

# Cerrar el navegador al finalizar
driver.quit()

