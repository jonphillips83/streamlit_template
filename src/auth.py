import bcrypt
import streamlit as st


def _get_admin_password_hash() -> str | None:
    """Fetch the stored bcrypt hash for the admin account from Streamlit secrets."""

    auth_secrets = st.secrets.get("auth", {})

    return auth_secrets.get("admin_password_hash")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Compare a plaintext password to a stored bcrypt hash."""

    if not plain_password or not hashed_password:
        return False

    try:
        return bcrypt.checkpw(
            plain_password.encode("utf-8"),
            hashed_password.encode("utf-8"),
        )
    except ValueError:
        return False


def authenticate_user(username: str, password: str) -> bool:
    """Validate the admin user against the bcrypt hash stored in secrets.toml."""

    if username != "admin":
        return False

    hashed_password = _get_admin_password_hash()
    return verify_password(password, hashed_password) if hashed_password else False
