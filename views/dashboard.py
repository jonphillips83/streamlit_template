import streamlit as st                  
from src.utils import load_css, log_streamlit_rerun
from src.database import fetch_sql_query                        
                 
# Terminal helper to know when streamlit restarts it's loop
log_streamlit_rerun()
load_css()

st.title("📊 Dashboard")
st.write("Update views/dashboard.py to alter display")
st.write("""This page is connected to the database but you will need to update 
         secrets.toml and static/sql/query.sql to ensure that you are connecting to the correct
         database name and table""")


df = fetch_sql_query("select.sql") # SQL statement loaded from static/sql
st.table(df)
