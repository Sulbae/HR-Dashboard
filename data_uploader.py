import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('')

URL = "postgresql://postgres:9c3UpYRDtrSN3gvJ@db.npxskcigiuiwqdowjouc.supabase.co:5432/postgres"

engine = create_engine(URL)
df.to_sql('orders', con=engine, if_exists='replace', index=False)