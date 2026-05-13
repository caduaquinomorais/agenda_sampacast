import pandas as pd
from config import config

class gestao_dados:
    def Leitura_dados(file_path):
        try:
            df = pd.read_excel(file_path)
            for i, row in df.iterrows():
                name =str