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

def home(mode):
    st.title('Project Among Us')
    st.subheader('Why Among Us and Who we are')
    st.markdown("Hello Everyone! Do you know  the Among Us Game? This phenomenal game is growing fast in Google Play and App Store Platform. Some Colleagues and I who have graduated from IYKRA Data MBA Batch IV, tried to scrap, analyze, and visualize comment sections of this games. Our results can be accessed by clicking dashboard on the sidebar.")
    st.markdown("")
    st.markdown("And Let me Introduce the team who is involved in this project:")
    st.markdown("1. [Imam Bhaskara](https://www.linkedin.com/in/imam-bhaskara)")
    st.markdown("2. [Ricky Nauvaldy Ruliputra](https://www.linkedin.com/in/rickynauvaldy/)")
    st.markdown("3. [Rahman Firmansyah](https://www.linkedin.com/in/rahman-firmansyah-79283512b/?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAB_7KR4BIiHd_IuPKvxTwNtnaMDJFlT339I)")
    st.markdown("4. [Arnold P](https://www.linkedin.com/in/arnold-p/)")
    st.markdown("5. [Cahya Putera](https://www.linkedin.com/in/cahyaputera/)")
    st.markdown("6. [Winata Syahputera](https://www.linkedin.com/in/winata-syahputra/)")
    st.markdown("7. [Muhamad Teo Khibran](https://www.linkedin.com/in/teokhibran/)")

def dashboard_amongus(mode):
    st.title(mode)
    st.header ("Among Us Dataframe")
    st.table(df.head(6))

    df_temp_rate = df.groupby(['Rate'])[['Pengguna']].count()
    df_temp_rate.reset_index(inplace=True)

    st.header("Grafik Distribusi Rating Among Us")
    fig_pie = px.pie(df_temp_rate, values='Pengguna', names='Rate', title='Distribusi Rating Among Us')
    st.plotly_chart(fig_pie)

    df_temp_tanggal_rate = df.groupby(['Rate','Tanggal'])[['Pengguna']].count()
    df_temp_tanggal_rate.reset_index(inplace=True)

    st.header("Grafik Rating Among Us oleh User")
    fig_line = px.line(df_temp_tanggal_rate, x='Tanggal', y='Pengguna', color='Rate', title='Rating Among Us Sepanjang Oktober - November')
    st.plotly_chart(fig_line)

def main():
    main_mode = st.sidebar.selectbox('Pilih menu yang ingin dikunjungi',
        ['Home', 'Dashboard Among Us']
    )

    if main_mode == 'Home':
        home(main_mode)
    elif main_mode == 'Dashboard Among Us':
        dashboard_amongus(main_mode)

if __name__ == '__main__':
    main()