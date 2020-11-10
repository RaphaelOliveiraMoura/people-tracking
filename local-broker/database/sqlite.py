import sqlite3

database_name = 'database/sqlite.db'

connection = sqlite3.connect(database_name, check_same_thread=False)

table_people_points = 'people_points'


def init():
    cursor = connection.cursor()

    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_people_points}
              (date text, iot_device_id int, x int, y int, read int);''')

    connection.commit()


def insert_random_points(people_points):
    if len(people_points) == 0:
        return

    cursor = connection.cursor()

    query_values = [f'''(
      "{people_point['date']}",
      {people_point['iot_device_id']},
      {people_point['x']},
      {people_point['y']},
      0)''' for people_point in people_points]

    comma_query_values = ','.join(query_values)

    cursor.execute(
        f'INSERT INTO {table_people_points} VALUES {comma_query_values};')

    connection.commit()


def get_unread_points():
    cursor = connection.cursor()

    cursor.execute(
        f'SELECT * FROM {table_people_points} WHERE read = 0;')

    query_result = cursor.fetchall()

    cursor.execute(
        f'UPDATE {table_people_points} SET read = 1 WHERE read = 0;')

    connection.commit()

    def map_people_points(people_point):
        return {
            'date': people_point[0],
            'iot_device_id': people_point[1],
            'x': people_point[2],
            'y': people_point[3],
        }

    people_points = list(map(map_people_points, query_result))

    return people_points


def close_connection():
    connection.close()
