#!/usr/bin/env python
# coding: utf-8

# # proyecto Actinver 2023
# ## bibliografia
# ### Enlaces utiles para obtener ideas de que estrategia tomar
# 
# 
# 
# **Cuando los físicos asaltaron los mercados: pagina 597** 
# [Enlace al libro](https://vittaquant-ai.com/wp-content/uploads/2021/08/CuandolosFisicosasaltaronlosmercados..pdf)
# 
# 
# **REPOSITORIO de yfinance**
# [Enlace al repositorio( solo esta como obtener datos historicos)](https://github.com/manursanchez/Practicas_Python_DataScience/blob/main/1.%20Pr%C3%A1ctica%20en%20el%20uso%20de%20la%20librer%C3%ADa%20yfinance.ipynb)
# 
# 
# **trading algoritmico**
# [Enlace a pagina de wikipedia](https://en.wikipedia.org/wiki/Algorithmic_trading)
# 
# *notas*
# 
# 
#        
#         

# In[ ]:


pip install yfinance


# In[ ]:


pip install pandas


# In[ ]:


import yfinance as yf


# In[13]:


from IPython.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


# In[ ]:


import pandas as pd


# In[ ]:


pip install tabulate termcolor


# In[19]:


import yfinance as yf
import matplotlib.pyplot as plt
from tabulate import tabulate

# Lista de acciones
acciones = ["AAL", "AAPL", "AAU", "ABBV", "ABNB", "AC", "AFRM", "AGNC", "ALFA", "ALPEK", "AMAT", "AMD", "AMX", "AMZN", "APA", "ASUR", "ATER", "ATOS", "ALSEA", "AX", "BA", "BABA", "BAC", "BBAJIO", "BBBY", "BIMBO", "BMY", "BNGO", "BRKB", "BYND", "CAT", "CCL", "CEMEX", "CHDRAUI", "CLF", "COST", "CPE", "F", "FANG", "FCX", "FDX", "FEMSA", "FIBRAMQ", "FIBRAPL", "FSLR", "FUBO", "FUNO", "GAP", "GCARSO", "GCC", "GENTERA", "GE", "GFINBUR", "GFNORTE", "GILD", "GMEXICO", "GOLD", "GOOGL", "GRUMA", "HD", "INTC", "JNJ", "JPM", "KIMBER", "KOF", "KO", "LAB", "LASITE", "LCID", "LIVEPOL", "LLY", "LUV", "LVS", "LYFT", "MA", "MARA", "MCD", "MEGA", "MELI", "META", "MGM", "MRK", "MRNA", "MRO", "MSFT", "MU", "NCLH", "NFLX", "NKE", "NKLA", "NU", "NVAX", "NVDA", "OMA", "ORBIA", "ORCL", "OXY", "PARA", "PBR", "PE&OLES", "PEP", "PFE", "PG", "PINFRA", "PLTR", "PYPL", "QCOM", "Q", "RCL", "RIOT", "RIVN", "ROKU", "R", "SBUX", "SHOP", "SITES1", "SKLZ", "SOFI", "SPCE", "SQ", "T", "TAL", "TERRA", "TGT", "TLEVISA", "TMO", "TSLA", "TSM", "TWLO", "TX", "T", "UAL", "UBER", "UNH", "UPST", "V", "VESTA", "Volaris", "VZ", "WALMEX", "WFC", "WISH", "WMT", "WYNN", "X", "XOM", "ZM"]

# Configurar subgráficos y tabla
fig, axs = plt.subplots(len(acciones), 1, figsize=(10, 2*len(acciones)), sharex=True)
tabla_data = []

for i, symbol in enumerate(acciones):
    try:
        # Obtener datos históricos
        data = yf.download(symbol, start="2023-06-01", end="2023-10-08")   
    
        # Graficar precio de cierre
        axs[i].plot(data['Close'], label=f'{symbol} - Precio de cierre', color='blue')

        # Graficar precio de apertura
        axs[i].plot(data['Open'], label=f'{symbol} - Precio de apertura', color='orange')

        # Línea de tendencia
        slope = (data['Close'].iloc[-1] - data['Close'].iloc[0]) / len(data)
        trend_label = 'Alcista' if slope > 0 else 'Bajista'
        axs[i].text(data.index[-1], data['Close'].iloc[-1], trend_label, fontsize=12, color='green')

        axs[i].set_title(f"Tendencia de {symbol}")
        axs[i].set_ylabel("Precio")
        axs[i].legend()

        # Agregar datos a la tabla
        tabla_data.append([symbol, trend_label])

    except Exception as e:
        print(f"Error obteniendo datos para {symbol}: {e}")
        continue  # Si hay un error, continúa con la siguiente acción

# Ajustar diseño y mostrar gráfico
plt.tight_layout()
plt.show()

# Imprimir tabla
headers = ['Acción', 'Tendencia']
print(tabulate(tabla_data, headers=headers, tablefmt='grid'))


# In[ ]:




