from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from time import sleep
import pyperclip
import os

# servico = Service(ChromeDriverManager().install())

# options = webdriver.ChromeOptions()
# options.add_argument(r'user-data-dir=C:\Users\felipe.monsef\AppData\Local\Google\Chrome\User Data\Profile Selenium')

# navegador = webdriver.Chrome(service=servico, options=options)


def abrir_navegador():
    chrome_install = ChromeDriverManager().install()

    folder = os.path.dirname(chrome_install)
    chromedriver_path = os.path.join(folder, "chromedriver.exe")

    servico = Service(chromedriver_path)

    options = webdriver.ChromeOptions()
    options.add_argument(r'user-data-dir=C:\Users\felipe.monsef\AppData\Local\Google\Chrome\User Data\Profile Selenium')
    options.add_argument("--log-level=1")

    navegador = webdriver.Chrome(service=servico, options=options)

    return navegador


def abrir_site(navegador, link_site='http://web.whatsapp.com'):
    navegador.get(link_site)


def pesquisar_nome_grupo(navegador, regiao):
    while True:
        try:
            sleep(1.5)
            navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(regiao, Keys.ENTER)
            break
        except NoSuchElementException:
            pass

    while True:
        try:
            navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/span/button').click()
            break
        except NoSuchElementException:
            pass


def selecionar_img(navegador, regiao, arquivos_img):
    arquivo_img = arquivos_img + fr'\{regiao} PARCIAL.jpg'

    while True:
        try:
            navegador.find_element(By.CLASS_NAME, 'x1h4ghdb').click()
            break
        except NoSuchElementException:
            pass

    while True:
        try:
            sleep(1)
            navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input').send_keys(arquivo_img)
            break
        except NoSuchElementException:
            pass


def escrever_mensagem(navegador, text_wpp, nome_contato):
    while True:
        try:
            navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p').click()
            break
        except:
            pass
        
    act = ActionChains(navegador)

    pyperclip.copy(text_wpp + '\n')
    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

    if len(nome_contato) > 1:
        pyperclip.copy(nome_contato[0][:6])
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        act.send_keys(Keys.TAB).perform()

        pyperclip.copy(nome_contato[1][:6])
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        act.send_keys(Keys.TAB).perform()
    else:
        pyperclip.copy(nome_contato[0][:11])
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        act.send_keys(Keys.TAB).perform()
        
    sleep(0.5)


def enviar_mensagem(navegador):
    restart = True

    while restart:
        restart = False
        spans = navegador.find_elements(By.TAG_NAME, 'span')

        for span in spans:
            try:
                if span.get_attribute('data-icon') == 'send':
                    span.click()
            except StaleElementReferenceException as e:
                print(e)
                restart = True
                break

# navegador = abrir_navegador()

# abrir_site(navegador=navegador)
# pesquisar_nome_grupo(navegador, 'felipe monsef')
# escrever_mensagem(navegador, )
# selecionar_foto(navegador, 'RG UBERLANDIA')
# enviar_mensagem(navegador)