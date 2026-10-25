# =====================================================================
#  daten_vorbereiten.py
#  Laedt eine Kenneth-French-CSV, bereinigt sie (Fehlcodes, erster
#  Block, Zeitraum ab 1969) und gibt die Renditematrix R zurueck.
#  Basis fuer alle anderen Skripte via: from daten_vorbereiten import ...
#  Hilfsskript (kein Replikationsskript).
#  Quellen: eigener Code.
# =====================================================================
import pandas as pd
import numpy as np

def lade_renditen(dateiname):
    """Laedt eine French-Industry-CSV und gibt (R, datum, branchen) zurueck."""

    # Schritt 1: laden, Kopfzeilen ueberspringen
    df = pd.read_csv(dateiname, skiprows=11)
    df = df.rename(columns={df.columns[0]: "Datum"})

    # Schritt 2: nur gueltige Monatsdaten (JJJJMM)
    datum_text = df["Datum"].astype(str).str.strip()
    maske = datum_text.str.match(r"^\d{6}$")
    df_m = df[maske].copy()
    df_m["Datum"] = df_m["Datum"].astype(int)

    # Schritt 3: nur der erste Block
    sprung = np.where(np.diff(df_m["Datum"].values) < 0)[0]
    if len(sprung) > 0:
        df_m = df_m.iloc[:sprung[0] + 1].copy()

    # Schritt 4: Fehlcodes -> NaN
    branchen = [c for c in df_m.columns if c != "Datum"]
    for spalte in branchen:
        df_m[spalte] = pd.to_numeric(df_m[spalte], errors="coerce")
    df_m[branchen] = df_m[branchen].replace([-99.99, -999.0], np.nan)

    # Schritt 5: Zeitraum mit allen Branchen verfuegbar
    vollstaendig = df_m[branchen].notna().all(axis=1)
    erste_gute = df_m.loc[vollstaendig, "Datum"].iloc[0]
    df_final = df_m[df_m["Datum"] >= erste_gute].copy()
    assert df_final[branchen].isna().sum().sum() == 0, "Es gibt noch NaN!"

    # Schritt 6: Renditematrix R (Prozent -> Dezimal)
    R = df_final[branchen].values / 100.0
    datum = df_final["Datum"].values
    return R, datum, branchen


# Test: laeuft das Skript direkt, zeigen wir eine Kurzinfo
if __name__ == "__main__":
    R, datum, branchen = lade_renditen("48_Industry_Portfolios.csv")
    print("R =", R.shape, "von", datum[0], "bis", datum[-1])