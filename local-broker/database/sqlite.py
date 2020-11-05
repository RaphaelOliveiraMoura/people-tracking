import sqlite3

database_name = 'sqlite.db'

connection = sqlite3.connect(database_name)

table_people_points = 'people_points'


def init():
    cursor = connection.cursor()

    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_people_points}
              (date text, iot_device_id int, x int, y int);''')

    connection.commit()


def insert_random_points(people_points):
    cursor = connection.cursor()

    query_values = [f'''(
      "{people_point['date']}",
      {people_point['iot_device_id']},
      {people_point['x']},
      {people_point['y']})''' for people_point in people_points]

    comma_query_values = ','.join(query_values)

    cursor.execute(
        f'INSERT INTO {table_people_points} VALUES {comma_query_values};')

    connection.commit()


def close_connection():
    connection.close()
