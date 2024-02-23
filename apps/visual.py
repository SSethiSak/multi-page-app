import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import plotly.express as px

def app():

    st.subheader("Sepal Width correlation with species")
    df = px.data.iris()
    fig = px.scatter(
        df,
        x="sepal_width",
        y="species",
        color="species",
        color_continuous_scale="reds",
    )
    
    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    with tab2:
        st.plotly_chart(fig, theme=None, use_container_width=True)

    

    st.subheader("Sepal Length correlation with species")
    fig2 = px.scatter(
        df,
        x="sepal_length",
        y="species",
        color="species",
        color_continuous_scale="blues",
    )
    
    tab3, tab4 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab3:
        st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    with tab4:
        st.plotly_chart(fig2, theme=None, use_container_width=True)


    st.subheader("Petal Width correlation with species")
    fig3 = px.scatter(
        df,
        x="petal_width",
        y="species",
        color="species",
        color_continuous_scale="blues",
    )
    
    tab5, tab6 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab5:
        st.plotly_chart(fig3, theme="streamlit", use_container_width=True)
    with tab6:
        st.plotly_chart(fig3, theme=None, use_container_width=True)


    st.subheader("Petal Length correlation with species")
    fig4 = px.scatter(
        df,
        x="petal_length",
        y="species",
        color="species",
        color_continuous_scale="blues",
    )
    
    tab7, tab8 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab7:
        st.plotly_chart(fig4, theme="streamlit", use_container_width=True)
    with tab8:
        st.plotly_chart(fig4, theme=None, use_container_width=True)