# Portfolio Optimization with Machine Learning  
# Portfoliooptimierung mit Machine Learning  

---

## Overview | Überblick

This project investigates portfolio optimization using classical financial theory and modern data-driven methods.

Das Ziel dieses Projekts ist die Untersuchung der Portfoliooptimierung unter Verwendung klassischer finanzwirtschaftlicher Methoden sowie moderner datengetriebener Ansätze.

The main objective is to analyze whether Machine Learning techniques can improve the estimation of expected returns compared to the classical Markowitz approach.

Im Fokus steht die Frage, ob Machine-Learning-Methoden die klassische Portfoliooptimierung verbessern können.

---

## Motivation | Motivation

In finance, investors aim to maximize returns while controlling risk.

In der Finanzökonomie versuchen Investoren, ihre Rendite zu maximieren und gleichzeitig das Risiko zu kontrollieren.

This trade-off can be formulated as an optimization problem between return and risk.

Dieses Problem kann als Optimierungsproblem zwischen Rendite und Risiko formuliert werden.

The classical solution is given by Markowitz, showing that diversification reduces risk.

Die klassische Lösung liefert die Markowitz-Theorie, die zeigt, dass Diversifikation das Risiko reduziert.

---

## Research Question | Forschungsfrage

Can Machine Learning improve classical portfolio optimization?

Kann Machine Learning die klassische Portfoliooptimierung nach Markowitz verbessern?

---

## Methodology | Methodik

This project follows a structured research approach:

1. Data collection using financial APIs (yfinance)  
2. Data preprocessing and return computation  
3. Portfolio optimization using Markowitz theory  
4. Simulation of the efficient frontier  
5. Extension using Machine Learning models  
6. Volatility modeling using GARCH  

Das Projekt folgt einem strukturierten wissenschaftlichen Ansatz:

1. Datenerhebung über Finanz-APIs (yfinance)  
2. Datenaufbereitung und Berechnung von Renditen  
3. Portfoliooptimierung nach Markowitz  
4. Simulation der effizienten Grenze  
5. Erweiterung durch Machine Learning  
6. Modellierung der Volatilität mit GARCH  

---

## Project Structure | Projektstruktur

- `notebooks/01_data_preparation.ipynb`  
  Data loading and preprocessing / Datenaufbereitung  

- `notebooks/02_markowitz_simulation.ipynb`  
  Simulation of the efficient frontier / Simulation der effizienten Grenze  

- `notebooks/03_markowitz_real_data.ipynb`  
  Portfolio optimization with real data / Optimierung mit realen Daten  

- `notebooks/04_machine_learning_extension.ipynb`  
  Machine Learning extension *(Work in progress)*  
  Machine Learning Erweiterung *(in Bearbeitung)*  

- `notebooks/05_volatility_model_garch.ipynb`  
  GARCH volatility modeling *(Work in progress)*  
  GARCH Volatilitätsmodell *(in Bearbeitung)*  

---

## Current Status | Aktueller Stand

This project is part of an ongoing Bachelor thesis.

Dieses Projekt ist Teil einer laufenden Bachelorarbeit.

Work in progress.

In Bearbeitung.

---

## Next Steps | Nächste Schritte

- Improve return prediction using Machine Learning  
- Implement GARCH models for volatility estimation  
- Compare all approaches using the Sharpe Ratio  
- Evaluate robustness and out-of-sample performance  

- Verbesserung der Renditeprognose durch Machine Learning  
- Implementierung von GARCH-Modellen zur Volatilitätsschätzung  
- Vergleich aller Ansätze anhand der Sharpe Ratio  
- Analyse der Robustheit und Out-of-Sample-Performance  

---

## Installation | Installation

Install dependencies using:

pip install -r requirements.txt

---

## Repository

GitHub Repository:  
https://github.com/tresorkamdem/Portfolio-Optimization-Thesis

---

## Author

Jean Jacques Kamdem  
Matrikelnummer: 548153  
Bachelorstudent Wirtschaftsmathematik  

---

## References (initial) | Literatur (Auswahl)

- Markowitz, H. (1952). Portfolio Selection  
- Sharpe, W. (1964). Capital Asset Pricing Model  
- Hull, J. – Options, Futures and Other Derivatives  