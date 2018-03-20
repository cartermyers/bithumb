#This is the original __init__ file,
# modified to only include the class we want

#from bitfinex import Bitfinex
#from bitstamp import Bitstamp
#from bitvc import BitVc
#from coinapult import Coinapult
from coindesk import CoinDesk
#from futures796 import Futures796
#from huobi import Huobi
#from kraken import Kraken
#from okcoin import OKCoin, OKCoinFutures
#from poloniex import Poloniex
#from bravenewcoin import BraveNewCoin

exchange_list = {
    #'bitfinex' : Bitfinex,
    #'bitstamp' : Bitstamp,
    #'bitvc' : BitVc,
    #'coinapult' : Coinapult,
    'coindesk' : CoinDesk,
    #'futures796' : Futures796,
    #'huobi' : Huobi,
    #'kraken' : Kraken,
    #'okcoin' : OKCoin,
    #'okcoin_futures' : OKCoinFutures,
    #'poloniex' : Poloniex,
    #'bravenewcoin' : BraveNewCoin
}

def get_exchange(s, *args, **kwargs):
    if s not in exchange_list:
        raise RuntimeError
    else:
        return exchange_list[s](*args, **kwargs)
