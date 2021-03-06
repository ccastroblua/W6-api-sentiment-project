import os
import dotenv
import sqlalchemy as alch

dotenv.load_dotenv()

# Get password from .env and uses "slack" DB.
password = os.getenv("sql_pass")
db_name = "slack"

# Connecting with MySQL DB "slack".
connection = f"mysql+pymysql://root:{password}@localhost/{db_name}"
engine = alch.create_engine(connection)

# Informs that it's connected to the specified DB.
print(f"Conectado a mysql / base de datos: {db_name}")