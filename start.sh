#!/bin/bash  

# Start FastAPI using Gunicorn  
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000 &  

# Start Streamlit  
streamlit run app/streamlit_app.py --server.port 8501 --server.enableCORS false  