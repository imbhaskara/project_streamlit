#import package
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.express as px
import plotly.graph_objects as go
import base64

#import data
drive_path = './'
df = pd.read_excel(drive_path+'Komen Play Among Us1.xlsx',index_col='Unnamed: 0')
image_path = drive_path + 'images/'

def image_to_base64(image_full_path):
    """Convert image file to base64"""
    file_ = open(image_full_path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url

def home(mode):
    # Image resource set
    avatar_arnold = image_to_base64(image_path+"/arnold.jpg")
    avatar_cahya = image_to_base64(image_path+"/cahya.jpg")
    avatar_imam = image_to_base64(image_path+"/imam.jpg")
    avatar_rahman = image_to_base64(image_path+"/rahman.jpg")
    avatar_ricky = image_to_base64(image_path+"/ricky.jpg")
    avatar_teo = image_to_base64(image_path+"/teo.jpg")
    avatar_winata = image_to_base64(image_path+"/winata.jpg")
    
    st.title('Project Among Us')
    st.subheader('Why Among Us and Who we are')
    st.markdown("Hello Everyone! Do you know  the Among Us Game? This phenomenal game is growing fast in Google Play and App Store Platform. Some Colleagues and I who have graduated from IYKRA Data MBA Batch IV, tried to scrap, analyze, and visualize comment sections of this games. Our results can be accessed by clicking dashboard on the sidebar.")
    st.markdown("")
    st.markdown("And let me Introduce the team involved in this project:")
    template_html = f"""
    <ul class="collection">
        <li class="collection-item avatar">
            <img src="data:image/jpg;base64,{avatar_imam}"  alt="Imam Bhaskara" class="circle">
            <span class="title">Imam Bhaskara</span>
            <p>Analyst <br>
                Linkedin: <a href="https://www.linkedin.com/in/imam-bhaskara" class="linkedin-link">Imam Bhaskara</a>
            </p>
        </li>
        <li class="collection-item avatar">
            <img src="data:image/jpg;base64,{avatar_ricky}"  alt="Ricky Nauvaldy Ruliputra" class="circle">
            <span class="title">Ricky Nauvaldy Ruliputra</span>
            <p>Analyst <br>
                Linkedin: <a href="https://www.linkedin.com/in/rickynauvaldy/" class="linkedin-link">Ricky Nauvaldy Ruliputra</a>
            </p>
        </li>
        <li class="collection-item avatar">
            <img src="data:image/jpg;base64,{avatar_rahman}"  alt="Rahman Firmansyah" class="circle">
            <span class="title">Rahman Firmansyah</span>
            <p>Analyst <br>
                Linkedin: <a href="https://www.linkedin.com/in/rahman-firmansyah-79283512b" class="linkedin-link">Rahman Firmansyah</a>
            </p>
        </li>
        <li class="collection-item avatar">
            <img src="data:image/jpg;base64,{avatar_cahya}"  alt="Cahya Putera" class="circle">
            <span class="title">Cahya Putera</span>
            <p>Analyst <br>
                Linkedin: <a href="https://www.linkedin.com/in/cahyaputera/" class="linkedin-link">Cahya Putera</a>
            </p>
        </li>
        <li class="collection-item avatar">
            <img src="data:image/jpg;base64,{avatar_winata}"  alt="Winata Syahputera" class="circle">
            <span class="title">Winata Syahputera</span>
            <p>Analyst <br>
                Linkedin: <a href="https://www.linkedin.com/in/winata-syahputra/" class="linkedin-link">Winata Syahputera</a>
            </p>
        </li>
        <li class="collection-item avatar">
            <img src="data:image/jpg;base64,{avatar_teo}"  alt="Muhamad Teo Khibran" class="circle">
            <span class="title">Muhamad Teo Khibran</span>
            <p>Analyst <br>
                Linkedin: <a href="https://www.linkedin.com/in/teokhibran/" class="linkedin-link">Muhamad Teo Khibran</a>
            </p>
        </li>
        <li class="collection-item avatar">
            <img src="data:image/jpg;base64,{avatar_arnold}"  alt="Arnold P" class="circle">
            <span class="title">Arnold P</span>
            <p>Analyst <br>
                Linkedin: <a href="https://www.linkedin.com/in/arnold-p/" class="linkedin-link">Arnold P</a>
            </p>
        </li>
    </ul>
    """
    st.markdown(template_html, unsafe_allow_html=True)

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