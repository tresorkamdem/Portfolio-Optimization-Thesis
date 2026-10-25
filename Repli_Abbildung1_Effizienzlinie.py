# =====================================================================
#  Repli_Abbildung1_Effizienzlinie.py  --  Replikationsskript
#  Reproduziert: Abbildung: Effizienzlinie, GMV- und Tangentialportfolio (hypothetisches 5-Wertpapier-Beispiel).
#  Quellen: eigener Code.
# =====================================================================

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

np.random.seed(42)   # Reproduzierbarkeit der Streuwolke

mu  = np.array([0.06, 0.08, 0.10, 0.12, 0.085])   # erwartete Jahresrenditen
vol = np.array([0.12, 0.15, 0.20, 0.25, 0.14])
C = np.array([[1.00, 0.30, 0.20, 0.10, 0.35],
              [0.30, 1.00, 0.40, 0.25, 0.30],
              [0.20, 0.40, 1.00, 0.35, 0.20],
              [0.10, 0.25, 0.35, 1.00, 0.15],
              [0.35, 0.30, 0.20, 0.15, 1.00]])
Sigma = np.outer(vol, vol) * C
n = len(mu); rf = 0.02

W = np.random.dirichlet(np.ones(n), size=8000)        # Long-only-Portfolios
port_mu  = W @ mu
port_sig = np.sqrt(np.einsum("ij,jk,ik->i", W, Sigma, W))

inv = np.linalg.inv(Sigma); ones = np.ones(n)
w_gmv = inv @ ones / (ones @ inv @ ones)
mu_gmv = w_gmv @ mu; sig_gmv = np.sqrt(w_gmv @ Sigma @ w_gmv)
w_tan = inv @ (mu - rf*ones); w_tan = w_tan / (ones @ w_tan)
mu_tan = w_tan @ mu; sig_tan = np.sqrt(w_tan @ Sigma @ w_tan)

A = ones @ inv @ ones; B = ones @ inv @ mu; Cc = mu @ inv @ mu
mus = np.linspace(mu_gmv - 0.03, mu.max() + 0.03, 200)
sig_eff = np.sqrt((A*mus**2 - 2*B*mus + Cc) / (A*Cc - B**2))
ober = mus >= mu_gmv

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(port_sig, port_mu, s=4, color="0.75", alpha=0.5, label="Mögliche Portfolios")
ax.plot(sig_eff[ober], mus[ober], color="#2471A3", lw=2.5, label="Effizienzlinie")
ax.plot(sig_eff[~ober], mus[~ober], color="0.5", lw=1.8, ls="--", label="Dominierter Ast")
xs = np.linspace(0, port_sig.max()*1.05, 50)
ax.plot(xs, rf + (mu_tan - rf)/sig_tan*xs, color="#C0392B", lw=1.8, label="Kapitalmarktlinie (CML)")
ax.scatter([sig_gmv], [mu_gmv], color="#1E8449", s=90, zorder=5, edgecolor="black")
ax.annotate("GMV\n(Minimalvarianz)", (sig_gmv, mu_gmv), textcoords="offset points",
            xytext=(6, -30), color="#1E8449", fontweight="bold")
ax.scatter([sig_tan], [mu_tan], color="#E67E22", s=90, zorder=5, edgecolor="black")
ax.annotate("Tangential-\nportfolio (max. Sharpe)", (sig_tan, mu_tan),
            textcoords="offset points", xytext=(10, -4), color="#E67E22", fontweight="bold")
ax.scatter([0], [rf], color="black", s=40, zorder=5)
ax.annotate("Risikoloses Asset $r_f$", (0, rf), textcoords="offset points", xytext=(6, -14))
ax.set_xlabel("Risiko  $\\sigma_p$  (Volatilität)")
ax.set_ylabel("Erwartete Rendite  $\\mu_p$")
ax.set_title("Effizienzlinie, GMV- und Tangentialportfolio")
ax.set_xlim(left=0); ax.legend(loc="lower right"); ax.grid(alpha=0.3)
plt.tight_layout(); plt.savefig("abbildung1_effizienzlinie.png", dpi=150)
print("abbildung1_effizienzlinie.png gespeichert")
