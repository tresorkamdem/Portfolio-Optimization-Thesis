# =====================================================================
#  Repli_Abbildung5_Dimension.py  --  Replikationsskript
#  Reproduziert: Abbildung: Volatilitaetsreduktion durch Shrinkage in Abhaengigkeit von n.
#  Quellen: eigener Code. Ledoit-Wolf-/OAS-Schaetzer aus scikit-learn
#    (Ledoit & Wolf 2004; Chen, Wiesel & Hero 2010).
# =====================================================================

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.covariance import LedoitWolf
from daten_vorbereiten import lade_renditen

def gmv_weights(Sigma):
    ones = np.ones(Sigma.shape[0])
    inv = np.linalg.inv(Sigma)
    return inv @ ones / (ones @ inv @ ones)

dateien = {10: "10_Industry_Portfolios.csv",
           30: "30_Industry_Portfolios.csv",
           48: "48_Industry_Portfolios.csv"}
fenster = 120
ns, reduktionen = [], []
for n_i, datei in dateien.items():
    Ri, _, _ = lade_renditen(datei)
    T_total = Ri.shape[0]
    oe, ol = [], []
    for t in range(fenster, T_total):
        v = Ri[t-fenster:t, :]; r_next = Ri[t, :]
        oe.append(gmv_weights(np.cov(v, rowvar=False, ddof=1)) @ r_next)
        ol.append(gmv_weights(LedoitWolf().fit(v).covariance_) @ r_next)
    ve = np.std(oe, ddof=1)*np.sqrt(12); vl = np.std(ol, ddof=1)*np.sqrt(12)
    ns.append(n_i); reduktionen.append((ve-vl)/ve*100)

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.plot(ns, reduktionen, "o-", color="#1E8449", linewidth=2, markersize=9)
ax.set_xlabel("Anzahl Branchen n"); ax.set_ylabel("Vola-Reduktion durch Shrinkage (%)")
ax.set_title("Der Shrinkage-Vorteil wächst mit der Dimension (Fenster 120)")
ax.grid(alpha=0.3)
for xi, yi in zip(ns, reduktionen):
    ax.annotate(f"{yi:.1f}%", (xi, yi), textcoords="offset points", xytext=(0, 10))
plt.tight_layout(); plt.savefig("abbildung5_dimension.png", dpi=150)
print("abbildung5_dimension.png gespeichert")
