import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Definir o caminho do arquivo Excel contendo os dados de inflação
caminho = r"C:\Users\Vitória\Downloads\dados_inf.xlsx"

# Crio o dataframe df onde carregarei a planilha Excel
df = pd.read_excel(caminho)

# Criar uma coluna de data a partir do ano
df['data'] = pd.to_datetime(df['ano'], format='%Y')
df.set_index('data', inplace=True)

# Calcular a média móvel de 3 anos
df['media_movel'] = df['inflação'].rolling(window=3).mean()

# Plotar a inflação ao longo do tempo
plt.figure(figsize=(10, 6))

# Plotar os dados originais de inflação
plt.plot(df.index, df['inflação'], label='Inflação', color='green', linewidth = 3)

# Plotar a média móvel
plt.plot(df.index, df['media_movel'], label='Média Móvel (3 anos)', color='blue', linestyle='--', linewidth = 1)

# Adicionar linha de tendência
coeficientes = np.polyfit(df.index.year, df['inflação'], 1)
tendencia = np.poly1d(coeficientes)
plt.plot(df.index, tendencia(df.index.year), label='Linha de Tendência', color='red', linestyle='--', linewidth = 1)

# Nomear os eixos do gráfico
plt.xlabel('Ano')
plt.ylabel('Inflação')

# Entitular o gráfico
plt.title('Inflação ao longo do tempo no Brasil no Século XXI')

# Mostrar a legenda no gráfico
plt.legend()

# Mostrar as grades no gráfico
plt.grid(True, color="gray")

# Configurar o limite do eixo x, datas, de 99 a 2022
plt.xlim(pd.Timestamp('1999-01-01'), pd.Timestamp('2022-12-31'))

# Adicionar um texto dizendo a fonte dos dados
plt.text(pd.Timestamp('1997-01-01'), df['inflação'].min() * 0.4, 'Fonte de Dados: IBGE', fontsize=10, color='gray', horizontalalignment='left')

# Mostrar o gráfico
plt.show()
