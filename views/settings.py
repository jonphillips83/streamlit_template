import streamlit as st                  
from src.utils import load_css, get_image_path, log_streamlit_rerun

# Terminal helper to know when streamlit restarts it's loop
log_streamlit_rerun()
load_css()

st.title("⚙️ Settings")
st.write("Update views/settings.py to alter display")
st.image(get_image_path("wtf.gif"))
