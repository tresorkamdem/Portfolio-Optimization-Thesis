import numpy as np
import scipy.optimize as sco

def portfolio_volatility(weights, mean_returns, cov_matrix):
    return np.sqrt(weights.T @ cov_matrix @ weights)

def optimize_portfolio(returns):
    mean_returns = returns.mean() * 252
    cov_matrix = returns.cov() * 252

    num_assets = len(mean_returns)

    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for _ in range(num_assets))

    initial_weights = num_assets * [1. / num_assets]

    result = sco.minimize(
        portfolio_volatility,
        initial_weights,
        args=(mean_returns, cov_matrix),
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )

    return result.x