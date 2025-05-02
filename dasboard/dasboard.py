
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("dasboard/main_data.csv")

data['dteday'] = pd.to_datetime(data['dteday'])

data['season'] = data['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
data['mnth'] = data['mnth'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})
data['weekday'] = data['weekday'].map({
    0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
    4: 'Thursday', 5: 'Friday', 6: 'Saturday'
})
data['weathersit'] = data['weathersit'].map({
    1: 'Clear', 2: 'Mist + Cloudy', 3: 'Light Snow/Rain', 4: 'Heavy Rain'
})
data['holiday'] = data['holiday'].map({0: 'No', 1: 'Yes'})
data['workingday'] = data['workingday'].map({0: 'No', 1: 'Yes'})
data['yr'] = data['yr'].map({0: '2011', 1: '2012'})
data['hr'] = data['hr'].astype(str)

st.title("Dashboard Peminjaman Sepeda 🚲")

st.sidebar.header("Filter Tanggal")
start_date = st.sidebar.date_input("Mulai Tanggal", value=data['dteday'].min())
end_date = st.sidebar.date_input("Akhir Tanggal", value=data['dteday'].max())

filtered_data = data[(data['dteday'] >= pd.to_datetime(start_date)) & (data['dteday'] <= pd.to_datetime(end_date))]

columns = ['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit',
           'temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt', 'hr']
selected_col = st.selectbox("Pilih kolom untuk visualisasi:", columns)

# Visualisasi
st.subheader(f"Visualisasi Kolom: {selected_col}")
if filtered_data[selected_col].nunique() < 15:
    fig, ax = plt.subplots()
    sns.countplot(x=selected_col, data=filtered_data, palette="Set2", ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)
else:
    fig, ax = plt.subplots()
    sns.histplot(filtered_data[selected_col], kde=True, color="skyblue", bins=30, ax=ax)
    st.pyplot(fig)



