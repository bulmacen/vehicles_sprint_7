import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Gráficos del conjunto de datos de anuncios de venta de coches')
st.subheader('Construcción utilizando botones')
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="model")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True, key='histogram_button')

disp_button = st.button('Construir gráfico de dispersión')  # crear un botón
if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="model", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True, key='dispersion_button')

st.subheader('Construcción utilizando una casilla de verificación')
build_histogram = st.checkbox('Construir un histograma')
build_disp = st.checkbox('Construir un gráfico de dispersión')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna modelo')
    fig = px.histogram(car_data, x="model")
    st.plotly_chart(fig, use_container_width=True, key='histogram_checkbox')

if build_disp:  # si la casilla de verificación está seleccionada
    st.write('Construir un gráfico de dispersión para la columna modelo')
    fig = px.scatter(car_data, x="model", y="price")
    st.plotly_chart(fig, use_container_width=True, key='dispersion_checkbox')
