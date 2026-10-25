# =====================================================================
#  Repli_Abbildung3_Problem.py  --  Replikationsskript
#  Reproduziert: Abbildung: Konditionszahl kappa der empirischen Kovarianzmatrix vs. n/T.
#  Quellen: eigener Code.
# =====================================================================

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from daten_vorbereiten import lade_renditen

R, datum, branchen = lade_renditen("48_Industry_Portfolios.csv")
n = R.shape[1]

Ts = [50, 60, 70, 80, 100, 120, 160, 200, 300, 500, 683]
ratios, kappas = [], []
for T in Ts:
    fenster = R[-T:, :]
    S = np.cov(fenster, rowvar=False, ddof=1)
    ratios.append(n / T); kappas.append(np.linalg.cond(S))

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(ratios, kappas, "o-", color="#C0392B", linewidth=2, markersize=7)
ax.axvline(1.0, color="gray", ls="--", alpha=0.7)
ax.text(1.02, max(kappas)*0.3, "n/T = 1\n(Matrix singulär)", color="gray", fontsize=9)
ax.set_yscale("log")
ax.set_xlabel("Verhältnis n/T (Wertpapiere pro Beobachtung)")
ax.set_ylabel("Konditionszahl κ (log-Skala)")
ax.set_title("Das Schätzproblem: κ explodiert, wenn n/T → 1")
ax.grid(alpha=0.3)
plt.tight_layout(); plt.savefig("abbildung3_problem.png", dpi=150)
print("abbildung3_problem.png gespeichert")
