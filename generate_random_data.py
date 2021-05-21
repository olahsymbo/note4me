import psycopg2
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

from faker import Faker

from db_config import *

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

fake = Faker()

for i in range(1000):
    # another_model_instance = Category.objects.get(id=1)
    title = fake.sentence()
    content=fake.paragraph()
    created = datetime.now().strftime("%Y-%m-%d")
    due_date = datetime.now().strftime("%Y-%m-%d")
    id =fake.random_digit_not_null()
    cursor.execute("INSERT INTO noteschema.notes (title,content, created, due_date) VALUES (%s, %s, %s, %s)",
                   (title, content, created, due_date))
con.commit()
print("Records created successfully")
con.close()