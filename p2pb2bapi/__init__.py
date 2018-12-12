import requests

class P2PB2B:
    BASE_URL = 'https://p2pb2b.io'
    API_V1_URL = BASE_URL + '/api/v1'
    METHODS = {
        'markets': API_V1_URL + '/public/markets',
        'tickers': API_V1_URL + '/public/tickers',
        'ticker': API_V1_URL + '/public/ticker',
        'book': API_V1_URL + '/public/book',
        'history': API_V1_URL + '/public/history',
        'historyResult': API_V1_URL + '/public/history/result',
        'products': API_V1_URL + '/public/products',
        'symbols': API_V1_URL + '/public/symbols',
        'depth': API_V1_URL + '/public/depth/result',
        'newOrder': API_V1_URL + '/order/new',
        'cancelOrder': API_V1_URL + '/order/cancel',
        'orders': API_V1_URL + '/orders',
        'balances': API_V1_URL + '/account/balances',
        'balance': API_V1_URL + '/account/balance',
        'order': API_V1_URL + '/account/order',
        'orderHistory': API_V1_URL + '/account/order_history'
    }

    def __init__(self, apiKey, apiSecret):
        self.apiKey = apiKey
        self.apiSecret = apiSecret

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

    def _getRequest(self, url, params = None):
        response = requests.get(url, params = params)
        return response.json()

    def _postRequest(self, url, data = None):
        response = requests.post(url, data = data)
        return response.json()
