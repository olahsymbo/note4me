import os
import psycopg2
from dotenv import load_dotenv
import warnings

warnings.filterwarnings("ignore")

load_dotenv()
# get the postgres db connection parameters from environment variable
name = os.getenv("DATABASE_NAME")
user = os.getenv("DATABASE_USERNAME")
password = os.getenv("DATABASE_PASSWORD")
host = os.getenv("DATABASE_HOST")
port = os.getenv("DATABASE_PORT")

# connect an instance of postgres DB
con = psycopg2.connect(
    database=name, user=user, password=password, host=host, port=port
)
print("Database opened successfully")

cursor = con.cursor()

# creating tables
cursor.execute(
    "CREATE SCHEMA noteschema "
    "CREATE TABLE notes "
    "(id SERIAL PRIMARY KEY NOT NULL, "
    "title VARCHAR(300) NOT NULL, "
    "content VARCHAR(250) NOT NULL, "
    "created TIMESTAMP NOT NULL, "
    "due_date TIMESTAMP NOT NULL)"
)

# cursor.execute(
#     "CREATE TABLE notes "
#     "(id SERIAL PRIMARY KEY NOT NULL, "
#     "title VARCHAR(300) NOT NULL, "
#     "content VARCHAR(250) NOT NULL, "
#     "created TIMESTAMP NOT NULL, "
#     "due_date TIMESTAMP NOT NULL)"
# )

cursor.execute("CREATE TABLE category " "(name VARCHAR(300) NOT NULL)")

print("Table created successfully")
con.commit()
con.close()
