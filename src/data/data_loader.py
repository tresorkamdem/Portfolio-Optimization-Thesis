import yfinance as yf

def load_data(assets, start="2020-01-01", end="2025-01-01"):
    data = yf.download(assets, start=start, end=end)["Close"]
    returns = data.pct_change().dropna()
    return returns
