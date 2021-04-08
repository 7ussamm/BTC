#!/usr/bin/python3.6

# __auther__    = "Hussam Ashraf"
# __copyright__ = "Copyright 2021"
# __license__   = "GPL"
# __version__   = "1.1.0"
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
    


def main():
    returnedVlaues = list(getCoin())
    coinName = returnedVlaues[0]
    coinPrice = round(returnedVlaues[1], 2)
    
    coinPrice = str(coinPrice)
    
    if len(str(coinPrice)) == 8:
        coinPrice = coinPrice[0:2] + ',' + coinPrice[2:]
    elif len(str(coinPrice)) < 8:
        coinPrice = coinPrice[0:1] + ',' + coinPrice[2:]
    else:
        coinPrice = coinPrice[0:3] + ',' + coinPrice[2:]
    
    
    msgToBeSent = f"""
                    * Hey 7usS .. Up to date {coinName} price is 
                //  $ {coinPrice}  //
                     
* Hola, 7usS .. El precio de {coinName} actualizado es
                //  $ {coinPrice}  // 
    
* Merhaba 7usS .. Güncel {coinName} fiyatı
                //  $ {coinPrice}  //
                    
                    """
    
    sendBotUpdate(msgToBeSent)

if __name__ == "__main__":
    try:
        main()
    except:
        pass
