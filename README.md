# p2pb2bapi

Wrapper for P2PB2B exchange API.

## Installing

```
pip install p2pb2bapi
```

## How to use

```
from p2pb2bapi import P2PB2B
client = P2PB2B(apiKey, apiSecret)
```

### /api/v1/public/markets

```
result = client.getMarkets()
```

### /api/v1/public/ticker

```
result = client.getTicker(market = 'ETH_USD')
```

### /api/v1/order/newOrder

```
result = client.newOrder(
    market = 'ETH_USD',
    side = 'sell',
    amount = '1',
    price = '10'
)
```

## Documentation

Coming soon ...
