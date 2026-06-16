import streamlit as st


def user_card(username, email, role):
    """A reusable UI component for displaying user info."""
    html_content = f"""
    <div class="user-card">
        <h3>{username}</h3>
        <p><strong>Email:</strong> {email}</p>
        <span class="badge">{role}</span>
    </div>
    """
    return st.markdown(html_content, unsafe_allow_html=True)