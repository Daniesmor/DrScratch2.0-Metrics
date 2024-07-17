import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.service import Service


# Ruta al archivo de texto con los enlaces
links_file = 'batch_master_id_no_editor.txt'

# Ruta a la carpeta donde se buscarán los archivos .sb3
sb3_folder = './projects_sb3'

# Función para verificar si el archivo .sb3 existe en la carpeta
def check_file_exists(project_name, folder):
    file_name = f"{project_name}.sb3"
    return os.path.isfile(os.path.join(folder, file_name))

# Configuración de Selenium para Firefox
firefox_options = FirefoxOptions()
firefox_options.headless = True  # Para ejecución en modo sin ventana (headless)
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.download.folderList", 2)
firefox_profile.set_preference("browser.download.dir", "./projects/")
firefox_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/zip")

service = Service(executable_path='/snap/bin/geckodriver')

driver = webdriver.Firefox(service=service, options=firefox_options)
# Inicializar el navegador Firefox
gecko_driver_path = '/path/to/geckodriver'  # Ruta al geckodriver en tu sistema
# Leer el archivo de texto y procesar cada enlace
with open(links_file, 'r') as file:
    links = file.readlines()

for link in links:
    link = link.strip()
    if not link:
        continue
    
    # Navegar a la página con Selenium
    driver.get(link)
    
    # Esperar un tiempo prudente para que se cargue el contenido dinámico (ajusta según necesidades)
    time.sleep(1)
    
    # Obtener el contenido de la página después de la carga dinámica con BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    app = soup.find(id='app')
    
    if app:
        
        page = app.find('div', class_='page')
        if page:
            main = page.find(id='view')
            if main:
                preview = main.find('div', class_='preview')
                if preview:
                    inner = preview.find('div', class_='inner')
                    if inner:
                        bat_tit = inner.find('div', class_='flex-row preview-row force-row')
                        if bat_tit:
                            flex_row = bat_tit.find('div', class_='flex-row project-header')
                            if flex_row:
                                title = flex_row.find('div', class_='title')
                                if title:
                                    title_text = title.find(class_='project-title no-edit')
                                    if title_text:
                                        project_name = title_text.text.strip()
                                        
                                        with open('all_project_names.sb3', 'a') as project_names:
                                        	project_names.write(project_name + '\n' + link)
                                        
                                        # Verificar si el archivo .sb3 existe
                                        if check_file_exists(project_name, sb3_folder):
                                            print(f"The file {project_name}.sb3 exists in the folder.")        
                                        else:
                                            print(f"The file {project_name}.sb3 does not exist in the folder.")
                                            with open('non_exist_projects.txt', 'a') as non_exist: 
                                                non_exist.write(link + '\n')
                                    else:
                                        print("No project title text found.")
                                else:
                                    print("No title div found.")
                            else:
                                print("No flex-row project-header found.")
                        else:
                            print("No flex-row preview-row force-row found.")
                    else:
                        print("No inner div found.")
                else:
                    print("No preview div found.")
            else:
                print("No main view found.")
        else:
            print("No page div found.")
    else:
        print("No app div found.")
