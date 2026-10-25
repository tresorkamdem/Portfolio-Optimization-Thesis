# =====================================================================
#  Repli_Tabelle1_Schaetzproblem.py  --  Replikationsskript
#  Reproduziert: Tabelle zum Schaetzproblem (Konditionszahl und Invertierbarkeit je T).
#  Quellen: eigener Code. Ledoit-Wolf-/OAS-Schaetzer aus scikit-learn
#    (Ledoit & Wolf 2004; Chen, Wiesel & Hero 2010).
# =====================================================================

import numpy as np
from daten_vorbereiten import lade_renditen

# Wir nehmen die 48 Branchen und schneiden das Datenfenster kuenstlich kurz,
# um den Fall "viele Wertpapiere, wenig Daten" zu erzeugen.
R, datum, branchen = lade_renditen("48_Industry_Portfolios.csv")
n = R.shape[1]
print(f"Anzahl Wertpapiere n = {n}\n")

print(f"{'T (Monate)':>12}{'n/T':>8}{'Konditionszahl':>18}{'invertierbar?':>16}")
print("-" * 54)

for T in [24, 36, 48, 60, 120, 240, 683]:
    fenster = R[-T:, :]                        # die letzten T Monate
    S = np.cov(fenster, rowvar=False, ddof=1)  # empirische Kovarianzmatrix
    kappa = np.linalg.cond(S)

    # Ist die Matrix praktisch invertierbar? (Rang voll?)
    rang = np.linalg.matrix_rank(S)
    invertierbar = "ja" if rang == n else f"NEIN (Rang {rang})"

    # Bei singulaerer Matrix ist kappa astronomisch -> lesbar anzeigen
    kappa_txt = f"{kappa:.2e}" if kappa > 1e6 else f"{kappa:.1f}"
    print(f"{T:>12}{n/T:>8.2f}{kappa_txt:>18}{invertierbar:>16}")

print()
print("Deutung:")
print("- T=24 (2 Jahre): n/T = 2.0 -> die Matrix ist SINGULAER,")
print("  gar nicht invertierbar. Das GMV-Portfolio existiert nicht.")
print("- Je mehr Daten, desto besser die Konditionszahl.")
