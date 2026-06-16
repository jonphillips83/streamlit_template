import streamlit as st                  
from src.utils import load_css, load_markdown, log_streamlit_rerun

# Terminal helper to know when streamlit restarts it's loop
log_streamlit_rerun()
load_css()

st.title("🏠 Home")
st.write("Update views/home.py to alter display")
st.markdown(load_markdown("lorem.md"))

