import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('datos/vehicles_us.csv')

st.header("Visualización de datos de vehículos usados")

st.dataframe(car_data)

# BOTÓN 
hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches'
    )

    fig = px.histogram(
        car_data,
        x="odometer",
        title="Distribución del kilometraje"
    )

    st.plotly_chart(fig, use_container_width=True, key="hist_button")

# histograma de precio con checkbox
build_histogram = st.checkbox('Mostrar histograma de precio')

if build_histogram:
    st.write('Histograma del precio (controlado por checkbox)')

    fig_checkbox = px.histogram(
        car_data,
        x="price",
        title="Distribución del precio (checkbox)"
    )

    st.plotly_chart(fig_checkbox, use_container_width=True, key="hist_checkbox")