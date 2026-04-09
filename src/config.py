

class config:

    #ARQUIVOS
    excel_path: Path = Path("data/agenda.xlsx")
    log_path: Path = Path(f"logs/whatsapp_{datetime.now().strftime('%Y%m')}.log")

    #PLANILHAS
    COL_NOME     = "Usuário - Nome"
    COL_TELEFONE = "Usuário - Telefone"
    COL_UNIDADE  = "Unidade"
    COL_HORARIO  = "Horário Início"

    #WhatsApp
    whatsapp_delay: float = 1.5
    ddi: str = "55"

DEFAULT_DDI = "55"
FILE_PATH = r"agenda.xlsx"
MANUAL_URL = "https://adesampa.com.br/wp-content/uploads/2025/11/Manual-de-conduta-unificado.pdf"

LOG_LEVEL = "INFO"