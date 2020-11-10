import sys
import random
from database import sqlite
from datetime import datetime
from utils.set_interval import set_interval


iot_device_id = sys.argv[1]

print(f'device {iot_device_id} started')

room_width = 10
room_heigth = 10

people_range_min = 0
people_range_max = 10

emit_signal_interval = 10


def coordinates_random_generate():
    x = random.randrange(0, room_width + 1)
    y = random.randrange(0, room_heigth + 1)
    return [x, y]


def people_points_random_generate():
    people_length = random.randint(people_range_min, people_range_max)
    return [coordinates_random_generate() for _ in range(people_length)]


def send_data_to_sqlite():
    random_points = people_points_random_generate()

    print(f'generated points {random_points}')

    def map_people_points(people_point):
        return {
            'date': str(datetime.now()),
            'iot_device_id': iot_device_id,
            'x': people_point[0],
            'y': people_point[1],
        }

    people_points = list(map(map_people_points, random_points))

    try:
        print('saving data in sqlite ...')
        sqlite.insert_random_points(people_points)
        print('data saved with success')
    except:
        print('error savving data in sqlite ...')


sqlite.init()
set_interval(emit_signal_interval, send_data_to_sqlite)
