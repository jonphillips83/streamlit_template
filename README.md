## Streamlit app structure


```
my_streamlit_app/
│
├── .streamlit/
│   ├── secrets.toml
│   └── config.toml          # Global theme settings (primary color, fonts)
│
├── static/
│   ├── css/
│   │   └── style.css        # ALL your custom CSS goes here
│   └── images/
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
"Run these from inside vscode terminal once you have the project"
uv sync
uv run streamlit run
```

