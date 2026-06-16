import streamlit as st
from src.utils import get_image_path, load_css

# Terminal helper to know when streamlit restarts it's loop
print(f'🚨 Streamlit has restarted: Reading Python script from the beginning\n')

# Inject css
load_css()

st.markdown('<div class="login-shell"><div class="login-card">', unsafe_allow_html=True)
card_left, card_right = st.columns([1.05, 1], gap="large")

with card_left:
    image_path = get_image_path("whistle.gif")
    if image_path:
        st.image(image_path)


with card_right:
    st.markdown(
        """
        <div class="login-copy">
            <div class="login-kicker">Secure Access</div>
            <div class="login-title">Welcome back</div>
            <div class="login-text">
                Sign in to continue to the dashboard. This is still the lightweight
                placeholder login, but the layout now behaves more like a proper entry screen.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    col1, col2, button_col = st.columns([3.4, 0.2, 1])
    with button_col:
        st.write("")
        st.write("")
        if st.button("Login", use_container_width=True):
            if username == "admin" and password =='1234':
                st.session_state.logged_in = True
                st.success('✔️ Jackpot')
                st.rerun()
            else:               
                st.error('❌ Error')


st.markdown("</div></div>", unsafe_allow_html=True)
