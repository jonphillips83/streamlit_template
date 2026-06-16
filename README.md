## Streamlit app structure


my_streamlit_app/
│
├── .streamlit/
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
│   ├── home.py
│   └── dashboard.py
│
└── streamlit_app.py         # Clean entry point 

```Powershell
uv run streamlit run
```

