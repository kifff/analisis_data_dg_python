import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dasboard/main_data.csv")

st.title("Dasboard peminjaman sepeda")

kolom_opsi =['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit',
            'temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt', 'hr']

pilihan = st.selectbox("Pilih kolom untuk melihat visiual data :" , kolom_opsi)

st.markdown("---")

if df[pilihan].nunique() <= 20:
    st.subheader(f"Jumlah data berdasarkan : {pilihan}")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(x=pilihan , y='cnt',data=df,estimator=sum,ci=None,palette="Set2",ax=ax )
    plt.xlabel(pilihan.capitalize())
    plt.ylabel("Total peminjaman (cnt)")
    st.pyplot(fig)

else:
    st.subheader(f"📊 Distribusi Nilai: {pilihan.capitalize()}")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(df[pilihan], bins=30, kde=True, color='skyblue', ax=ax)
    plt.xlabel(pilihan.capitalize())
    plt.ylabel("Frekuensi")
    st.pyplot(fig)    
    
    
    
    
