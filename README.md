# Rick & Morty ETL Pipeline

## Overview

This project is a simple ETL (Extract, Transform, Load) pipeline built with Python.

The pipeline:

1. Extracts character data from the Rick & Morty API.
2. Transforms and cleans the data using pandas.
3. Loads the processed data into a PostgreSQL database.

The goal of this project is to practice the fundamentals of Data Engineering, including ETL development, project organization, Git workflow and database loading.

---

## Technologies

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Requests
- python-dotenv

---

## Project Structure

```
Rick_Morty/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── extract/
│   ├── transform/
│   ├── load/
│   └── pipeline/
│
├── tests/
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## ETL Flow

```
Rick & Morty API
        │
        ▼
Extract
        │
        ▼
characters_raw.json
        │
        ▼
Transform
        │
        ▼
characters_processed.csv
        │
        ▼
Load
        │
        ▼
PostgreSQL
```

---

## Installation

Clone the repository:

```bash
git clone <repository_url>
cd Rick_Morty
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file with:

```text
API_URL=https://rickandmortyapi.com/api/character

DB_NAME=your_database
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

## Run the project

```bash
python main.py
```

---

## Features

- API extraction
- Data transformation with pandas
- PostgreSQL loading
- Logging
- Error handling with try/except
- Environment variables
- Modular project structure