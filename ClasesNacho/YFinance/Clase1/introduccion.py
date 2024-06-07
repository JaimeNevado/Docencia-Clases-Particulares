import yfinance as yf
import matplotlib.pyplot as plt


ticker = yf.Ticker("AAPL")

#Obtener la informacion de la empresa
informacion = ticker.info

archivo = open("apple_info.txt", "w")

#archivo.write(str(informacion))

#print(informacion["address1"])

# Datos históricos de la empresa
# ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
hist = ticker.history(period="1y")

fechas = []
valores = hist["Close"].tolist()

longitud = len(valores)

for i in range (0, longitud):
	fechas.append(str(i))


plt.plot(fechas, valores)
plt.xlabel("Dias")
plt.ylabel("Precio")
plt.title("Valores de Apple")

plt.show()


