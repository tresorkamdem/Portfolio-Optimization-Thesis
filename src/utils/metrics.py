import numpy as np

def portfolio_performance(weights, returns):
    mean_returns = returns.mean() * 252
    cov_matrix = returns.cov() * 252

    ret = np.dot(weights, mean_returns)
    risk = np.sqrt(weights.T @ cov_matrix @ weights)

    return ret, risk