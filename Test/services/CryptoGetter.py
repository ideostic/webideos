from urllib import request
import json


urlPriceBase = '/data/price?fsym={0}&tsyms={1}&e={2}&extraParams={3}'
urlbase = 'https://www.cryptocompare.com'
allCoins = '/api/data/coinlist/'
exchange = 'Coinbase'
app = 'IDEOS'
usd = 'USD'

imageHTML_Prefix = '<img src="{0}" '
imageHTML_alt = alt=' alt="{0}"> '


def getCryptoData(url):
    ret = request.urlopen(url)
    encoding = ret.info().get_content_charset('utf-8')
    data = ret.read()
    docodedData = data.decode(encoding)
    data_string = json.dumps(docodedData)
    return json.loads(json.loads(data_string))


def generateInfoLabel():
    returned_Data = getCryptoData(urlbase + allCoins)
    # base_url = returned_Data['BaseLinkUrl']
    cryptoData = returned_Data['Data']
    allCoinsLabel = ''
    coins = {'BTC', 'LTC', 'ETH'}
    for key in coins:
        url_price = urlPriceBase.format(key, usd, exchange, app)
        price = getCryptoData('https://min-api.cryptocompare.com{0}'.format(url_price))
        image_url = '{0}?width=25'.format(returned_Data['BaseImageUrl'] + cryptoData[key]['ImageUrl'])
        allCoinsLabel += getImageLabel(image_url, price, cryptoData[key])
    # End for
    return allCoinsLabel


def getImageLabel(image_url, price, value):
    exvalue = price[usd]
    imagehtmlPrefix = imageHTML_Prefix.format(image_url)
    imageSubFix = imageHTML_alt.format(value['Name'])
    finalImage = imagehtmlPrefix + imageSubFix
    coinLabel = finalImage + value['CoinName'] + ' = ' + str(exvalue) + ' ' + usd + '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
    return coinLabel


# print(generateInfoLabel())
