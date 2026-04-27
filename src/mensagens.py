from datetime import datetime
from time import sleep, time
import logging
from urllib.parse import quote
from config import config
import pandas as pd
import webbrowser

logging.basicConfig(level=logging.INFO)

class Parametros_Mensagem:
    def retirada_datos_excel(file_path):
        try:
            df = pd.read_excel(file_path)
            for i, row in df.iterrows():
                name =str(row[config.COL_NOME]).split()[0].title()
                phone_number = str(row[config.COL_TELEFONE])
                unid = str(row[config.COL_UNIDADE])

                if isinstance(row[config.COL_HORARIO], str):
                    hora = datetime.strptime(row[config.COL_HORARIO], '%H:%M:%S')
                    hora = hora.strftime('%H:%M')
                else:
                    hora = row[config.COL_HORARIO].strftime('%H:%M')

                mensagem = Mensagens.mensagem_personalizada(name, unid, hora)
                Parametros_Mensagem.messages_browser(phone_number, mensagem)
        
        except Exception as e:
            print(f'Ocorreu um erro ao processar os dados de entrada da mensagem: {e}')
        
    def messages_browser(phone_number, message):
        """
        Abrir link de whatsapp com mensagem pronta.
        :param phone: Número com ou sem a formação.
        :param message: Texto da mensagem.
        """
        try:
            link = Mensagens.generate_link(phone_number, message)
            logging.info(f"Iniciando envio para: {phone_number}")

            webbrowser.open(link)
            sleep(1)

        except Exception as e:
            logging.error(f"Erro ao tentar abrir o navegador: {e}")

class Mensagens:
    def generate_link(phone_number, message, ddd=config.ddd):
        """
        Gerar link de whatsapp limpo e padronizado.
        :param phone: Número com ou sem a formatação.
        :param message: Texto da mensagem.
        :param ddi: Código do país.
        """
        phone_number = ''.join(c for c in str(phone_number) if c.isdigit())
        final_number = phone_number if phone_number.startswith(ddd) else f"{ddd}{phone_number}"
        encoded_message = quote(message)
        
        return f"https://wa.me/{final_number}/?text={encoded_message}"

    def saudacao_horario():
        now = datetime.now().time()
        if now < datetime.strptime("13:00:00", "%H:%M:%S").time():
            return "Bom dia"
        else:
            return "Boa tarde"

    def mensagem_personalizada(name, unid, horario):
        return (f"Olá, {name}! {Mensagens.saudacao_horario()}!\n\n"
                        f"Nós da ADE SAMPA entramos em contato para confirmar sua agenda para amanhã às *{horario}* na unidade *{unid.strip()}*.\n\n"
                        "*Precisa cancelar?*\n"
                        "É obrigatório acessar o sistema e realizar o cancelamento manualmente. O não comparecimento sem cancelamento prévio gera penalidades.\n\n"
                        f"É fundamental que você conheça nosso manual de conduta. Acesse aqui: {config.MANUAL_URL}\n\n"
                        "Agradecemos a atenção e até amanhã!")
    