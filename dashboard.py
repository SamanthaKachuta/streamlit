import streamlit as st
import plotly.express as px
import pandas as pd 
import os
import warnings
warnings.filterwarnings('ignore')
import matplotlib
print(matplotlib.__version__)

st.set_page_config(page_title="Superstore!!!", page_icon=":bar_chart", layout="wide")
st.title(":bar_chart: Sam SuperStore")
