# Raja Tirumalasetty

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('seaborn')

while True:
    userTicker = input('Enter a ticker symbol to retrieve its stock information:')
    tickerData = yf.Ticker(userTicker)
    print("ticker data type", type(tickerData))
    print("ticker data.info", type(tickerData.info))

    tickerInfoSize = len(tickerData.info)
    print(tickerInfoSize)
    zipCode = tickerData.info.get('zip')
    if (zipCode == None):
        print('Your ticker was invalid, enter a valid ticker:')
    else:
        print(tickerData.info)

    userChoice = input("Would you like to look up another stock?:(Enter y/n)")
    userChoice = userChoice.upper()
    if (userChoice == 'Y'):
        continue
    else:
        exit(0)

while True:
    userChoice = input("Would you like to look up the specifics of a stock?:(Enter y/n)")
    userChoice = userChoice.upper()
    if (userChoice == 'Y'):
        userTicker2 = input('Enter a ticker symbol to retrieve its stock information:')
        tickerData2 = yf.Ticker(userTicker)
        userFunction = input('What specific data would you like to look up(ex: dividends, recomendations, splits, etc):')
        print(userTicker.userFunction)
        continue
    else:
        exit(0)


tickerName = yf.Ticker(userTicker)
stockinfo = userTicker.info

userPeriod = input('Enter the wanted time period/limits to create graph.')

df = userTicker.history(period = userPeriod)
plt.figure()
plt.plot(df('close'))
plt.show()



df = userTicker.dividends
print(df)
graphLimitX = input("Enter year limit for graph:")
graphLimitY = input("Enter year limits for graph:")

df = userTicker.dividends #returns a dataframe
data = df.resample('Y').sum() # sum dividends by year
data = data.reset_index()
data['Year'] = data['Data'].dt.year # create a new dataframe column for the year only 

plt.figure()
plt.bar(data['Year'], data['Dividends'])
plt.ylabel('Dividend Yield($)')
plt.xlabel('Year')
plt.title('Microsoft Dividend History')
plt.xlim(graphLimitX, graphLimitY)
plt.show()

def stockAnalyser(userTicker):
    earings = yf.download(userTicker)
    if(earings > 0):
        print(userTicker, "is a well performing stock:")
        print("This is a stock you should purchase:")
    else:
        print(userTicker, "is not a well preforming stock:")
        print("This is a stock you should not purchase:")
stockAnalyser()