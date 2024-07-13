import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

# page config
st.set_page_config(
    page_title="Streamlit App",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)
alt.themes.enable("dark") # darkmode

# hier css
# --------
# ....
# -------- 


# load data 
data = pd.read_csv("data/simulated_data.csv")

# add sidebar

# add main content
# add plots and charts

# Donuts

# layout

