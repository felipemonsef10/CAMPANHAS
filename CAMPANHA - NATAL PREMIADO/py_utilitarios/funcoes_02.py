import pyautogui as py
from pyautogui import FailSafeException
from time import sleep
import pyperclip
import os


py.FAILSAFE = True
py.PAUSE = 1


def escrever_nova_mensagem(img_file_name=r'\btn-nova-mensagem.png'):
    file_path = os.getcwd() + r'\py_utilitarios' + img_file_name

    while not py.locateOnScreen(file_path, grayscale=True, confidence=0.9):
        sleep(1)
    
    btn_nova_mensagem = py.locateOnScreen(file_path, grayscale=True, confidence=0.9)
    py.click(py.center(btn_nova_mensagem))


def escrever_email_do_destinatario(email, img_file_name=r'\img-escrever-email.png'):
    file_path = os.getcwd() + r'\py_utilitarios' + img_file_name

    while not py.locateOnScreen(file_path, grayscale=True, confidence=0.9):
        sleep(1)

    if type(email) == list:
        for endereco_email in email:
            pyperclip.copy(endereco_email.capitalize())
            py.hotkey('ctrl', 'v')
            py.press('tab') 
    else:
        pyperclip.copy(email.capitalize())
        py.hotkey('ctrl', 'v')
        py.press('tab')


def escrever_emails_copia_oculta(emails_copia=['valdinei.claudiano@vasconcelos.ind.br'], img_file_name=r'\img-escrever-email.png'):
    file_path = os.getcwd() + r'\py_utilitarios' + img_file_name

    while not py.locateOnScreen(file_path, grayscale=True, confidence=0.9):
        sleep(1)

    py.hotkey('ctrl', 'shift', 'b')

    for email in emails_copia:
        pyperclip.copy(email)
        py.hotkey('ctrl', 'v')
        py.press('enter')
    
    py.press('tab')


def escrever_emails_copia(emails_copia=['valdinei.claudiano@vasconcelos.ind.br'], img_file_name=r'\img-escrever-email.png'):
    file_path = os.getcwd() + r'\py_utilitarios' + img_file_name

    while not py.locateOnScreen(file_path, grayscale=True, confidence=0.9):
        sleep(1)

    py.hotkey('ctrl', 'shift', 'c')

    for email in emails_copia:
        pyperclip.copy(email)
        py.hotkey('ctrl', 'v')
        py.press('enter')
    
    py.press('tab')


def escrever_assunto(assunto, img_file_name=r'\img-escrever-email.png'):
    file_path = os.getcwd() + r'\py_utilitarios' + img_file_name

    while not py.locateOnScreen(file_path, grayscale=True, confidence=0.9):
        sleep(1)

    pyperclip.copy(assunto)
    py.hotkey('ctrl', 'v')
    py.press('tab')


def inserir_texto_html(txt_html, img_file_names=[r'\btn-inserir.png', r'\btn-html.png']):
    file_paths = [os.getcwd() + r'\py_utilitarios' + img_file_names[0], os.getcwd() + r'\py_utilitarios' + img_file_names[1]]

    while not py.locateOnScreen(file_paths[0], grayscale=True, confidence=0.9):
        sleep(1)

    btn_inserir = py.locateOnScreen(file_paths[0], grayscale=True, confidence=0.9)
    py.click(py.center(btn_inserir))

    while not py.locateOnScreen(file_paths[1], grayscale=True, confidence=0.9):
        sleep(1)

    btn_html = py.locateOnScreen(file_paths[1], grayscale=True, confidence=0.9)
    py.click(py.center(btn_html))

    # escrever o texto html
    pyperclip.copy(txt_html)
    py.shortcut('ctrl', 'v')
    py.click(x=474, y=434)


def adicionar_anexo(nome_arquivo, img_file_names=[r'\anexar.png', r'\btn-abrir.png']):
    file_paths = [os.getcwd() + r'\py_utilitarios' + img_file_names[0], os.getcwd() + r'\py_utilitarios' + img_file_names[1]]

    if 'CONSOLIDADO' not in nome_arquivo:
        nome_arquivo = f'{nome_arquivo} PARCIAL'

    py.shortcut('ctrl', 'shift', 'a')

    while not py.locateOnScreen(file_paths[0], grayscale=True, confidence=0.9):
        sleep(1)

    pyperclip.copy(nome_arquivo)
    py.hotkey('ctrl', 'v')

    while not py.locateOnScreen(file_paths[1], grayscale=True, confidence=0.9):
        sleep(1)
        
    btn_abrir = py.locateOnScreen(file_paths[1], grayscale=True, confidence=0.9)
    py.click(py.center(btn_abrir))


def enviar_email(img_file_name=r'\anexo.png'):
    file_path = os.getcwd() + r'\py_utilitarios' + img_file_name

    while not py.locateOnScreen(file_path, grayscale=True, confidence=0.9):
        sleep(1)

    py.shortcut('ctrl', 'enter')


def fechar_janela(img_file_name=r'\anexar.png'):
    file_path = os.getcwd() + r'\py_utilitarios' + img_file_name

    while py.locateOnScreen(file_path, grayscale=True, confidence=0.9):
        sleep(1)
    py.click(x=1341, y=8)
    py.click(x=793, y=404)    

