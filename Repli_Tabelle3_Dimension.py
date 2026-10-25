# =====================================================================
#  Repli_Tabelle3_Dimension.py  --  Replikationsskript
#  Reproduziert: Tabelle Volatilitaetsreduktion nach Dimension (n = 10, 30, 48).
#  Quellen: eigener Code. Ledoit-Wolf-/OAS-Schaetzer aus scikit-learn
#    (Ledoit & Wolf 2004; Chen, Wiesel & Hero 2010).
# =====================================================================

import numpy as np
from sklearn.covariance import LedoitWolf
from daten_vorbereiten import lade_renditen

# ---------------------------------------------------------------------
# Werkzeuge (wie im Backtest)
# ---------------------------------------------------------------------
def gmv_weights(Sigma):
    ones = np.ones(Sigma.shape[0])
    inv = np.linalg.inv(Sigma)
    return inv @ ones / (ones @ inv @ ones)

def backtest_vola(R, fenster):
    """Gibt die annualisierte OOS-Volatilitaet fuer empirisch und LW zurueck."""
    T_total, n = R.shape
    oos_emp, oos_lw = [], []
    for t in range(fenster, T_total):
        vergangen = R[t-fenster:t, :]
        r_next = R[t, :]
        # Empirisch
        w = gmv_weights(np.cov(vergangen, rowvar=False, ddof=1))
        oos_emp.append(w @ r_next)
        # Ledoit-Wolf
        w = gmv_weights(LedoitWolf().fit(vergangen).covariance_)
        oos_lw.append(w @ r_next)
    vola_emp = np.std(oos_emp, ddof=1) * np.sqrt(12)
    vola_lw = np.std(oos_lw, ddof=1) * np.sqrt(12)
    return vola_emp, vola_lw

# ---------------------------------------------------------------------
# Die drei Datensaetze durchlaufen
# ---------------------------------------------------------------------
dateien = {
    10: "10_Industry_Portfolios.csv",
    30: "30_Industry_Portfolios.csv",
    48: "48_Industry_Portfolios.csv",
}

fenster = 120   # feste Fensterlaenge fuer alle -> fairer Vergleich

print(f"Fenster = {fenster} Monate\n")
print(f"{'n':>4}{'n/T':>8}{'Vola emp.':>12}{'Vola LW':>10}{'Reduktion':>12}")
print("-" * 46)

for n, datei in dateien.items():
    R, datum, branchen = lade_renditen(datei)
    v_emp, v_lw = backtest_vola(R, fenster)
    reduktion = (v_emp - v_lw) / v_emp * 100
    print(f"{n:>4}{n/fenster:>8.2f}{v_emp*100:>11.2f}%{v_lw*100:>9.2f}%{reduktion:>10.1f}%")
