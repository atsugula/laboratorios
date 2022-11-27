from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

campos = [
    'Lógica', 'Ciclos', 'Recursividad', 'Funciones', 'Import', 'Variables globales', 'Arreglos', 'Matrices', 'Interfaz gráfica'
]

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://forms.gle/NpsJmuHawDUio1Nz5")

driver.find_element(By.CLASS_NAME, 'uHMk6b fsHoPb')

# Inicio ciclo para llenar el form
time.sleep(30)