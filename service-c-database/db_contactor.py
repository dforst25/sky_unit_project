import os
import mysql.connector




SQL_HOST = os.getenv("SQL_HOST")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
SQL_DATABASE = os.getenv("SQL_DATABASE")


def connect_to_database():
    db_connector = mysql.connector.connect(
    host=SQL_HOST,
    user=SQL_USER,
    password=SQL_PASSWORD
    )
    if not db_connector.is_connected:
        raise ConnectionError("Could not connect to database")

    create_table = """CREATE TABLE IF NOT EXISTS records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME  NOT NULL,
    location_name VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    temperature FLOAT NOT NULL,
    wind_speed FLOAT NOT NULL,
    humidity INT NOT NULL,
    temperature_category VARCHAR(255) NOT NULL,
    wind_category VARCHAR(255) NOT NULL
    )"""
    cursor = db_connector.cursor().execute(create_table)
    cursor.close()
    db_connector.commit()


    return db_connector



def insert_records(records, db_connector):
    cursor = db_connector.cursor()
    sql = "INSERT INTO customers () VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = [(row for row in record) for record in records]
    cursor.executemany(sql, val)
    cursor.close()
    db_connector.commit()


    return cursor.rowcount











