import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


def load_characters():
    load_dotenv()

    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")

    df = pd.read_csv("data/processed/characters_processed.csv")

    engine = create_engine(
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )

    df.to_sql(
        name="characters",
        con=engine,
        if_exists="replace",
        index=False,
    )

    print("Characters loaded successfully into PostgreSQL.")


if __name__ == "__main__":
    load_characters()