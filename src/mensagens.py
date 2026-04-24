def retirada_datos_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        for i, row in df.iterrows():
            name =str(row[COL_NOME]).split()[0].title()
            phone_number = str(row[COL_TELEFONE])
            unid = str(row[COL_UNIDADE])

            if isinstance(row[COL_HORARIO], str):
                hora = datetime.strptime(row[COL_HORARIO], '%H:%M:%S')
                hora = hora.strftime('%H:%M')
            else:
                hora = row[COL_HORARIO].strftime('%H:%M')
    except Exception as e:
        print('Ocorreu um erro ao processar os dados de entrada da mensagem: {e}')
        