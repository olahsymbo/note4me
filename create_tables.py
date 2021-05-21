import psycopg2
from db_config import *
import warnings
warnings.filterwarnings("ignore")

# get the postgres db connection parameters from environment variable
name = os.environ.get('name')
user = os.environ.get('user')
password = os.environ.get('password')
host = os.environ.get('host')
port = os.environ.get('port')

# connect an instance of postgres DB
con = psycopg2.connect(database=name, user=user, password=password, host=host, port=port)
print("Database opened successfully")

cursor = con.cursor()

## creating tables
cursor.execute("CREATE SCHEMA noteschema "
               "CREATE TABLE notes "
               "(id SERIAL PRIMARY KEY NOT NULL, "
               "title VARCHAR(300) NOT NULL, "
               "content VARCHAR(250) NOT NULL, "
               "created TIMESTAMP NOT NULL, "
               "due_date TIMESTAMP NOT NULL)")

cursor.execute("CREATE TABLE category "
               "(name VARCHAR(300) NOT NULL)")

print("Table created successfully")
con.commit()
con.close()