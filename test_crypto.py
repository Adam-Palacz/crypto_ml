from binance_api import download_historical_prices
import pytest

TEST_CRYPTO_SYMBOL_INTERVAL = (
    ('BTCUSDT', '1d'),
    ('ETHBTC', '1M'),
    ('LSKETH', '1m')
)


@pytest.mark.parametrize("symbol, interval", TEST_CRYPTO_SYMBOL_INTERVAL)
def test_download_historical_prices(symbol, interval):
    assert isinstance(symbol, str)
    assert isinstance(interval, str)
    assert download_historical_prices(symbol, interval) is not None
