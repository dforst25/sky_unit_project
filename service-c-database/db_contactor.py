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

        with cnx.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT COUNT(*) FROM records;')
            length_before = cursor.fetchone()[0]

            cursor.execute(f"USE {self.database}")

            if len(values) > 1:
                cursor.executemany(insert_statement, values)
            elif len(values) == 1:
                cursor.execute(insert_statement, values[0])
            else:
                raise ValueError("No records to insert")
            
            row_count = cursor.rowcount
            
            cursor.execute('SELECT COUNT(*) FROM records;')
            length_after = cursor.fetchone()

        cnx.commit()
        return {'message': 
                f'All records in database: {length_before}.'
                f'All records inserted: {row_count}. All records in database yet: {length_after}.'
                }


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
    


    def get_avg_temperature(self):
        cnx = self.get_connection()
        select_avg_statement = """SELECT location_name, AVG(temperature) as avg_temperature
                                    FROM records
                                    GROUP BY location_name
                                    ORDER BY location_name;"""
        
        with cnx.cursor(dictionary=True) as cursor:
            cursor.execute(f"USE {self.database}")
            cursor.execute(select_avg_statement)
            result = cursor.fetchall()
        return result
    


    def get_max_wind_speed(self):
        cnx = self.get_connection()
        select_max_statement = """SELECT location_name, MAX(wind_speed) as max_wind_speed
                                    FROM records
                                    GROUP BY location_name
                                    ORDER BY location_name;"""
        
        with cnx.cursor(dictionary=True) as cursor:
            cursor.execute(f"USE {self.database}")
            cursor.execute(select_max_statement)
            result = cursor.fetchall()
        return result


    def get_extreme_records(self):
        cnx = self.get_connection()
        select_extreme_statement = """SELECT *
   FROM(SELECT location_name, temperature_category, wind_category
        FROM records r1
        GROUP BY location_name, temperature_category, wind_category
        HAVING COUNT(*) = (SELECT MAX(count)
                           FROM (SELECT location_name, COUNT(*) AS count
                                 FROM records r2
                                 WHERE r1.location_name = r2.location_name
                                 GROUP BY location_name, temperature_category, wind_category) T2
        ) T1
   WHERE (temperature_category = 'hot' AND wind_category = 'calm')
   OR (temperature_category = 'cold' AND wind_category = 'windy')
   ;"""

        
        with cnx.cursor(dictionary=True) as cursor:
            cursor.execute(f"USE {self.database}")
            cursor.execute(select_extreme_statement)
            result = cursor.fetchall()
        return result




















"""SELECT location_name, MAX(count)
   FROM (SELECT location_name, temperature_category, wind_category, COUNT(*) AS count
        FROM records
        GROUP BY location_name, temperature_category, wind_category) AS T
   GROUP BY location_name;"""