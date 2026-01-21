import os
import mysql.connector


SQL_HOST = os.getenv("SQL_HOST", 'localhost')
SQL_PORT = os.getenv("SQL_PORT", 3307)
SQL_USER = os.getenv("SQL_USER", 'root')
SQL_PASSWORD = os.getenv("SQL_PASSWORD", '')
SQL_DATABASE = os.getenv("SQL_DATABASE", 'weather')



class DbConnection:
    def __init__(self, host, port, user, password, database):
        self.config = {
            'host': host,
            'port': port,
            'user': user,
            'password': password
        }
        self.database = database
        self.connection = None


    def get_connection(self):
        self.connection = mysql.connector.connect(**self.config)

        if not self.connection.is_connected:
            raise ConnectionError("Couldn't connect to the database")

        cursor = self.connection.cursor()            
        return cursor



    def create_table(self):
        cursor = self.get_connection()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")

        cursor.execute(f"USE {self.database}")

        create_statement = """
            CREATE TABLE IF NOT EXISTS records (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
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
            );"""

        cursor.execute(create_statement)
        self.connection.commit()
    


    def insert_records(self, records):
        cursor = self.get_connection()
        cursor.execute(f"USE {self.database}")

        insert_statement = """INSERT INTO records (
                timestamp, location_name, country,
                latitude, longitude, temperature, wind_speed, humidity, temperature_category, wind_category)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ;"""

        values = [tuple(record.values()) for record in records]

        if len(values) > 1:
            cursor.executemany(insert_statement, values)
        elif len(values) == 1:
            cursor.execute(insert_statement, values[0])
        else:
            print('There are no record to insert')

        self.connection.commit()
        return cursor.rowcount
