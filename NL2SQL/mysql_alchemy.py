from mysql_alchemy import create_engine, text
from nl2sql import response
from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME 
# Create Engine
engine = create_engine(
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

cursor = engine.connect()

final_output = cursor.execute(response)
