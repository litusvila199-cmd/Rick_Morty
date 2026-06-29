import pandas as pd
import logging



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def transform_characters():

    try:

        df = pd.read_json("data/raw/characters_raw.json")

        df = df[["id", "name", "status", "species", "gender", "origin", "created"]]

        df["origin_name"] = df["origin"].apply(lambda x: x["name"])

        df = df.drop(columns=["origin"])

        df["created"] = pd.to_datetime(df["created"])

        df.to_csv("data/processed/characters_processed.csv", index=False)

        logger.info("Processed file saved to data/processed/characters_processed.csv")

    except Exception as e:
        logger.error(f"Error during transformation: {e}")
        raise


if __name__ == "__main__":
    transform_characters()





