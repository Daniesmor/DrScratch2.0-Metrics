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


class TestScratchdownloader():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_scratchdownloader1(self):
        self.driver.get("https://scratch.mit.edu/projects/129150753/editor/")
        self.driver.set_window_size(550, 691)
        self.driver.find_element(By.XPATH, "//img[contains(@src,'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHZpZXdCb3g9IjAgMCAyMCAyMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00Ljk4MTE2IDFIMTUuMDE5NkMxNi40MDQyIDEgMTcuNjE1OCAyLjIxMTU0IDE3LjYxNTggMy41OTYxNVYxMC44NjU0SDEzLjYzNUMxMS4zODUgMTAuODY1NCA5LjY1NDI0IDEyLjc2OTIgOS42NTQyNCAxNC44NDYyVjE4LjgyNjlINC45ODExNkMzLjU5NjU1IDE4LjgyNjkgMi4zODUwMSAxNy42MTU0IDIuMzg1MDEgMTYuMjMwOFYzLjU5NjE1QzIuMzg1MDEgMi4yMTE1NCAzLjU5NjU1IDEgNC45ODExNiAxWk02LjAxOTYzIDkuODI2OTJIOC43ODg4NkM5LjQ4MTE2IDkuODI2OTIgMTAuMDAwNCA5LjQ4MDc3IDEwLjAwMDQgOC43ODg0NkMxMC4wMDA0IDguMDk2MTUgOS40ODExNiA3Ljc1IDguOTYxOTMgNy43NUg2LjAxOTYzQzUuNTAwMzkgNy43NSA0Ljk4MTE2IDguMjY5MjMgNC45ODExNiA4Ljc4ODQ2QzQuOTgxMTYgOS4zMDc2OSA1LjUwMDM5IDkuODI2OTIgNi4wMTk2MyA5LjgyNjkyWk0xNC4xNTQyIDUuODQ2MTVINi4wMTk2M0M1LjMyNzMyIDUuODQ2MTUgNC45ODExNiA1LjMyNjkyIDQuOTgxMTYgNC44MDc2OUM0Ljk4MTE2IDQuMjg4NDYgNS41MDAzOSAzLjc2OTIzIDYuMDE5NjMgMy43NjkyM0gxNC4xNTQyQzE0LjY3MzUgMy43NjkyMyAxNS4xOTI3IDQuMjg4NDYgMTUuMTkyNyA0LjgwNzY5QzE1LjAxOTYgNS4zMjY5MiAxNC42NzM1IDUuODQ2MTUgMTQuMTU0MiA1Ljg0NjE1Wk0xNy40NDI3IDEyLjI1SDEzLjQ2MTlDMTIuMDc3MyAxMi4yNSAxMC44NjU4IDEzLjQ2MTUgMTAuODY1OCAxNS4wMTkyVjE5TDE3LjQ0MjcgMTIuMjVaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4K')]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".menu_menu-item_3EwYA:nth-child(3)").click()
    
    def test_scratchdownloader2(self):
        self.driver.get("https://scratch.mit.edu/projects/131382669/editor/")
        self.driver.set_window_size(550, 691)
        self.driver.find_element(By.XPATH, "//img[contains(@src,'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHZpZXdCb3g9IjAgMCAyMCAyMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00Ljk4MTE2IDFIMTUuMDE5NkMxNi40MDQyIDEgMTcuNjE1OCAyLjIxMTU0IDE3LjYxNTggMy41OTYxNVYxMC44NjU0SDEzLjYzNUMxMS4zODUgMTAuODY1NCA5LjY1NDI0IDEyLjc2OTIgOS42NTQyNCAxNC44NDYyVjE4LjgyNjlINC45ODExNkMzLjU5NjU1IDE4LjgyNjkgMi4zODUwMSAxNy42MTU0IDIuMzg1MDEgMTYuMjMwOFYzLjU5NjE1QzIuMzg1MDEgMi4yMTE1NCAzLjU5NjU1IDEgNC45ODExNiAxWk02LjAxOTYzIDkuODI2OTJIOC43ODg4NkM5LjQ4MTE2IDkuODI2OTIgMTAuMDAwNCA5LjQ4MDc3IDEwLjAwMDQgOC43ODg0NkMxMC4wMDA0IDguMDk2MTUgOS40ODExNiA3Ljc1IDguOTYxOTMgNy43NUg2LjAxOTYzQzUuNTAwMzkgNy43NSA0Ljk4MTE2IDguMjY5MjMgNC45ODExNiA4Ljc4ODQ2QzQuOTgxMTYgOS4zMDc2OSA1LjUwMDM5IDkuODI2OTIgNi4wMTk2MyA5LjgyNjkyWk0xNC4xNTQyIDUuODQ2MTVINi4wMTk2M0M1LjMyNzMyIDUuODQ2MTUgNC45ODExNiA1LjMyNjkyIDQuOTgxMTYgNC44MDc2OUM0Ljk4MTE2IDQuMjg4NDYgNS41MDAzOSAzLjc2OTIzIDYuMDE5NjMgMy43NjkyM0gxNC4xNTQyQzE0LjY3MzUgMy43NjkyMyAxNS4xOTI3IDQuMjg4NDYgMTUuMTkyNyA0LjgwNzY5QzE1LjAxOTYgNS4zMjY5MiAxNC42NzM1IDUuODQ2MTUgMTQuMTU0MiA1Ljg0NjE1Wk0xNy40NDI3IDEyLjI1SDEzLjQ2MTlDMTIuMDc3MyAxMi4yNSAxMC44NjU4IDEzLjQ2MTUgMTAuODY1OCAxNS4wMTkyVjE5TDE3LjQ0MjcgMTIuMjVaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4K')]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".menu_menu-item_3EwYA:nth-child(3)").click()
        

tester = TestScratchdownloader()
tester.setup_method()

# Cerrar el navegador al finalizar
driver.quit()


