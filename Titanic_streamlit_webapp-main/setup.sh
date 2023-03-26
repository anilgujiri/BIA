mkdir -p ~/.streamlit/

echo "\
http://192.168.43.240\n\
port = 8501\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
