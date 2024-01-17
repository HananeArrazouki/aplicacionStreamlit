FROM python:3.8
RUN pip install pandas scikit-learn streamlit numpy matplotlib seaborn
COPY src/app.py /app/
COPY csv/employees.csv /app/csv
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]