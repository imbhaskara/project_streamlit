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
    templete_html = """
    <ul class="collection">
        <li class="collection-item avatar">
            <img src="(/images/imam.jpg)" alt="images/imam.jpg" class="circle">
            <span class="title">Imam Bhaskara</span>
            <p>Analyst <br>
                Linkedin: <a href="https://www.linkedin.com/in/imam-bhaskara" class="linkedin-link">Imam Bhaskara</a>
            </p>
        </li>
        <li class="collection-item avatar">
            <img src="(/images/imam.jpg)" alt="images/imam.jpg" class="circle">
            <span class="title">Ricky Nauvaldy Ruliputra</span>
            <p>Analyst <br>
                Linkedin: <a href="https://www.linkedin.com/in/rickynauvaldy/" class="linkedin-link">Ricky Nauvaldy Ruliputra</a>
            </p>
        </li>
        <li class="collection-item avatar">
            <img src="(/images/imam.jpg)" alt="images/imam.jpg" class="circle">
            <span class="title">Rahman Firmansyah</span>
            <p>Analyst <br>
                Linkedin: <a href="https://www.linkedin.com/in/rahman-firmansyah-79283512b/?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAB_7KR4BIiHd_IuPKvxTwNtnaMDJFlT339I" class="linkedin-link">Rahman Firmansyah</a>
            </p>
        </li>
        <li class="collection-item avatar">
            <img src="(/images/imam.jpg)" alt="images/imam.jpg" class="circle">
            <span class="title">Cahya Putera</span>
            <p>Analyst <br>
                Linkedin: <a href="https://www.linkedin.com/in/cahyaputera/" class="linkedin-link">Cahya Putera</a>
            </p>
        </li>
        <li class="collection-item avatar">
            <img src="(/images/imam.jpg)" alt="images/imam.jpg" class="circle">
            <span class="title">Winata Syahputera</span>
            <p>Analyst <br>
                Linkedin: <a href="https://www.linkedin.com/in/winata-syahputra/" class="linkedin-link">Winata Syahputera</a>
            </p>
        </li>
        <li class="collection-item avatar">
            <img src="(/images/imam.jpg)" alt="images/imam.jpg" class="circle">
            <span class="title">Muhamad Teo Khibran</span>
            <p>Analyst <br>
                Linkedin: <a href="https://www.linkedin.com/in/teokhibran/" class="linkedin-link">Muhamad Teo Khibran</a>
            </p>
        </li>
        <li class="collection-item avatar">
            <img src="(/images/imam.jpg)" alt="images/imam.jpg" class="circle">
            <span class="title">Arnold P</span>
            <p>Analyst <br>
                Linkedin: <a href="https://www.linkedin.com/in/arnold-p/" class="linkedin-link">Arnold P</a>
            </p>
        </li>
    </ul>
    """
    st.markdown(templete_html, unsafe_allow_html=True)

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

def init():
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">', unsafe_allow_html=True)
    st.markdown('<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>', unsafe_allow_html=True)

def main():
    init()
    main_mode = st.sidebar.selectbox('Pilih menu yang ingin dikunjungi',
        ['Home', 'Dashboard Among Us']
    )

    if main_mode == 'Home':
        home(main_mode)
    elif main_mode == 'Dashboard Among Us':
        dashboard_amongus(main_mode)

if __name__ == '__main__':
    main()