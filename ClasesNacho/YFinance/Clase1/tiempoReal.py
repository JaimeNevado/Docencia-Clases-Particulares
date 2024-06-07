import yfinance as yf

archivo = open("apple.csv", "w")

ticker = yf.Ticker("AAPL")
ticker2 = yf.Ticker("EURUSD")

cambio = 0.95

hist = ticker.history(period="1y")


for elemento in hist["Close"].tolist():
	print(round(elemento * cambio, 2), "euros")

