# =====================================================================
#  Repli_Abbildung2_Rolling.py  --  Replikationsskript
#  Reproduziert: Abbildung: schematische Darstellung des Rolling-Window-Verfahrens.
#  Quellen: eigener Code.
# =====================================================================

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(9, 4.5))
fenster = 4; n_schritte = 5
for i in range(n_schritte):
    start = i
    ax.add_patch(patches.Rectangle((start, n_schritte - i), fenster, 0.7,
                 facecolor="#2471A3", edgecolor="black"))
    ax.add_patch(patches.Rectangle((start + fenster, n_schritte - i), 1, 0.7,
                 facecolor="#C0392B", edgecolor="black"))
ax.add_patch(patches.Rectangle((0, -1.3), 0.7, 0.5, facecolor="#2471A3", edgecolor="black"))
ax.text(0.9, -1.15, "Schätzfenster (Vergangenheit): Σ schätzen → GMV-Gewichte", fontsize=9)
ax.add_patch(patches.Rectangle((0, -2.1), 0.7, 0.5, facecolor="#C0392B", edgecolor="black"))
ax.text(0.9, -1.95, "Test-Monat (ungesehen): Out-of-Sample-Rendite messen", fontsize=9)
ax.set_xlim(-0.5, 11); ax.set_ylim(-2.5, n_schritte + 1.2)
ax.set_xlabel("Zeit (Monate) →")
ax.set_title("Das Rolling-Window-Verfahren: Fenster verschiebt sich Monat für Monat")
ax.set_yticks([])
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig("abbildung2_rolling.png", dpi=150)
print("abbildung2_rolling.png gespeichert")
