import streamlit as st                  
                  
st.set_page_config(page_title="Box Office", page_icon="🎟️", layout="wide")

# Initialize session state for security/auth
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# Router
login_page = st.Page("views/login.py", title="Log In", icon="🔒", url_path="login")
home = st.Page("views/home.py", title="Home", icon="🏠",url_path="home")

dashboard = st.Page("views/dashboard.py", title="Dashboard", icon="📊",url_path="dashboard")

settings = st.Page("views/settings.py", title="Settings", icon="⚙️",url_path="settings")
help = st.Page("views/help.py", title="Help", icon="🆘",url_path="help")

statistics = st.Page("views/statistics_101.py", title="Statistics 101", icon="🧮",url_path="statistics_101")
encryption = st.Page("views/rsa_example.py", title="RSA Encryption", icon="🔑",url_path="encryption")

# Conditional Routing (Role/Auth based)
if not st.session_state.logged_in:
    # If not logged in, they ONLY see the login page
    pg = st.navigation([login_page])
else:
    # If logged in, group pages neatly into sidebar sections
    # Register Pages Here
    pg = st.navigation({
        "Main Hub": [home, dashboard],
        "Management": [settings, help],
        "Experiments": [encryption, statistics]
    })

# Run the selected page
pg.run()





