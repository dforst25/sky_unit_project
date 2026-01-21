import mysql.connector



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

        return self.connection            



    def create_table(self):
        cnx = self.get_connection()
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

        with cnx.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")

            cursor.execute(f"USE {self.database}")

            cursor.execute(create_statement)
            self.connection.commit()
        


    def insert_records(self, records):
        cnx = self.get_connection()

        insert_statement = """INSERT INTO records (
                    timestamp, location_name, country,
                    latitude, longitude, temperature, wind_speed, humidity, temperature_category, wind_category)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ;"""

        values = [tuple(record.values()) for record in records]
        row_count = 0
        with cnx.cursor() as cursor:
            cursor.execute(f"USE {self.database}")

            if len(values) > 1:
                cursor.executemany(insert_statement, values)
            elif len(values) == 1:
                cursor.execute(insert_statement, values[0])
            else:
                raise ValueError("No records to insert")
            row_count = cursor.rowcount


        cnx.commit()
        return row_count

    def get_records_count(self):
        cnx = self.get_connection()
        select_count_statement = """SELECT location_name, COUNT(*) as count
                                    FROM records
                                    GROUP BY location_name
                                    ORDER BY count DESC;"""
        with cnx.cursor(dictionary=True) as cursor:
            cursor.execute(f"USE {self.database}")
            cursor.execute(select_count_statement)
            result = cursor.fetchall()
        return result

        