# crypto_ml 
Application using machine learning to predict cryptocurrency prices from Binance Exchange API.\
App also allow to simulate trading based on predicted moves.\
Application functions are made available in API form using the Flask library\

Research for this application is presented in Jupyter-Nootebook file crypto_ml.ipynb

# API 
App is using Binance Exchange API. All functions are availbe on https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md, but in this application we use only two

### Lexicon
symbol - cryptocurrency pair symbol (string)\
price - cryptocurrency price e.g. ETHBTC is ETH price in BTC (float)\
interval - time interval beetween prices (string) :
 * minutes -> 1m, 3m, 5m, 15m, 30m
 * hours -> 1h, 2h, 4h, 6h, 8h, 12h
 * days -> 1d, 3d
 * weeks -> 1w
 * months -> 1M

money - buy value for trading simulation (float)

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
localhost:5000/crypto/<symbol>/<interval>/ # e.g. localhost:5000/crypto/BTCUSDT/1d/ 
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
### Predict next price for selected cryptocurrency and time interval
```
localhost:5000/crypto/<symbol>/<interval>/predict/ # e.g. localhost:5000/crypto/BTCUSDT/1d/predict/ 
0	57797.35 # Open
1	57911.02 # High
2	56035.25 # Low
3	56762.73 # Close
4	57126.5875 # Mean
5	56563.34535026978 # Predicted next price
6	"Stay" # Recommended move
```
### Simulate trading for all predicted "Buy" moves in 1000 records
```
localhost:5000/crypto/<symbol>/<interval>/<float:money>/simulation/ # e.g. localhost:5000/crypto/BTCUSDT/1d/100.0/simulation/ 
0	0 # Ignore
1	543 # "Buy" count 
2	6.7323972146730275 # Bought crypto
3	54300 # Money spend
4	57118.945 # Current crypto price
5	384547.43 # Fortune
6	330247.43 # Profit
7	608.19 # Rate of return
```
