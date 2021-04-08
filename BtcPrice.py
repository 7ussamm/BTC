#!/usr/bin/python3.6

# __auther__    = "Hussam Ashraf"
# __copyright__ = "Copyright 2021"
# __license__   = "GPL"
# __version__   = "1.2.0"
# __status__    = "Active"

import requests 



## Link to Coin market cap API page
    ## https://pro.coinmarketcap.com/account
## Link to Telegram API page
    ## https://core.telegram.org/bots/api#authorizing-your-bot

# Global variables

CMC_apiKey = '93a7a6b3-7e08-44a9-8257-61e6f5ee5d51'  # CMC => Coin Market Cap
botToken = '1758373314:AAE1biaeJu9S-rS4vJOaW8Y2pWS6h-i8p2I'
telegramID = '166507989'


# Starting functions 

def getCoin():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':'1',
        'limit':'1',
        'convert':'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': CMC_apiKey,
    }

    response = requests.get(url, headers=headers, params=parameters).json()
    
    coinName = response['data'][0]['name']
    coinPrice = response['data'][0]['quote']['USD']['price']
    
    return coinName, coinPrice


''' for key, value in getCoin()['data'][0].items():
    print('"{}"'.format(key))
    print(value) '''
    

def sendBotUpdate(msg):
    url = f'https://api.telegram.org/bot{botToken}/sendMessage?chat_id={telegramID}&text={msg}'
    requests.get(url)
    

def currencyConverter():
    
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    
    data = requests.get(url).json()

    coins = data['rates']
        
    Egp, Eur, Try = coins['EGP'], coins['EUR'], coins['TRY'] 
    
    return Egp, Eur, Try
            

def main():
    btcNamePrice = list(getCoin())
    currencyPrices = list(currencyConverter())
    
    coinName = btcNamePrice[0]
    coinPriceUSD = btcNamePrice[1]
    
    
    coinPriceEGP = str(round(coinPriceUSD * currencyPrices[0]))
    coinPriceEUR = str(round(coinPriceUSD * currencyPrices[1]))
    coinPriceTRY = str(round(coinPriceUSD * currencyPrices[2]))
    
    coinPriceUSD = str(round(btcNamePrice[1]))
    
    dictOfCurrencies = {
        "USD" : coinPriceUSD, 
        "EGP" : coinPriceEGP,
        "EUR" : coinPriceEUR, 
        "TRY" : coinPriceTRY
    }
    
    listOfCoins = {}
    
    for coin in dictOfCurrencies:
    
        if len(dictOfCurrencies[coin]) == 5:
            listOfCoins[coin] = (dictOfCurrencies[coin][0:2] + ', ' + dictOfCurrencies[coin][2:])
            
        elif len(dictOfCurrencies[coin]) < 5:
            listOfCoins[coin] = (dictOfCurrencies[coin][0:1] + ', ' + dictOfCurrencies[coin][1:])
            
        else:
            listOfCoins[coin] = (dictOfCurrencies[coin][0:3] + ', ' + dictOfCurrencies[coin][3:])
            
    
    msgToBeSent = f"""
    
                    ********* بقولك يامعلم .. سعر البيتكوين حالياّ *********
                    //  £ {listOfCoins["EGP"]}  //
                                
* Hey there Boss .. Up to date {coinName} price is 
                    //  $ {listOfCoins["USD"]}  //
                          
* Hola, Jefe .. El precio de {coinName} actualizado es
                    //  € {listOfCoins["EUR"]}  // 
    
* Merhaba Önder .. Güncel {coinName} fiyatı
                    //  $ {listOfCoins["TRY"]}  //
                
                    """
    
    sendBotUpdate(msgToBeSent)

if __name__ == "__main__":

    try:
        main()
    except:
        pass
