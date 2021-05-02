# crypto_ml 
Application using machine learning to predict cryptocurrency prices.\
App is connecting to Binance Exchange API, download data and saving them to database.\
The data is prepared for linear regression model to predict prices.\
Access to application function is allowed by api provided by Flask.\
Research for this application is presented in Jupyter-Nootebook file crypto_ml.ipynb\

# API 
App is using Binance Exchange API. All functions are availbe on https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md, but in this application we use only two

### Lexicon
symbol - cryptocurrency pair symbol (string)\
price - cryptocurrency price e.g. ETHBTC is ETH price in BTC (float)\
interval - time interval beetween prices (string) :\
  minutes -> 1m, 3m, 5m, 15m, 30m\
  hours -> 1h, 2h, 4h, 6h, 8h, 12h\
  days -> 1d, 3d\
  weeks -> 1w\
  months -> 1M\
money - buy value for trading simulation (float)\

### Show all cryptocurrency pairs
```
localhost:5000/crypto/ 
0	
  0	"ETHBTC" # symbol
  1	0.051335 # price
1	
  0	"LTCBTC"
  1	0.004742
...
```

### Show 1000 records for selected cryptocurrency and time interval
```
localhost:5000/crypto/<symbol>/<interval>/ # localhost:5000/crypto/BTCUSDT/1d/ 
0	
  0	6935 # Open 
  1	7150.46 # High
  2	6670 # Low
  3	6720.06 # Close
  4	45438.473501 # Volume
1	
  0	6720.63
  1	6721.54
  2	6123
  3	6285
  4	59550.536319
...
```
