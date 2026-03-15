# 🏊‍♂️🚴‍♂️🏃‍♂️ Ironman World Championship 2019 - Data Analysis

Projekt analizuje wyniki Mistrzostw Świata Ironman 2019 w Kailua-Kona na Hawajach. Celem było zidentyfikowanie kluczowych czynników wpływających na sukces w triathlonie oraz analiza demograficzna uczestników.

## 🚀 Link do aplikacji
https://ironman-data-analysis.streamlit.app

<p align="center">
  <img src="dashboard.png" width="800">
</p>

## 🛠 Technologie
* **Python 3.x**
* **Pandas**: Czyszczenie i transformacja danych (ETL).
* **Plotly & Streamlit**: Budowa interaktywnego dashboardu i wizualizacji webowych.
* **Seaborn & Matplotlib**: Wizualizacja statystyczna.

## 📈 Kluczowe wnioski (Insights)
1. **Dominacja Biegu i Roweru**: Czas maratonu (Run) oraz roweru (Bike) wykazują niemal identyczną, najwyższą korelację z wynikiem końcowym (r = 0.94). To na lądzie decydują się losy wyścigu, co potwierdza tezę, iż triathlonu nie wygrywa się w wodzie, ale można go tam przegrać (ze względu na mniejszą korelację pływania z wynikiem końcowym).
2. **Wydajność a Płeć**: Mężczyźni mają statystycznie lepszą (niższą) medianę czasu, jednak ich wyniki mają ogromny rozrzut i najwięcej skrajnie słabych czasów. Grupa kobiet jest znacznie bardziej wyrównana.
3. **Geografia**: USA, Niemcy i Australia stanowią większość uczestników z top 10 krajów, co odzwierciedla popularność dyscypliny w tych regionach. W każdym z nich dominuje udział mężczyzn.
4. **Efektywność zmian (T1/T2)**: Korelacja stref zmian z wynikiem końcowym jest niższa, co wskazuje, że dla większości zawodników czas spędzony w namiotach zmianowych nie jest w pełni decydujący dla wyniku.

## 🚀 Jak uruchomić?
Aby uniknąć konfliktów z innymi bibliotekami na Twoim komputerze, zalecam użycie wirtualnego środowiska.

1. Sklonuj repozytorium.
2. Utwórz i aktywuj środowisko:
   * **Windows:** `python -m venv venv` a następnie `venv\Scripts\activate`
   * **macOS/Linux:** `python3 -m venv venv` a następnie `source venv/bin/activate`
3. Zainstaluj wymagania: `pip install -r requirements.txt`
4. Uruchom dashboard: `streamlit run app.py`