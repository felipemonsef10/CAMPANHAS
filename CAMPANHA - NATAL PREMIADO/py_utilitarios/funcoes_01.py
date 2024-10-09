from datetime import date
import pandas as pd
import PyPDF2 as pyf
from pathlib import Path
import os
from pdf2image import convert_from_path
from PIL import Image


def calcula_tempo_campanha(ano=2024, dia_inicial=1, mes_inicial=10, dia_final=31, mes_final=12):
    data_atual = date.today()

    data_inicio = date(ano, mes_inicial, dia_inicial)

    data_fim = date(ano, mes_final, dia_final)

    dias_totais_campanha = (data_fim - data_inicio).days

    dias_decorridos_campanha = (data_atual - data_inicio).days

    percentagem_tempo_decorrido_campanha = int(round(dias_decorridos_campanha / dias_totais_campanha * 100, 0))

    return f'{percentagem_tempo_decorrido_campanha}%'


def ler_corpo_emails(path):
    with open(path, 'r+', encoding='utf-8') as file:
        corpo_email = file.read()

        # if 'diretor' in name_file:
        #     corpo_email = corpo_email.format(tempo_decorrido)
        # else:
        #     corpo_email = corpo_email.format(nome_destinaratio, tempo_decorrido)

    file.close
        
    return corpo_email


# def ler_emails_copia(txt_file):
#     with open(txt_file, 'r+') as emails:
#         list_emails = list(map(lambda s: s.removesuffix('\n'), emails.readlines()))

#     emails_copia = list_emails

#     return emails_copia


def ler_msg_wpp(tempo_decorrido, file_path):
    with open(file_path, 'r+', encoding='utf8') as text:
        msg = text.read().format(tempo_decorrido)

    text.close()

    # msg = ''.join(msg).format(tempo_decorrido)

    return msg


def separar_pdf_area(texto_chave, path_file_orig, path_dest):
    arquivo_pdf_junto = pyf.PdfReader(path_file_orig)

    for index, pagina in enumerate(arquivo_pdf_junto.pages):
        novo_pdf = pyf.PdfWriter()
        novo_pdf.add_page(pagina)

        texto_pagina = pagina.extract_text()
        
        if texto_chave in texto_pagina:
            with Path(path_dest + rf'\{texto_chave} PARCIAL.pdf').open(mode='wb') as arquivo:
                novo_pdf.write(arquivo)

            arquivo.close()


def juntar_pdf(df_supervisores, path=r'D:\Perfil\Desktop\PROJETOS EMPRESA\NEI\CAMPANHA\CAMPANHA - AQUECENDO VENDAS\PDFS_SEPARADOS'):
    arquivos_pdfs_separados = os.listdir(path)

    areas = df_supervisores['AREA'].unique().tolist()
    for area in areas:
        novo_arquivo = pyf.PdfWriter()

        for arq in arquivos_pdfs_separados:
            if area in arq:
                pagina_pdf = pyf.PdfReader(f'{path}\{arq}')
                novo_arquivo.add_page(pagina_pdf.pages[0])

            for index in df_supervisores.index:
                regiao = df_supervisores.loc[index, 'REGIAO']
                area_ = df_supervisores.loc[index, 'AREA']

                if area_ == area:
                    if regiao in arq:
                        pagina_pdf = pyf.PdfReader(f'{path}\{arq}')
                        novo_arquivo.add_page(pagina_pdf.pages[0])


        with Path(fr'D:\Perfil\Desktop\PROJETOS EMPRESA\NEI\CAMPANHA\CAMPANHA - AQUECENDO VENDAS\ARQUIVOS BASE\RESULTADOS_PDF\RESULTADOS GERAIS - {area}.pdf').open(mode='wb') as arquivo:
            novo_arquivo.write(arquivo)


def criar_imgs_do_pdf(caminho_arquivos_pdfs, caminho_arquivos_img):
    while True:
        list_arquivos_pdfs = os.listdir(caminho_arquivos_pdfs)
        if len(list_arquivos_pdfs) == 0:
            print('PASTA VAZIA AINDA')
        else:
            break
    
    if len(os.listdir(caminho_arquivos_img)) == 0:
        for arq in list_arquivos_pdfs:
            if 'RG' in arq:
                # Caminho para o arquivo PDF
                pdf_path = caminho_arquivos_pdfs + rf'\{arq}'

                # Caminho para salvar a imagem
                arq = arq.replace('pdf', 'jpg')
                output_image_path = caminho_arquivos_img + rf'\{arq}'

                # Caminho para a pasta 'bin' do poppler
                poppler_path = r'D:\Perfil\Desktop\PYTHON\POPPLER\poppler-24.02.0\Library\bin'  # Ajuste conforme o seu ambiente

                # Definindo a resolução (DPI)
                dpi = 300

                # Convertendo a primeira página do PDF em uma lista de imagens com DPI ajustado
                images = convert_from_path(pdf_path, dpi=dpi, poppler_path=poppler_path)

                # Coordenadas da área a ser recortada (left, upper, right, lower)
                # Ajuste os valores conforme necessário
                left = 50
                upper = 50
                right = 3500
                lower = 1600

                # Salvando a área recortada da primeira página como imagem
                if images:
                    # Recortar a área desejada
                    cropped_image = images[0].crop((left, upper, right, lower))
                    
                    # Salvar a imagem recortada
                    cropped_image.save(output_image_path, 'JPEG')
                    print(f'A imagem da área selecionada foi salva em {output_image_path}.')
                else:
                    print('Não foi possível converter o PDF.')

    else:
        print('ARQUIVOS IMG JÁ EXISTENTES!')


def apagar_imgs(caminho_arquivos_imgs):
    for pnj in os.listdir(caminho_arquivos_imgs):
        os.remove(caminho_arquivos_imgs + f'\{pnj}')


def abrir_programa(caminho_arquivo=r"C:\Program Files\Mozilla Thunderbird\thunderbird.exe"):
    os.startfile(caminho_arquivo)

