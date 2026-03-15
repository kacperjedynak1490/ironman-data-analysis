import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

if not os.path.exists('Wykresy'):
    os.makedirs('Wykresy')

#ustawienia wizualizacji
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12,6)
sns.set_context("paper", font_scale=1.2)

#----------------------------------------------------
#wczytanie danych z pliku csv
data = pd.read_csv('2019 Ironman World Championship Results.csv')

#----------------------------------------------------
#analiza typow danych
#print(data.dtypes) #wszystko string, konwersja

#----------------------------------------------------
#sprawdzenie nulli
#print(data.isnull().sum()) 

#----------------------------------------------------
#czyszczenie danych - usuniecie wierszy z brakujacymi danymi
data = data.dropna()

#----------------------------------------------------
#konwersja do odpowiednich typow 
to_conversion = ['Swim', 'Bike', 'Run', 'Overall', 'T1', 'T2']
data[to_conversion] = data[to_conversion].apply(lambda x: pd.to_timedelta(x))

#print(data.dtypes) #sprawdzenie po konwersji

#----------------------------------------------------
#konwersja czasu do sekund 
data[to_conversion] = data[to_conversion].apply(lambda x: x.dt.total_seconds())

#print(data.head()) #sprawdzenie danych

#----------------------------------------------------
#analiza statystyczna
print(data.describe()) #podstawowe statystyki

#----------------------------------------------------
#analiza korelacji - czas danej dyscypliny a overall
correlation_swim = data['Swim'].corr(data['Overall'])
correlation_bike = data['Bike'].corr(data['Overall'])
correlation_run = data['Run'].corr(data['Overall'])

print(f"Korelacja ze swim: {correlation_swim}")
print(f"Korelacja ze bike: {correlation_bike}")
print(f"Korelacja ze run: {correlation_run}")

#korelogram - wizualizacja korelacji
sns.heatmap(data[['Swim', 'Bike', 'Run', 'Overall']].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.savefig('Wykresy/correlation_heatmap.png')
plt.close()
#wedlug wynikow korelacji, czas biegu ma najsilniejszy wplyw na czas calkowity, a nastepnie rower

#----------------------------------------------------
#analiza rozkladu czasow wedlug dyscyplin
sns.histplot(data['Swim'],kde=True)
plt.xlabel('Czas plywania (sekundy)')
plt.ylabel('Liczba zawodników')
plt.title('Rozklad czasow plywania')
plt.savefig('Wykresy/swim_distribution.png')
plt.close()
#pokazuje ze dane plywania maja rozklad zblizony do normalnego, z wieksza liczba zawodnikow konczacych w okolicach 1h, ale zdarzaja sie tez zawodnicy koncacy w 2h, co wskazuje na duza rozpietosc wynikow w tej dyscyplinie

sns.histplot(data['Bike'],kde=True)
plt.xlabel('Czas roweru (sekundy)')
plt.ylabel('Liczba zawodników')
plt.title('Rozklad czasow roweru')
plt.savefig('Wykresy/bike_distribution.png') 
plt.close()
#rozklad podobny do plywania, skosny w prawo

sns.histplot(data['Run'],kde=True)
plt.xlabel('Czas biegu (sekundy)')
plt.ylabel('Liczba zawodników')
plt.title('Rozklad czasow biegu')
plt.savefig('Wykresy/run_distribution.png') 
plt.close()
#rozklad bardziej skosny w prawo z anomalia w okolicach 22500 sekund, prawdopodobne dla amatorow

#----------------------------------------------------
#wykres punktowy z krzywa regresji dla overall i swim
sns.regplot(x='Swim', y='Overall', data=data, scatter_kws={"alpha": 0.3,"color": "blue"}, line_kws={"color": "red"})
plt.xlabel('Czas plywania (sekundy)')
plt.ylabel('Calkowity czas (sekundy)')
plt.title('Regresja: czas plywania vs czas calkowity')
plt.savefig('Wykresy/swim_overall_regression.png')
plt.close()
#Regresja liniowa potwierdza dodatnią zależność czasu pływania od wyniku końcowego, jednak niski współczynnik nachylenia sugeruje, że przewaga uzyskana w wodzie jest najmniej znaczącą składową sukcesu w całym wyścigu.

#---------------------------------------------------
#analiza demograficzna - plec a czas calkowity
sns.boxplot(x='Gender',y='Overall', data=data)
plt.xlabel('Płeć')
plt.ylabel('Calkowity czas (sekundy)')
plt.title('Rozklad czasu calkowitego wedlug plci')
plt.savefig('Wykresy/gender_overall_boxplot.png')
plt.close()
#Mediana czasu mężczyzn jest niższa (są statystycznie szybsi), jednak rozkład ich wyników 
#jest znacznie szerszy, z dużą liczbą tzw. outlierów (zawodników kończących blisko limitu czasu). 
#Grupa kobiet jest bardziej jednorodna i wyrównana pod względem czasu ukończenia zawodów.

#---------------------------------------------------
#analiza trendow geograficznych - 10 najliczniej reprezentowanych krajow z podzialem na plec
top_countries = data['Country'].value_counts().head(10)
#print(top_countries)
data_top_10 = data[data['Country'].isin(top_countries.index)]
sns.countplot(data=data_top_10, x='Country', palette='viridis', hue='Gender')
plt.xlabel('Kraj')
plt.ylabel('Liczba zawodników')
plt.title('Liczba zawodników wg kraju i płci (top 10)')
plt.savefig('Wykresy/country_gender_countplot.png')
plt.close()
#dominacja USA, Niemiec i Australii, zgodne z popularnoscia triathlonu

#---------------------------------------------------
#czy zmiany maja wplyw na overall?
data['Change'] = data['T1'] + data['T2']
correlation_change = data['Change'].corr(data['Overall'])

print(f"Korelacja ze zmianami: {correlation_change}")
#zmiany maja slaby wplyw na czas calkowity, co wskazuje, ze najwazniejsze sa same dyscypliny

#---------------------------------------------------
#top 5 zawodnikow z najlepszym czasem calkowitym w minutach
top_5 = data.nsmallest(5, 'Overall')
top_5_readable = top_5.copy()
top_5_readable['Overall'] = pd.to_timedelta(top_5_readable['Overall'], unit='s')
print(top_5_readable[['Name', 'Country', 'Overall']])

#---------------------------------------------------
#przenoszenie danych do nowego pliku csv
data.to_csv('cleaned_ironman_results.csv')