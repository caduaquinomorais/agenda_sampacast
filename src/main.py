from config import config
from mensagens import *

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
                Parametros_Mensagem.retirada_datos_excel(config.excel_path)
            case '2':
                print('Teste email')
            case '3':
                print('Teste limpeza')
            case '4':
                break

        

if __name__ == "__main__":
    main_menu()