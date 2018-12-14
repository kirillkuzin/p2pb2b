import requests
import json
import base64
import hmac
import hashlib
import time

class P2PB2B:
    BASE_URL = 'https://p2pb2b.io'
    API_V1_URL = '/api/v1'
    METHODS = {
        'markets': '/public/markets',
        'tickers': '/public/tickers',
        'ticker': '/public/ticker',
        'book': '/public/book',
        'history': '/public/history',
        'historyResult': '/public/history/result',
        'products': '/public/products',
        'symbols': '/public/symbols',
        'depth': '/public/depth/result',
        'newOrder': '/order/new',
        'cancelOrder': '/order/cancel',
        'orders': '/orders',
        'balances': '/account/balances',
        'balance': '/account/balance',
        'order': '/account/order',
        'orderHistory': '/account/order_history'
    }

    def __init__(self, apiKey, apiSecret):
        self.apiKey = apiKey
        self.apiSecret = apiSecret.encode()

    ################################################
    #
    # PUBLIC API
    #
    ################################################

    def getMarkets(self):
        return self._getRequest(self.METHODS['markets'])

    def getTickers(self):
        return self._getRequest(self.METHODS['tickers'])

    def getTicker(self, market):
        params = {'market': market}
        return self._getRequest(self.METHODS['ticker'], params)

    def getBook(self, market, side, offset = 0, limit = 50):
        params = {
            'market': market,
            'side': side,
            'offset': offset,
            'limit': limit
        }
        return self._getRequest(self.METHODS['book'], params)

    def getHistory(self, market, lastId, limit = 50):
        params = {
            'market': market,
            'lastId': lastId,
            'limit': limit
        }
        return self._getRequest(self.METHODS['history'], params)

    def getHistoryResult(self, market, since, limit = 50):
        params = {
            'market': market,
            'since': since,
            'limit': limit
        }
        return self._getRequest(self.METHODS['historyResult'], params)

    def getProducts(self):
        return self._getRequest(self.METHODS['products'])

    def getSymbols(self):
        return self._getRequest(self.METHODS['symbols'])

    def getDepth(self, market, limit = 50):
        params = {
            'market': market,
            'limit': limit
        }
        return self._getRequest(self.METHODS['depth'], params)

    ################################################
    #
    # MARKET API
    #
    ################################################

    def newOrder(self, market, side, amount, price):
        data = {
            'market': market,
            'side': side,
            'amount': amount,
            'price': price
        }
        return self._postRequest(self.METHODS['newOrder'], data)

    def cancelOrder(self, market, orderId):
        data = {
            'market': market,
            'orderId': orderId
        }
        return self._postRequest(self.METHODS['cancelOrder'], data)

    def getOrders(self, market, offset = 0, limit = 50):
        data = {
            'market': market,
            'offset': offset,
            'limit': limit,
        }
        return self._postRequest(self.METHODS['orders'], data)

    ################################################
    #
    # ACCOUNT API
    #
    ################################################

    def getBalances(self):
        return self._postRequest(self.METHODS['balances'])

    def getBalance(self, currency):
        data = {'currency': currency}
        return self._postRequest(self.METHODS['balance'], data)

    def getOrder(self, orderId, offset = 0, limit = 50):
        data = {
            'orderId': orderId,
            'offset': offset,
            'limit': limit
        }
        return self._postRequest(self.METHODS['order'], data)

    def getOrderHistory(self, offset = 0, limit = 50):
        data = {
            'offset': offset,
            'limit': limit
        }
        return self._postRequest(self.METHODS['orderHistory'], data)

    ################################################
    #
    # CALLS TO P2PB2B
    #
    ################################################

    def _getRequest(self, requestUrl, params = None):
        response = requests.get(
            url = self.BASE_URL + self.API_V1_URL + requestUrl,
            params = params
        )
        return response.json()

    def _postRequest(self, requestUrl, data = None):
        timestamp = str(time.time()).split('.')[0]
        baseData = {
            'request': self.API_V1_URL + requestUrl,
            'nonce': timestamp
        }
        if data is not None:
            data.update(baseData)
        else:
            data = baseData
        data = json.dumps(data, separators = (',', ':'))
        payload = base64.b64encode(data.encode())
        signature = hmac.new(self.apiSecret, payload, hashlib.sha512).hexdigest()
        payload = payload.decode()
        headers = {
            'Content-type': 'application/json',
            'X-TXC-APIKEY': self.apiKey,
            'X-TXC-PAYLOAD': payload,
            'X-TXC-SIGNATURE': signature
        }
        response = requests.post(
            url = self.BASE_URL + self.API_V1_URL + requestUrl,
            data = data,
            headers = headers
        )
        return response.json()
