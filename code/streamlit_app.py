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

#######################

# Load in the happiness data
data = pd.read_csv("data/simulated_data.csv")
data['Date'] = pd.to_datetime(data['Date'])

#######################

# Plots
## Function to plot the over-all happiness level
def plot_happiness_level(df):
    fig = px.scatter(df, x='Date', y='Happiness_Level',
                 trendline="rolling", trendline_options=dict(window=100),
                 trendline_color_override='Steelblue',
                 trendline_scope='overall')
    fig.data = [t for t in fig.data if t.mode == "lines"]
    fig.update_layout(yaxis_title='Happiness')
    fig.update_traces(line=dict(width=6))
    fig.update_traces(showlegend=False)

    return fig

## Function to plot the histogram of the happiness levels
def happiness_histogram(df):
    fig = px.histogram(df, x='Happiness_Level', 
                       color_discrete_sequence=['steelblue'])
    fig.update_layout(bargap=0.1)
    fig.update_layout(xaxis_title='Happiness')
    fig.update_layout(yaxis_title='')
    return fig



#######################

# Set-up sidebar for subset selection
with st.sidebar:
    st.title('🥳 Happiness Dashboard')
    
    year_list = list(data.Date.dt.year.unique())[::-1]
    
    selected_year = st.selectbox('Select a year', year_list, index=len(year_list)-1)
    df_selected_year = data[data.Date.dt.year == selected_year]
    df_selected_year_sorted = df_selected_year.sort_values(by="Happiness_Level", ascending=False)

    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

#######################
# Main Panels
#######################

# Nr of columns to display (3)
col = st.columns((5.5, 2.5), gap='medium')

#######################

# Column 0: Line chart
with col[0]:
    st.markdown("#### Overall Happiness Score")

    line_graph = plot_happiness_level(df_selected_year)
    st.plotly_chart(line_graph)

    histo_graph = happiness_histogram(df_selected_year)
    st.plotly_chart(histo_graph)

# Column 1: .... 
with col[1]:
    st.markdown("#### Overall Happiness Score")

    line_graph = plot_happiness_level(df_selected_year)
    st.plotly_chart(line_graph)

    histo_graph = happiness_histogram(df_selected_year)
    st.plotly_chart(histo_graph)