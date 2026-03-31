from src.data.data_loader import load_data
from src.models.markowitz import optimize_portfolio
from src.utils.metrics import portfolio_performance

# Assets definieren
assets = ["SPY", "QQQ", "TLT", "GLD", "VNQ"]

# Daten laden
returns = load_data(assets)

# Optimierung durchführen
weights = optimize_portfolio(returns)

# Performance berechnen
ret, risk = portfolio_performance(weights, returns)

print("Optimale Gewichte:", weights)
print("Erwartete Rendite:", ret)
print("Risiko:", risk)