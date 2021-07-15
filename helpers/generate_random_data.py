import os

import psycopg2
from datetime import datetime
import warnings
from faker import Faker
from dotenv import load_dotenv

warnings.filterwarnings("ignore")

load_dotenv()

con = psycopg2.connect(
    database=os.getenv("DATABASE_NAME"),
    user=os.getenv("DATABASE_USERNAME"),
    password=os.getenv("DATABASE_PASSWORD"),
    host=os.getenv("DATABASE_HOST"),
    port=os.getenv("DATABASE_PORT"),
)
print("Database opened successfully")

cursor = con.cursor()

fake = Faker()

for i in range(1000):
    # another_model_instance = Category.objects.get(id=1)
    title = fake.sentence()
    content = fake.paragraph()
    created = datetime.now().strftime("%Y-%m-%d")
    due_date = datetime.now().strftime("%Y-%m-%d")
    id = fake.random_digit_not_null()
    cursor.execute(
        "INSERT INTO notes (title,content, created, due_date) VALUES (%s, %s, %s, %s)",
        (title, content, created, due_date),
    )
con.commit()
print("Records created successfully!")
con.close()
