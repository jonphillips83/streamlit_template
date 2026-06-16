import streamlit as st
import pandas as pd
import pyodbc  # db connector
from src.utils import load_sql

# Securely fetch connection details from Streamlit secrets

def get_db_connection() -> pyodbc.Connection:
    # Seamlessly pull nested keys from st.secrets
    sql_server = st.secrets["sql_server"]
    driver = "{ODBC Driver 18 for SQL Server}"
    server = sql_server["server"]
    db = sql_server["database"]
    uid = sql_server.get("uid")
    pwd = sql_server.get("password")
    auth = sql_server.get("auth", "sql" if uid and pwd else "windows").lower()

    conn_parts = [
        f"DRIVER={driver}",
        f"SERVER={server}",
        f"DATABASE={db}",
        "Encrypt=no",
    ]

    if auth in {"windows", "trusted", "integrated"}:
        conn_parts.append("Trusted_Connection=yes")
    else:
        if not uid or not pwd:
            raise ValueError(
                "SQL authentication requires sql_server.uid and sql_server.password "
                "in Streamlit secrets."
            )
        conn_parts.extend([f"UID={uid}", f"PWD={pwd}"])

    conn_str = ";".join(conn_parts) + ";"
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
