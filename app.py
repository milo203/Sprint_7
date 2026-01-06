"""Creación de aplicación básica para streamlit y plotly.express."""

import pandas as pd
import plotly.express as px
import streamlit as st

# Load car data
car_data = pd.read_csv("vehicles_us.csv")
# Configurar el título de la aplicación
st.title("Análisis de Datos de Vehículos en EE.UU.")
# Create a button to show the hist plot
hist_button = st.button("Mirar Histograma de Precios de Autos")
if hist_button:
    st.write("Creando Histograma de Precios de Autos...")
    fig_hist = px.histogram(
        car_data, x="price", nbins=50, title="Histogram of Car Prices"
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# Create a button to show the scatter plot
scatter_button = st.button("Mirar Gráfico de Dispersión de Precio vs Odómetro")
if scatter_button:
    st.write("Creando Gráfico de Dispersión de Precio vs Odómetro...")
    fig_scatter = px.scatter(
        car_data, x="odometer", y="price", title="Price vs Odometer"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

st.write("Aplicación creada por Emiliano Espejel")
