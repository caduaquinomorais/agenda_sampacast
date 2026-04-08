import time
import pandas as pd
from datetime import date, datetime
from urllib.parse import quote
import webbrowser
import logging

COL_NOME     = "Usuário - Nome"
COL_TELEFONE = "Usuário - Telefone"
COL_UNIDADE  = "Unidade"
COL_HORARIO  = "Horário Início"

def generate_link(phone_number, message, ddi="55"):
    """
    Gerar link de whatsapp limpo e padronizado.
    :param phone: Número com ou sem a formatação.
    :param message: Texto da mensagem.
    :param ddi: Código do país.
    """
    phone_number = ''.join(c for c in str(phone_number) if c.isdigit())
    encoded_msg = quote(message)
    final_number = phone_number if phone_number.startswith(ddi) else f"{ddi}{phone_number}"
    encoded_message = quote(message)
    
    return f"https://wa.me/{final_number}/?text={encoded_message}"

#Log simples
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

def send_messages_from_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        for index, row in df.iterrows():
            name = str(row[COL_NOME]).split()[0].title()
            phone_number = str(row[COL_TELEFONE])
            unid = str(row[COL_UNIDADE])
            
            if isinstance(row[COL_HORARIO], str):
                hora = datetime.strptime(row[COL_HORARIO], '%H:%M:%S')
                horario = hora.strftime('%H:%M')
            else:
                horario = row[COL_HORARIO].strftime('%H:%M')

            message = (f"Olá, {name}! Bom dia!\n\n"
                    f"Nós da ADE SAMPA entramos em contato para confirmar sua agenda para amanhã às *{horario}* na unidade *{unid}*.\n\n"
                    "*Precisa cancelar?*\n"
                    "É obrigatório acessar o sistema e realizar o cancelamento manualmente. O não comparecimento sem cancelamento prévio gera penalidades.\n\n"
                    "É fundamental que você conheça nosso manual de conduta. Acesse aqui: https://adesampa.com.br/wp-content/uploads/2025/11/Manual-de-conduta-unificado.pdf \n\n"
                    "Agradecemos a atenção e até amanhã!")
            messages_browser(phone_number, message)

    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo Excel: {e}")

if __name__ == "__main__":
    file_path = r'agenda.xlsx'
    send_messages_from_excel(file_path)