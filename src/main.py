import time
import pandas as pd
from datetime import date, datetime
from urllib.parse import quote
import webbrowser
import logging
import os
from config import config


def generate_link(phone_number, message, ddd=config.ddi):
    """
    Gerar link de whatsapp limpo e padronizado.
    :param phone: Número com ou sem a formatação.
    :param message: Texto da mensagem.
    :param ddi: Código do país.
    """
    phone_number = ''.join(c for c in str(phone_number) if c.isdigit())
    encoded_msg = quote(message)
    final_number = phone_number if phone_number.startswith(ddd) else f"{ddi}{phone_number}"
    encoded_message = quote(message)
    
    return f"https://wa.me/{final_number}/?text={encoded_message}"

logging.basicConfig(level=logging.INFO)

def messages_browser(phone_number, message):
    """
    Abrir link de whatsapp com mensagem pronta.
    :param phone: Número com ou sem a formação.
    :param message: Texto da mensagem.
    """
    try:
        link = generate_link(phone_number, message)
        logging.info(f"Iniciando envio para: {phone_number}")

        webbrowser.open(link)
        time.sleep(1)

    except Exception as e:
        logging.error(f"Erro ao tentar abrir o navegador: {e}")

def saudacao_horario():
    now = datetime.now().time()
    if now < datetime.strptime("13:00:00", "%H:%M:%S").time():
        return "Bom dia"
    else:
        return "Boa tarde"

def send_messages_from_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        for index, row in df.iterrows():
            name = str(row[config.COL_NOME]).split()[0].title()
            phone_number = str(row[config.COL_TELEFONE])
            unid = str(row[config.COL_UNIDADE])
            
            if isinstance(row[config.COL_HORARIO], str):
                hora = datetime.strptime(row[config.COL_HORARIO], '%H:%M:%S')
                horario = hora.strftime('%H:%M')
            else:
                horario = row[config.COL_HORARIO].strftime('%H:%M')

            message = (f"Olá, {name}! {saudacao_horario()}!\n\n"
                    f"Nós da ADE SAMPA entramos em contato para confirmar sua agenda para amanhã às *{horario}* na unidade *{unid.strip()}*.\n\n"
                    "*Precisa cancelar?*\n"
                    "É obrigatório acessar o sistema e realizar o cancelamento manualmente. O não comparecimento sem cancelamento prévio gera penalidades.\n\n"
                    "É fundamental que você conheça nosso manual de conduta. Acesse aqui: {config.manual_link}\n\n"
                    "Agradecemos a atenção e até amanhã!")
            messages_browser(phone_number, message)

    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo Excel: {e}")


def main_menu():
    while True:
        print('\n*** Menu de mensageria e limpeza de relatórios ***\n')
        print('1 - Para enviar mensagens via whatsapp')
        print('2 - Para enviar mensagens via email')
        print('3 - Limpeza de relatórios')
        print('4 - Sair')

        opcao = input('Qual a opção desejada? ')

        match opcao:
            case '1':
                send_messages_from_excel(config.excel_path)
            case '2':
                print('Teste email')
            case '3':
                print('Teste limpeza')
            case '4':
                break

        

if __name__ == "__main__":
    config.excel_path
    main_menu()