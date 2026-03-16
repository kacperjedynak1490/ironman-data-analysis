import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pickle
st.set_page_config(layout="wide")

data = pd.read_csv("cleaned_ironman_results.csv")
AVG_SWIM = data['Swim'].mean()
AVG_BIKE = data['Bike'].mean()
AVG_RUN = data['Run'].mean()

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    return f"{hours}h {minutes}min"

st.title("Analiza wyników Ironman World Championship 2019", text_alignment="center")
columns_to_show = ['Name', 'Country', 'Swim', 'Bike', 'Run', 'Overall', 'Overall Rank']
tab1, tab2, tab3, tab4 = st.tabs(["Tabela wyników", "Wykresy", "Statystyki", "Predykcja czasu"])

with tab1:
    #st.dataframe(data.head()) #pierwsze 5 wierszy na stronie

    #st.sidebar.header("Statystyki opisowe")
    #st.sidebar.write(data.describe()) #statystyki w sidebarze

    #sidebar tworzenie do kreowania tabeli oraz wykresow na podstawie wybranych parametrow

    #podzial dashboardu na okno tabeli i okno wykresow - sidebar do wyboru, gorne okno tabela przefiltrowana ze wszystkim, dolne okno wykresy, zmienne od sidebaru
    st.sidebar.header("Filtruj dane", text_alignment="center")

    df = data.copy()

    #wybor plci
    gender_selection = ["Wszystkie"] + list(data['Gender'].unique())
    selected_gender = st.sidebar.selectbox("Płeć", gender_selection)
    if selected_gender != "Wszystkie":
        df = df[df["Gender"] == selected_gender]
    #st.dataframe(data_filtered_gender[columns_to_show])

    #wybor kraju
    country_selection = ["Wszystkie"] + list(data['Country'].unique())
    selected_country = st.sidebar.selectbox("Kraj", country_selection)
    if selected_country != "Wszystkie":
        df = df[df['Country'] == selected_country]
    #st.dataframe(data_filtered_country[columns_to_show])

    #wybor dyscypliny
    discipline_selection = ["Overall"] + ['Swim', 'Bike', 'Run']
    selected_discipline = st.sidebar.selectbox("Dyscyplina", discipline_selection)
    #df = df[df.columns[df.columns == selected_discipline]]
    #st.dataframe(data_filtered_discipline[columns_to_show])

    #wybor zakresu czasow
    max_time = df[selected_discipline].max()
    min_time = st.sidebar.number_input("Minimalny czas (sekundy)", min_value = 0, value = 0)
    max_time = st.sidebar.number_input("Maksymalny czas (sekundy)", max_value = max_time, value = max_time)
    df = df[df[selected_discipline].between(min_time, max_time)]
    #st.dataframe(data_filtered_time[columns_to_show])

    #wybor zakresu miejsc
    min_rank = st.sidebar.number_input("Minimalne miejsce", min_value = 1, value = 1)
    max_rank = st.sidebar.number_input("Maksymalne miejsce", max_value = len(df), value = len(df))
    df = df[df['Overall Rank'].between(min_rank, max_rank)]
    #st.dataframe(data_filtered_rank[columns_to_show])

    #st.dataframe(df[columns_to_show])

    #dodanie sortowania w sidebarze (malejaco/rosnaco/domyslnie)
    sort_options = ['Overall Rank', 'Swim', 'Bike', 'Run']
    selected_sort = st.sidebar.selectbox("Sortuj według", sort_options)
    sort_order = st.sidebar.radio("Kierunek sortowania", ("Rosnąco", "Malejąco"), horizontal=True)
    df = df.sort_values(by=selected_sort, ascending=(sort_order == "Rosnąco"))

    st.header("Przefiltrowana tabela wyników", text_alignment="center")
    st.dataframe(df[columns_to_show])

    #metric cards
    kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)

    mean_time = df['Overall'].mean()
    min_time = df['Overall'].min()
    max_time = df['Overall'].max()

    #konwersja czasu z sekund na godziny i minuty
    kpi1.metric(label="Ilość zawodników", value=len(df))
    kpi2.metric(label="Ilość kobiet", value=len(df[df['Gender'] == "Female"]))
    kpi3.metric(label="Ilość mężczyzn", value=len(df[df['Gender'] == "Male"]))
    kpi4.metric(label="Średni czas", value=format_time(mean_time))
    kpi5.metric(label="Najszybszy czas", value=format_time(min_time), )
    kpi6.metric(label="Najwolniejszy czas", value=format_time(max_time))

