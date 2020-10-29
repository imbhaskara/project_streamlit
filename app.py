#import package
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.express as px
import plotly.graph_objects as go

#import data
drive_path = './'
df = pd.read_excel(drive_path+'Komen Play Among Us1.xlsx',index_col='Unnamed: 0')

def dashboard_amongus(mode):
    st.title(mode)
    st.header ("Among Us Dataframe")
    st.table(df.head(6))

    df_temp_tanggal_rate = df.groupby(['Rate','Tanggal'])[['Pengguna']].count()
    df_temp_tanggal_rate.reset_index(inplace=True)

    st.header("Grafik Rating Among Us oleh User")
    fig_line = px.line(df_temp_tanggal_rate, x='Tanggal', y='Pengguna', color='Rate', title='Rating Among Us Sepanjang Oktober - November')
    st.plotly_chart(fig_line)

    df_temp_rate = df.groupby(['Rate'])[['Pengguna']].count()
    df_temp_rate.reset_index(inplace=True)

    st.header("Grafik Distribusi Rating Among Us")
    fig_pie = px.pie(df_temp_rate, values='Pengguna', names='Rate', title='Distribusi Rating Among Us')
    st.plotly_chart(fig_pie)

def main():
    main_mode = st.sidebar.selectbox('Pilih menu yang ingin dikunjungi',
        ['Home', 'Dashboard Among Us']
    )

    if main_mode == 'Home':
        st.title('Project Among Us - Imam Bhaskara')
        st.markdown('Orang-orang yang terlibat dalam Project Ini')
    elif main_mode == 'Dashboard Among Us':
        dashboard_amongus(main_mode)

if __name__ == '__main__':
    main()