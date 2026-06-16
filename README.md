# Streamlit App Template

## SQL Queries

SQL can be added to static/sql and called with fetch_sql_query("name_of_sql_file.sql")
which will return a PANDAS Dataframe

```Python
"""The function will need to be imported from src.utils"""
from src.database import fetch_sql_query

fetch_sql_query("name_of_sql_file.sql")
```

`get_db_connection()` supports both SQL Server authentication and Windows integrated authentication.

For SQL Server authentication, use:

```toml
[sql_server]
server = "localhost,1433"
database = "my_database"
uid = "sa"
password = "your_password"
auth = "sql"
```

For Windows integrated authentication, omit `uid` and `password`, or set `auth = "windows"`:

```toml
[sql_server]
server = "WINDOWS-SERVER\\INSTANCE"
database = "my_database"
auth = "windows"
```

## Load Images

Images can be stored in static/img and loaded with get_image_path("name_of_image.jpg)

```Python
import streamlit as st
from src.utils import get_image_path

st.image(get_image_path("hilarious_cat.gif"))

```

## Load CSS

Css can be stored in static/css and loaded with load_css() at the top of the streamlit page.

```Python
from src.utils import load_css

# Inject css
load_css()
```

## Load JS

Javascript can be stored in static/js and loaded with load_js("script_name.js") at the bottom of the streamlit page.

```Python
from src.utils import load_js

# ...CODE
# ... MORE CODE
# ... ALL THE CODE

# Inject js
load_js()
```

## Load Markdown

Markdown can be stored in static/md and loaded with load_markdown("name_of_markdown_file.md").

```Python
import streamlit as st                  
from src.utils import load_markdown

st.markdown(load_markdown("lorem.md"))
```

## File Structure
```
my_streamlit_app/
│
├── .streamlit/
│   ├── secrets.toml
│   └── config.toml          # Global theme settings (primary color, fonts)
│
├── static/
│   ├── css/
│   │   └── style.css        # Custom CSS goes here
│   ├── md/                  # Markdown can be read from here
│   │   └── lorem.md
│   ├── js/                  # JS can be read from here
│   ├── sql/                 # SQL Queries can be read from here
│   │   └── select.sql       
│   └── images/              # Images can be read from here
│
├── src/                     # Core python logic
│   ├── __init__.py
│   ├── database.py          # Database queries / bcrypt logic
│   └── utils.py             # Helper functions
│
├── views/                   # Multipage UI layouts (if applicable)
│   ├── login.py
│   ├── home.py
│   ├── dashboard.py
│   └── settings.py
│
├── pyproject.toml           # Dependency requirements
└── streamlit_app.py         # Clean entry point 
```

## Installation

```Powershell

"""Install uv via winget"""
winget install --id=astral-sh.uv  -e

"""Sync project dependencies and run"""
uv sync
uv run streamlit run
```

