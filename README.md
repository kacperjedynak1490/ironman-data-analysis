# 🏊‍♂️🚴‍♂️🏃‍♂️ Ironman World Championship 2019 - Data Analysis

Projekt analizuje wyniki Mistrzostw Świata Ironman 2019 w Kailua-Kona na Hawajach. Celem było zidentyfikowanie kluczowych czynników wpływających na sukces w triathlonie oraz analiza demograficzna uczestników.

## 🛠 Technologie
* **Python 3.x**
* **Pandas**: Czyszczenie i transformacja danych (ETL).
* **Seaborn & Matplotlib**: Wizualizacja statystyczna.

## 📈 Kluczowe wnioski (Insights)
1. **Dominacja Biegu i Roweru**: Czas maratonu (Run) oraz roweru (Bike) wykazują niemal identyczną, najwyższą korelację z wynikiem końcowym (r = 0.94). To na lądzie decydują się losy wyścigu.
2. **Wydajność a Płeć**: Mężczyźni mają statystycznie lepszą (niższą) medianę czasu, jednak ich wyniki mają ogromny rozrzut i najwięcej skrajnie słabych czasów. Grupa kobiet jest znacznie bardziej wyrównana.
3. **Geografia**: USA, Niemcy i Australia stanowią większość uczestników z top 10 krajów, co odzwierciedla popularność dyscypliny w tych regionach. W każdym z nich dominuje udział mężczyzn.
4. **Efektywność zmian (T1/T2)**: Korelacja stref zmian z wynikiem końcowym jest niższa, co wskazuje, że dla większości zawodników czas spędzony w namiotach zmianowych nie jest w pełni decydujący dla wyniku.

## 🚀 Jak uruchomić?
Aby uniknąć konfliktów z innymi bibliotekami na Twoim komputerze, zalecam użycie wirtualnego środowiska.

1. Utwórz i aktywuj środowisko:
   * **Windows:** `python -m venv venv` a następnie `venv\Scripts\activate`
   * **macOS/Linux:** `python3 -m venv venv` a następnie `source venv/bin/activate`
2. Zainstaluj wymagania: `pip install -r requirements.txt`
3. Uruchom skrypt: `python analiza.py`
4. Wyniki zostaną wygenerowane automatycznie: wykresy zapiszą się w nowym folderze `Wykresy/`, a oczyszczone dane w pliku `cleaned_ironman_results.csv`.

## Lub...
## 🚀 Link do aplikacji
