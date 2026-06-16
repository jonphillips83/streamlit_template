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


def stat_card(title, value, delta, status="normal"):
    """
    A reusable dashboard card with custom HTML/CSS coloring 
    based on system status.
    """
    badge_color = "#28a745" if status == "normal" else "#dc3545"
    
    html_content = f"""
    <div class="custom-card">
        <p class="card-title">{title}</p>
        <h2 class="card-value">{value}</h2>
        <span class="card-delta" style="color: {badge_color};">{delta}</span>
    </div>
    """
    return st.markdown(html_content, unsafe_allow_html=True)


def server_status_header(container_name, status):
    """A reusable header to display Docker container status."""
    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader(f"🎛️ System: {container_name}")
    with col2:
        if status == "connected":
            st.success("SQL Server Live")
        else:
            st.error("Connection Lost")