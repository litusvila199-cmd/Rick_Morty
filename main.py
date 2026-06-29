from src.extract.api_extractor import extract_characters
from src.transform.transform_characters import transform_characters
from src.load.postgres_loader import load_characters

def main():

    extract_characters()
    transform_characters()
    load_characters()

if __name__ == "__main__":
    main()    