from src.data.data_loader import load_data
from src.models.garch_model import estimate_volatility

assets = ["SPY", "QQQ", "TLT", "GLD", "VNQ"]

data = load_data(assets)

estimate_volatility(data)

print("GARCH Modell ausgeführt")