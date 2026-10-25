# =====================================================================
#  Repli_Abbildung4_Volatilitaet.py  --  Replikationsskript
#  Reproduziert: Abbildung: annualisierte Out-of-Sample-Volatilitaet je Schaetzer und Fenster.
#  Quellen: eigener Code. Ledoit-Wolf-/OAS-Schaetzer aus scikit-learn
#    (Ledoit & Wolf 2004; Chen, Wiesel & Hero 2010).
# =====================================================================

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.covariance import LedoitWolf, OAS
from daten_vorbereiten import lade_renditen

R, datum, branchen = lade_renditen("48_Industry_Portfolios.csv")
n = R.shape[1]

def gmv_weights(Sigma):
    ones = np.ones(Sigma.shape[0])
    inv = np.linalg.inv(Sigma)
    return inv @ ones / (ones @ inv @ ones)

def backtest_vola_alle(R, fenster):
    T_total = R.shape[0]
    oos = {"Empirisch": [], "Ledoit-Wolf": [], "OAS": [], "1/N": []}
    for t in range(fenster, T_total):
        v = R[t-fenster:t, :]; r_next = R[t, :]
        oos["Empirisch"].append(gmv_weights(np.cov(v, rowvar=False, ddof=1)) @ r_next)
        oos["Ledoit-Wolf"].append(gmv_weights(LedoitWolf().fit(v).covariance_) @ r_next)
        oos["OAS"].append(gmv_weights(OAS().fit(v).covariance_) @ r_next)
        oos["1/N"].append((np.ones(n)/n) @ r_next)
    return {m: np.std(r, ddof=1)*np.sqrt(12)*100 for m, r in oos.items()}

vola60 = backtest_vola_alle(R, 60)
vola120 = backtest_vola_alle(R, 120)

methoden = list(vola60.keys())
x = np.arange(len(methoden)); breite = 0.35
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.bar(x - breite/2, [vola60[m] for m in methoden], breite, label="Fenster 60 Monate", color="#C0392B")
ax.bar(x + breite/2, [vola120[m] for m in methoden], breite, label="Fenster 120 Monate", color="#2471A3")
ax.set_ylabel("Out-of-Sample-Volatilität p.a. (%)")
ax.set_title("Volatilität je Schätzer und Fensterlänge (48 Branchen)")
ax.set_xticks(x); ax.set_xticklabels(methoden)
ax.legend(); ax.grid(axis="y", alpha=0.3)
plt.tight_layout(); plt.savefig("abbildung4_volatilitaet.png", dpi=150)
print("abbildung4_volatilitaet.png gespeichert")
