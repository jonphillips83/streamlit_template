from datetime import datetime
import inspect
import streamlit as st              
from pathlib import Path            # pathlib instead of OS (cleaner, modern, easier to reason about)
import re


def load_css(file_name: str = "styles.css") -> None:
    """
    Reads a CSS file from static/css/ and injects it into the Streamlit app.
    Defaults to 'styles.css' if no file name is provided.
    """
    
    css_path = Path.cwd() / "static" / "css" / file_name
    
    if css_path.exists():
        # .read_text() opens, reads, and closes the file automatically
        css_content = css_path.read_text(encoding="utf-8")
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    else:
        st.warning(f"CSS file not found: {css_path}")


@st.cache_data # Decorator Function to cache the data
def load_markdown(file_name: str) -> str:
    """Reads a markdown file from the md/ directory."""

    markdown_path = Path.cwd() / "static" / "md" / file_name
    if markdown_path.exists():
        return markdown_path.read_text(encoding="utf-8")
    return f"⚠️ Markdown file `{file_name}` not found."


def load_sql(file_name: str) -> str:
    """Reads a SQL file from the sql/ directory."""

    sql_path = Path.cwd() / "static" / "sql" / file_name
    if sql_path.exists():
        return sql_path.read_text(encoding="utf-8")
    raise FileNotFoundError(f"⚠️ SQL file not found: {sql_path}")


def get_image_path(file_name: str) -> Path | None:

    """
    Returns the absolute path string for an image in static/img/.
    """
    img_path = Path.cwd() / "static" / "img" / file_name
    
    if img_path.exists():
        # st.image accepts pathlib.Path objects directly!
        return img_path
        
    st.error(f"❌ Image not found: {file_name}")
    return None


def load_js(file_name: str) -> None:
    """
    Reads a JavaScript file from static/js/, wraps it in a DOMContentLoaded
    listener to ensure it runs at the bottom of the page, and injects it.
    """
    js_path = Path.cwd() / "static" / "js" / file_name
    
    if js_path.exists():
        # Read the raw javascript code from the file
        js_content = js_path.read_text(encoding="utf-8")
        
        # Wrap it in a listener so it executes safely after the DOM renders
        html_block = f"""
        <script>
            document.addEventListener("DOMContentLoaded", function() {{
                {js_content}
            }});
        </script>
        """
        st.markdown(html_block, unsafe_allow_html=True)
    else:
        st.warning(f"🖲️ JavaScript file not found: {js_path}")


def log_streamlit_rerun() -> None:
    """Print a simple timestamped message whenever a Streamlit page reruns."""

    timestamp = datetime.now().strftime("%H:%M")
    caller_file = inspect.stack()[1].filename
    page_name = Path(caller_file).stem
    print(f"🚨 Streamlit rerun at {timestamp} from {page_name}")


def check_valid_email(email: str) -> bool:

    # Regex pattern matcher

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if re.match(pattern, email):
        
        return True
    
    else:

        return False