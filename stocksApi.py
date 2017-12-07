import requests

stockTime = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=60min&apikey=4NCAZA32OZVKB0L2"
fx = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=4NCAZA32OZVKB0L2"
crypto = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_INTRADAY&symbol=BTC&market=CNY&apikey=4NCAZA32OZVKB0L2"

#rStockTime = requests.get(stockTime)
#dataStockTime = rStockTime.json()
#print dataStockTime["Time Series (60min)"].keys()[0]
#print dataStockTime["Time Series (60min)"].values()[0]

#rFx = requests.get(fx)
#dataFx = rFx.json()
#print dataFx["Realtime Currency Exchange Rate"]["5. Exchange Rate"]

rCrypto = requests.get(crypto)
dataCrypto = rCrypto.json()
print dataCrypto["Time Series (Digital Currency Intraday)"].keys()[0]
print dataCrypto["Time Series (Digital Currency Intraday)"].values()[0]