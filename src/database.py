import streamlit as st
import pandas as pd
import pyodbc  # db connector
from src.utils import load_sql

# Securely fetch connection details from Streamlit secrets

def get_db_connection() -> pyodbc.Connection:
    # Seamlessly pull nested keys from st.secrets
    driver = "{ODBC Driver 18 for SQL Server}"
    server = st.secrets["sql_server"]["server"]
    db = st.secrets["sql_server"]["database"]
    uid = st.secrets["sql_server"]["uid"]
    pwd = st.secrets["sql_server"]["password"]
    
    conn_str = f"DRIVER={driver};SERVER={server};DATABASE={db};UID={uid};PWD={pwd};Encrypt=no;"
    return pyodbc.connect(conn_str)

@st.cache_data(ttl=600) # Caches results in memory for 10 minutes (600 seconds)
def fetch_sql_query(file_name: str) -> pd.DataFrame:
    """Fetches and caches query results from a SQL file."""
    query = load_sql(file_name)
    
    with get_db_connection() as conn:
        # Reading directly into a Pandas DataFrame keeps things incredibly clean
        df = pd.read_sql(query, conn)
    
    return df
@st.cache_data(ttl=600) # Caches results in memory for 10 minutes (600 seconds)
def generic_inline_sql_fetch():
    """Fetches and caches data from database with an inline query."""

    query = """
        SELECT * FROM venue
    """
    
    with get_db_connection() as conn:
        # Reading directly into a Pandas DataFrame keeps things incredibly clean
        df = pd.read_sql(query, conn)
    
    return df
