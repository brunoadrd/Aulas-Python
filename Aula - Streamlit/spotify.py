import streamlit as st
import pandas as pd

st.set_page_config(
    layout = 'wide',
    page_title = 'Spotify Songs'
)

@st.cache_data
def load_data():
    df = pd.read_csv('Datasets/01 Spotify.csv')
    return df

df = load_data()

st.session_state['df_spotify'] = df

artists = df['Artist'].value_counts().index
artist = st.sidebar.selectbox('Artista', artists)
df_filtered = df[df['Artist'] == artist].set_index('Track')

albums = df_filtered['Album'].value_counts().index
album = st.selectbox('Album', albums)
df_filtered2 = df_filtered[df_filtered['Album'] == album]

col1, col2 = st.columns([0.7, 0.3])

agree = st.checkbox('Mostrar Gráfico')

if agree:
    col1.bar_chart(df_filtered2['Stream'])
    col2.line_chart(df_filtered2['Danceability'])



