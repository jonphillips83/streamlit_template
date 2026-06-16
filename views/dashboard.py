import streamlit as st                  
from src.utils import load_css, get_image_path   
from src.database import fetch_sql_query                        
import pandas as pd                     
from datetime import date               
import numpy as np                     
   
# Terminal helper to know when streamlit restarts it's loop
print(f'🚨 Streamlit has restarted: Reading Python script from the beginning\n')

load_css()

st.title("📊 Events Dashboard")
st.write("Here is an overview of all available events.")

df = fetch_sql_query()
st.table(df)
