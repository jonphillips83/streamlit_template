import streamlit as st
import pandas as pd
import pyodbc  # db connector
from src.utils import load_sql

# Securely fetch connection details from Streamlit secrets

def get_db_connection():
    # Seamlessly pull nested keys from st.secrets
    driver = "{ODBC Driver 18 for SQL Server}"
    server = st.secrets["sql_server"]["server"]
    db = st.secrets["sql_server"]["database"]
    uid = st.secrets["sql_server"]["uid"]
    pwd = st.secrets["sql_server"]["password"]
    
    conn_str = f"DRIVER={driver};SERVER={server};DATABASE={db};UID={uid};PWD={pwd};Encrypt=no;"
    return pyodbc.connect(conn_str)

@st.cache_data(ttl=600) # Caches results in memory for 10 minutes (600 seconds)
def fetch_events():
    """Fetches and caches all events for the dashboard."""
    query = load_sql("select.sql")
    
    with get_db_connection() as conn:
        # Reading directly into a Pandas DataFrame keeps things incredibly clean
        df = pd.read_sql(query, conn)
    
    return df

@st.cache_data(ttl=600) # Caches results in memory for 10 minutes (600 seconds)
def fetch_venue():
    """Fetches and caches all venues for the dashboard."""

    query = """
        SELECT * FROM venue
    """
    
    with get_db_connection() as conn:
        # Reading directly into a Pandas DataFrame keeps things incredibly clean
        df = pd.read_sql(query, conn)
    
    return df
