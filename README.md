# Portfoliooptimierung mit Machine Learning  

---

## Überblick

Dieses Projekt untersucht die Portfoliooptimierung unter Verwendung klassischer finanzwirtschaftlicher Modelle sowie moderner datengetriebener Methoden.

Im Fokus steht der Vergleich eines praxisbasierten Portfolios mit mathematisch optimierten Portfolios.

---

## Zielsetzung

Ziel dieser Arbeit ist es zu analysieren, ob Machine-Learning-Methoden die klassische Portfoliooptimierung nach Markowitz verbessern können.

Dabei wird insbesondere untersucht, ob sich durch datenbasierte Ansätze bessere Rendite-Risiko-Verhältnisse erzielen lassen.

---

## Methodik

Das Projekt folgt einem strukturierten quantitativen Ansatz:

1. Datenerhebung über Finanz-APIs (Yahoo Finance)  
2. Berechnung von Renditen auf Basis historischer Daten  
3. Schätzung der erwarteten Renditen und der Kovarianzmatrix  
4. Portfoliooptimierung nach der Markowitz-Theorie  
5. Modellierung der Volatilität mit GARCH  
6. Erweiterung durch Machine-Learning-Modelle  
7. Bewertung der Ergebnisse anhand von Risikokennzahlen  

---

## Datenbasis

Da direkte Marktdaten aus der CEMAC-Region nur eingeschränkt verfügbar sind, werden börsengehandelte Fonds (ETFs) als Approximation verschiedener Anlageklassen verwendet:

- SPY → Aktienmarkt  
- QQQ → Technologieaktien  
- TLT → Staatsanleihen  
- GLD → Gold  
- VNQ → Immobilien  

Die Daten stammen aus Yahoo Finance und ermöglichen eine empirische Analyse von Renditen und Risiken.

---

## Projektstruktur

Portfolio-Optimization-Thesis/
│
├── notebooks/        # Analysen und Visualisierungen  
├── src/              # Kernlogik (Modelle & Funktionen)  
│   ├── data/  
│   ├── models/  
│   ├── utils/  
│
├── scripts/          # Ausführbare Programme  
│   ├── run_markowitz.py  
│   ├── run_ml.py  
│   ├── run_garch.py  
│   └── run_all_models.py  
│
├── results/          # Ergebnisse (Tabellen & Grafiken)  
├── README.md  
├── requirements.txt  

---

## Implementierung

### Markowitz-Modell
- Minimierung der Portfolio-Varianz  
- Nebenbedingungen: Summe der Gewichte = 1, keine Leerverkäufe  

### Machine Learning
- Prognose von Renditen auf Basis historischer Daten  
- Erweiterung der klassischen Portfolio-Theorie  

### GARCH-Modell
- Modellierung zeitvariierender Volatilität  
- Berücksichtigung von Volatilitäts-Clustern in Finanzmärkten  

---

## Ausführung

Alle Modelle ausführen:

python -m scripts.run_all_models

Einzelne Modelle:

python -m scripts.run_markowitz  
python -m scripts.run_ml  
python -m scripts.run_garch  

---

## Ergebnisse (vorläufig)

Erste Ergebnisse zeigen:

- Das praxisbasierte Portfolio ist intuitiv, jedoch nicht effizient  
- Das Markowitz-Portfolio bietet ein besseres Rendite-Risiko-Verhältnis  
- Machine Learning und GARCH liefern zusätzliche Einblicke in Prognose und Risikomodellierung  

Diese Ergebnisse sind als vorläufig zu verstehen und werden im weiteren Verlauf der Arbeit vertieft.

---

## Bewertung

Die Portfolios werden anhand folgender Kennzahlen bewertet:

- Erwartete Rendite  
- Volatilität (Standardabweichung)  
- Sharpe Ratio  

Diese ermöglichen einen konsistenten Vergleich der verschiedenen Ansätze.

---

## Aktueller Stand der Arbeit

Dieses Projekt ist Teil einer laufenden Bachelorarbeit und befindet sich noch in Bearbeitung.

Aktuelle Schwerpunkte sind:

- Verbesserung der Renditeprognosen durch Machine Learning  
- Erweiterung der GARCH-Modelle  
- Durchführung von Out-of-Sample-Analysen  
- Validierung der Ergebnisse  

---

## Installation

Abhängigkeiten installieren:

pip install -r requirements.txt  

---

## Autor

Jean Jacques Kamdem  
Matrikelnummer: 548153  
Bachelor Wirtschaftsmathematik  

---

## Literatur

- Markowitz, H. (1952). Portfolio Selection  
- Sharpe, W. (1964). Capital Asset Pricing Model  
- Hull, J. (2018). Options, Futures and Other Derivatives