with tab2:
    st.header("Wykresy i analizy", text_alignment="center")
    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)
    #wykresy na podstawie filtracji z sidebaru

    with row1_col1:
        #rozklad czasow
        st.subheader(f"Rozkład czasów według {selected_discipline}", text_alignment="center")
        fig = px.histogram(
            df, 
            x=selected_discipline, 
            nbins=30, 
            labels={selected_discipline: "Czas (sekundy)", "count": "Liczba zawodników"}
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with row1_col2:
    #plec a wynik koncowy
        st.subheader(f"Rozkład czasu całkowitego według płci ({selected_gender})", text_alignment="center")
        fig2 = px.box(
            df,
            x = "Gender",
            y = "Overall",
            labels={selected_gender: "Płeć", "Overall": "Czas całkowity (sekundy)"}
        )
        st.plotly_chart(fig2, use_container_width=True)

    with row2_col1:
    #rower vs bieg
        st.subheader(f"Zależność między czasem roweru a czasem biegu", text_alignment="center")
        fig3 = px.scatter(
            df,
            x = "Bike",
            y = "Run",
            labels={"Bike": "Czas roweru (sekundy)", "Run": "Czas biegu (sekundy)"},
            trendline="ols",
            trendline_color_override="red" 
        )
        st.plotly_chart(fig3, use_container_width=True)

    with row2_col2:
    #top kraje
        st.subheader("Top 10 krajów według liczby zawodników", text_alignment="center")
        top_countries = df['Country'].value_counts().head(10).reset_index()
        top_countries.columns = ['Kraj', 'Liczba zawodników']
        fig4 = px.bar(
            top_countries,
            x='Kraj',
            y='Liczba zawodników',
            labels={'Kraj': 'Kraj', 'Liczba zawodników': 'Liczba zawodników'},
            color='Kraj'
        )
        st.plotly_chart(fig4, use_container_width=True)

#statystyki opisowe
with tab3:
    st.header("Statystyki opisowe", text_alignment="center")
    st.write(df.describe())

with tab4:
    st.header("Model predykcyjny", text_alignment="center")
    model = pickle.load(open('ironman_model.pkl', 'rb'))
    st.subheader("Wprowadź czasu dla poszczególnych dyscyplin w sekundach i dowiedz się, jaki będziesz mieć czas!", text_alignment="center")
    use_swim = st.checkbox("Uwzględnij czas pływania", value=True)

    if use_swim:
        swim_time = st.number_input("Czas plywania (sekundy)", min_value = 0, value = int(AVG_SWIM))
    else:
        swim_time = AVG_SWIM
    
    use_bike = st.checkbox("Uwzględnij czas roweru", value=True)
    if use_bike:
        bike_time = st.number_input("Czas roweru (sekundy)", min_value = 0, value = int(AVG_BIKE))
    else:
        bike_time = AVG_BIKE

    use_run = st.checkbox("Uwzględnij czas biegu", value=True)
    if use_run:
        run_time = st.number_input("Czas biegu (sekundy)", min_value = 0, value = int(AVG_RUN))
    else:
        run_time = AVG_RUN

    if not (use_swim or use_bike or use_run):
        st.warning("Musisz wybrać przynajmniej jedną dyscyplinę!")
        
    if st.button("Oblicz przewidywany czas całkowity"):
        predicted = model.predict([[swim_time, bike_time, run_time]])
        st.success(f"Twój przewidywany czas to: {format_time(predicted[0])}")