## Streamlit app structure

## SQL Queries 

SQL can be added to static/sql and called with fetch_sql_query("name_of_sql_file.sql")
which will return a PANDAS Dataframe

```Python
"""The function will need to be imported from src.utils"""
from src.database import fetch_sql_query

fetch_sql_query("name_of_sql_file.sql")
```

## Load Images

Images can be stored in static/img and loaded with get_image_path("name_of_image.jpg)

```Python
import streamlit as st
from src.utils import get_image_path

st.image(get_image_path("hilarious_cat.gif"))

```

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

```Powershell
winget install --id=astral-sh.uv  -e
uv sync
uv run streamlit run
```

