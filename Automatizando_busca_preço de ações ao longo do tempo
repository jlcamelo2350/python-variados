## Basta chamar a função 'dados_portfolio()' e os preços das ações das maiores empresas listadas na B3 aparece pra vc em um arquivo xlsx (excel) na pasta de downloads

import pandas as pd
import yfinance as yf
import datetime
import os

def dados_portfolio():
    # Definir o intervalo de datas: de 01/01/2022 até 04/01/2024.
    start = datetime.datetime(2022, 1, 1)
    end = datetime.datetime(2024, 4, 1)

    # Lista de tickers das empresas
    tickers = ['ITUB4.SA', 'VALE3.SA', 'PETR4.SA', 'BBDC4.SA', 'B3SA3.SA', 'ABEV3.SA', 'PETR3.SA', 'BBAS3.SA', 'BBDC3.SA',
           'BBSE3.SA', 'RENT3.SA', 'ITSA4.SA', 'BBSE3.SA', 'LREN3.SA', 'JBSS3.SA', 'NTCO3.SA', 'GGBR4.SA', 'WEGE3.SA',
           'SUZB3.SA', 'IRBR3.SA', 'ELET3.SA', 'ELET6.SA', 'CSAN3.SA', 'BRML3.SA', 'CIEL3.SA', 'BRFS3.SA', 'CCRO3.SA',
           'HYPE3.SA', 'MRFG3.SA', 'SBSP3.SA', 'RAIL3.SA', 'EMBR3.SA', 'BTOW3.SA', 'BEEF3.SA', 'VVAR3.SA', 'TIMP3.SA',
           'EGIE3.SA', 'BRDT3.SA', 'CSNA3.SA', 'QUAL3.SA', 'USIM5.SA', 'MULT3.SA', 'GOLL4.SA', 'IRBR3.SA', 'HAPV3.SA',
           'EVEN3.SA', 'MGLU3.SA', 'CYRE3.SA', 'SBFG3.SA', 'MRVE3.SA', 'AZUL4.SA', 'YDUQ3.SA', 'CMIG4.SA', 'BRAP4.SA',
           'TOTS3.SA', 'CCXC3.SA', 'PCAR3.SA', 'ENEV3.SA', 'CRFB3.SA', 'UGPA3.SA', 'CVCB3.SA', 'CIEL3.SA', 'BRML3.SA',
           'BRKM5.SA', 'MRFG3.SA', 'CSMG3.SA', 'LAME4.SA', 'GOAU4.SA', 'UGPA3.SA', 'VIVT4.SA', 'HYPE3.SA', 'SMTO3.SA',
           'IRBR3.SA', 'MRVE3.SA', 'BIDI4.SA', 'QUAL3.SA', 'KLBN11.SA', 'SMLS3.SA', 'ECOR3.SA', 'EVEN3.SA', 'BBDC3.SA',
           'LREN3.SA', 'TAEE11.SA', 'TUPY3.SA', 'ECOR3.SA', 'HGTX3.SA', 'CMIG4.SA', 'BRAP4.SA', 'GGBR4.SA', 'SUZB3.SA',
           'ENBR3.SA', 'CVCB3.SA', 'IRBR3.SA', 'BRKM5.SA']

    # Criar um DataFrame vazio para armazenar os dados
    df = pd.DataFrame()

    # Baixar os dados de fechamento para cada empresa e armazenar no DataFrame df
    for ticker in tickers:
        try:
            data = yf.download(ticker, start=start, end=end)['Close']
            # Renomear a coluna do DataFrame para incluir o ticker. split é quebra
            df[ticker.split('.')[0]] = data
        except Exception as e:
            print(f"Erro ao baixar dados para {ticker}: {e}")

    # Resetar o índice para incluir a coluna de datas no DataFrame
    df.reset_index(inplace=True)

    # Mostrar as primeiras linhas do DataFrame
    print(df.head())

    # Salvar o DataFrame df para Excel na pasta de downloads do usuário
    caminho = os.path.join(os.path.expanduser('~'), 'Downloads')
    df.to_excel(os.path.join(caminho, 'portfólio_RV.xlsx'), index=False)

# Chamada da função
dados_portfolio()
