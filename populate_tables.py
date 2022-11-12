import logging
import pandas as pd
import sys
import argparse
from sqlalchemy import create_engine

# Defining the constants
POSTGRES_USERNAME = ""
POSTGRES_PASSWORD = ""
POSTGRES_URL = ""
POSTGRES_PORT = 5432
POSTGRES_DATABASE = ""

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def populate_tables(dataframe, engine, table_name):
    logging.info(f"Populating the {table_name} table")
    # Save the dataframe to the database
    dataframe.to_sql(table_name, engine, index=False, if_exists="replace")


def create_database_engine(connection_string):
    logging.info("Creating the database engine")
    # Create a database engine
    engine = create_engine(connection_string)
    return engine


def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data-path", type=str, help="Path to the data", required=True)
    parser.add_argument("-t", "--table-name", type=str, help="Name of the table", required=True)
    args = parser.parse_args()

    # Logging welcome message
    logging.info(f"Reading data from {args.data_path}")

    # Create a dataframe
    df = pd.read_csv(args.data_path)

    # Define connection string
    connection_string = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_URL}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"

    # Create a database engine
    engine = create_database_engine(connection_string)

    # Save the dataframe to the database
    populate_tables(df, engine, table_name=args.table_name)


if __name__ == "__main__":
    main()