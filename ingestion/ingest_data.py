import pandas as pd
from sqlalchemy import create_engine

# connection
DB_URI = "postgresql://user:password@localhost:5432/datawarehouse"

engine = create_engine(DB_URI)

def load_csv():
    print("Starting ingestion...")

    df = pd.read_csv("data/sample_data.csv")

    # basic cleaning
    df.columns = [c.lower() for c in df.columns]

    # load to postgres
    df.to_sql("raw_data", engine, if_exists="replace", index=False)

    print("Data loaded successfully!")
    print(df.head())

if __name__ == "__main__":
    load_csv()