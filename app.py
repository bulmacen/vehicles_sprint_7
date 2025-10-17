import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Gráficos del conjunto de datos de anuncios de venta de coches')
st.subheader('Construcción utilizando botones')
st.markdown('Da clic en el botón para construir el gráfico correspondiente')

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma de condición contra año del auto')

    # crear un histograma
    fig = px.histogram(car_data,
                       x="model_year",
                       color="condition",
                       barmode='stack',
                       labels={'model_year': 'Año del modelo',
                               'condition': 'Condición',
                               'count': 'Número de autos'},
                       title='Histograma de condición contra año del auto',
                       nbins=80)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True, key='histogram_button')

disp_button = st.button('Construir gráfico de dispersión')  # crear un botón
if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un gráfico de dispersión entre precio y año del auto')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data,
                     x="model_year",
                     y="price",
                     color="condition",
                     labels={'model_year': 'Año del modelo',
                             'price': 'Precio',
                             'condition': 'Condición'},
                     title='Gráfico de dispersión entre precio y año del auto',
                     hover_data=['model', 'odometer'])

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True, key='dispersion_button')

st.subheader('Construcción utilizando una casilla de verificación')
st.markdown(
    'Selecciona la casilla de verificación para construir el gráfico correspondiente')
build_histogram = st.checkbox('Construir un histograma')
build_disp = st.checkbox('Construir un gráfico de dispersión')
if build_histogram:
    # escribir un mensaje
    st.write(
        'Creación de un histograma de condición contra año del auto')

    # crear un histograma
    fig = px.histogram(car_data,
                       x="model_year",
                       color="condition",
                       barmode='stack',
                       labels={'model_year': 'Año del modelo',
                               'condition': 'Condición',
                               'count': 'Número de autos'},
                       title='Histograma de condición contra año del auto')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True, key='histogram_checkbox')
if build_disp:
    # escribir un mensaje
    st.write(
        'Creación de un gráfico de dispersión entre precio y año del auto')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data,
                     x="model_year",
                     y="price",
                     color="condition",
                     labels={'model_year': 'Año del modelo',
                             'price': 'Precio',
                             'condition': 'Condición'},
                     title='Gráfico de dispersión entre precio y año del auto',
                     hover_data=['model', 'odometer'])

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True, key='dispersion_checkbox')
