import streamlit as st                  
from src.utils import load_css
from src.database import fetch_sql_query                        
                 
   
# Terminal helper to know when streamlit restarts it's loop
print(f'🚨 Streamlit has restarted: Reading Python script from the beginning\n')

load_css()

st.title("📊 Dashboard")
st.write("Dashboard for xyz")

df = fetch_sql_query()
st.table(df)
