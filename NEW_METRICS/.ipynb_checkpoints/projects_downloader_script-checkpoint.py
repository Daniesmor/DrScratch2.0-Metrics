from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ubicación del ejecutable de GeckoDriver (ajusta según tu sistema y ubicación)
geckodriver_path = '/snap/bin/geckodriver'

# Opciones para configurar Firefox como navegador controlado por Selenium
firefox_options = webdriver.FirefoxOptions()

# Crear un perfil personalizado para manejar las descargas automáticamente en Firefox
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.download.folderList", 2)  # 0: Desktop, 1: Default, 2: Directorio personalizado
firefox_profile.set_preference("browser.download.dir", "./projects/")  # Directorio donde se guardarán las descargas
firefox_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/zip")  # Tipos MIME para descargar automáticamente

# Inicializar el navegador Firefox usando GeckoDriver y las opciones configuradas
driver = webdriver.Firefox(executable_path=geckodriver_path, firefox_profile=firefox_profile, options=firefox_options)

# Función para descargar el proyecto desde una URL de Scratch
def descargar_proyecto(url):
    try:
        # Abrir la URL del proyecto de Scratch
        driver.get(url)
        
        # Esperar hasta que el botón "File" esté presente y sea cliclable
        file_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="File"]'))
        )
        file_button.click()

        # Esperar hasta que la opción "Save to your computer" esté presente y sea cliclable
        save_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//li[contains(text(), "Save to your computer")]'))
        )
        save_option.click()

        # Esperar a que se complete la descarga (opcional)
        WebDriverWait(driver, 60).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )

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
archivo_urls = 'batch_master_links.txt'

# Obtener las URLs desde el archivo
urls = leer_urls_desde_archivo(archivo_urls)

# Descargar cada proyecto desde las URLs obtenidas
for url in urls:
    descargar_proyecto(url)

# Cerrar el navegador al finalizar
driver.quit()
