import streamlit as st
from src.database import get_db_connection

# python -m tests.test_db

def test_db_connection():
    configured_server = st.secrets["sql_server"]["server"]
    configured_database = st.secrets["sql_server"]["database"]

    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT
                @@SERVERNAME AS server_name,
                DB_NAME() AS database_name,
                SYSTEM_USER AS login_name
            """
        )
        row = cur.fetchone()

    assert row is not None, "Expected a database response, but no row was returned."
    assert row.database_name == configured_database, (
        f"Expected database '{configured_database}', got '{row.database_name}'."
    )

    print("Connection OK")
    print(f"Configured server: {configured_server}")
    print(f"Configured database: {configured_database}")
    print(f"Connected server: {row.server_name}")
    print(f"Connected database: {row.database_name}")
    print(f"Connected as: {row.login_name}")


if __name__ == "__main__":
    test_db_connection()
