from src.data.data_loader import load_data
from src.models.ml_model import train_model

assets = ["SPY", "QQQ", "TLT", "GLD", "VNQ"]

data = load_data(assets)

train_model(data)

print("ML Modell ausgeführt")