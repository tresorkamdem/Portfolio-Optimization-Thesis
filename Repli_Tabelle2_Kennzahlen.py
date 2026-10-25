# =====================================================================
#  Repli_Tabelle2_Kennzahlen.py  --  Replikationsskript
#  Reproduziert: Out-of-Sample-Kennzahlen (Vola, Sharpe, Turnover, Kappa) fuer Fenster 60 und 120.
#  Quellen: eigener Code. Ledoit-Wolf-/OAS-Schaetzer aus scikit-learn
#    (Ledoit & Wolf 2004; Chen, Wiesel & Hero 2010).
# =====================================================================

import numpy as np
from sklearn.covariance import LedoitWolf, OAS
from daten_vorbereiten import lade_renditen

R, datum, branchen = lade_renditen("48_Industry_Portfolios.csv")
n = R.shape[1]

def gmv_weights(Sigma):
    ones = np.ones(Sigma.shape[0])
    inv = np.linalg.inv(Sigma)
    return inv @ ones / (ones @ inv @ ones)

def backtest_voll(R, fenster):
    T_total = R.shape[0]
    oos = {"Empirisch": [], "Ledoit-Wolf": [], "OAS": [], "1/N": []}
    gew = {"Empirisch": [], "Ledoit-Wolf": [], "OAS": [], "1/N": []}
    kappa = {"Empirisch": [], "Ledoit-Wolf": [], "OAS": []}

    for t in range(fenster, T_total):
        vergangen = R[t-fenster:t, :]
        r_next = R[t, :]

        S = np.cov(vergangen, rowvar=False, ddof=1)
        w = gmv_weights(S)
        oos["Empirisch"].append(w @ r_next); gew["Empirisch"].append(w)
        kappa["Empirisch"].append(np.linalg.cond(S))

        S = LedoitWolf().fit(vergangen).covariance_
        w = gmv_weights(S)
        oos["Ledoit-Wolf"].append(w @ r_next); gew["Ledoit-Wolf"].append(w)
        kappa["Ledoit-Wolf"].append(np.linalg.cond(S))

        S = OAS().fit(vergangen).covariance_
        w = gmv_weights(S)
        oos["OAS"].append(w @ r_next); gew["OAS"].append(w)
        kappa["OAS"].append(np.linalg.cond(S))

        w = np.ones(n) / n
        oos["1/N"].append(w @ r_next); gew["1/N"].append(w)

    return oos, gew, kappa

def turnover(gewichte):
    """Mittlerer monatlicher Umschlag der Gewichte."""
    diffs = [0.5 * np.abs(gewichte[i] - gewichte[i-1]).sum()
             for i in range(1, len(gewichte))]
    return np.mean(diffs)

def auswerten(oos, gew, kappa, fenster):
    print(f"\n=== Fenster = {fenster} Monate (n/T = {n/fenster:.2f}) ===")
    print(f"{'Methode':<14}{'Vola':>9}{'Sharpe':>9}{'Turnover':>11}{'kappa':>10}")
    print("-" * 53)
    for m in oos:
        r = np.array(oos[m])
        vola = np.std(r, ddof=1) * np.sqrt(12)
        sharpe = (np.mean(r) * 12) / vola
        to = turnover(gew[m])
        k = np.mean(kappa[m]) if m in kappa else float("nan")
        k_txt = f"{k:>10.0f}" if m in kappa else f"{'-':>10}"
        print(f"{m:<14}{vola*100:>8.2f}%{sharpe:>9.3f}{to:>11.3f}{k_txt}")

for fenster in [60, 120]:
    oos, gew, kappa = backtest_voll(R, fenster)
    auswerten(oos, gew, kappa, fenster)
