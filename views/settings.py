import streamlit as st                  
from src.utils import load_css, get_image_path, load_markdown

# Terminal helper to know when streamlit restarts it's loop
print(f'🚨 Streamlit has restarted: Reading Python script from the beginning\n')

load_css()

st.title("⚙️ Settings")

line = "string"
st.toast(f'''Multi  
             line  
             {line}''')