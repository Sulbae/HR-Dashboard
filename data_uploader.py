import pandas as pd
from sqlalchemy import create_engine

CSV_URL = 'https://raw.githubusercontent.com/Sulbae/HR-Dashboard/refs/heads/main/employee_data.csv'

df = pd.read_csv(CSV_URL)

DATABASE_URL = "postgresql://postgres:9c3UpYRDtrSN3gvJ@db.npxskcigiuiwqdowjouc.supabase.co:5432/postgres"

engine = create_engine(DATABASE_URL)
df.to_sql('employees', con=engine, if_exists='replace', index=False)