import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

#wczytywanie danych
data = pd.read_csv('cleaned_ironman_results.csv')

#srednie - dane do imputacji
mean_swim = data['Swim'].mean() 
mean_bike = data['Bike'].mean()
mean_run = data['Run'].mean()

# print(mean_swim, mean_bike, mean_run)

#przygotowanie danych do modelu 
X = data[['Swim', 'Bike', 'Run']] #dane do predykcji
Y = data['Overall'] #dane predykowane

model = LinearRegression() #metoda regresji liniowej do predykcji
model.fit(X, Y) #trenowanie modelu

#zapis modelu do pliku
pickle.dump(model, open('ironman_model.pkl', 'wb')) #wb - write binary

