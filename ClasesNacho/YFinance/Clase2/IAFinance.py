import yfinance as yf
import matplotlib.pyplot as plt
from libreriaIA import *

def analizarCompra(nombre, tiempo):
	ticker = yf.Ticker(nombre)
	hist = ticker.history(period=tiempo)
	valores = hist["Close"].tolist()
	print("Analisis de : ", nombre, ": ")
	archivo = open("precondiciones.txt", "r")
	lectura = archivo.readlines()

	archivo = open(f"{nombre}.txt", "r")
	analisis = archivo.readlines()

	resultado = chatGPT(analisis, lectura)
	print(resultado)
	return resultado

# Datos históricos de la empresa
# ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
#listaRec = []

#listaRec.append(analizarCompra("AAPL", "1y"))
#listaRec.append(analizarCompra("TSLA", "1y"))
#listaRec.append(analizarCompra("NVDA", "1y"))



#leyenda = ["AAPL", "TSLA", "NVDA"]

#plt.bar(leyenda, listaRec)
#plt.show()

analizarCompra("AAPL", "1y")
