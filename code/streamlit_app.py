import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Happiness Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Dark mode. Fight me!
alt.themes.enable("dark")   

