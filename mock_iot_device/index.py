import random
import sys
import requests
import json
from threading import Timer

local_broker_url = 'http://localhost:3435'

iot_device_id = sys.argv[1]

print(f'device {iot_device_id} started')

room_width = 10
room_heigth = 10

people_range_min = 0
people_range_max = 10

emit_signal_interval = 20


def coordinates_random_generate():
    x = random.randrange(0, room_width + 1)
    y = random.randrange(0, room_heigth + 1)
    return [x, y]


def people_points_random_generate():
    people_length = random.randint(people_range_min, people_range_max)
    return [coordinates_random_generate() for _ in range(people_length)]


def set_interval(timer, task):
    is_stop = task()
    if not is_stop:
        Timer(timer, set_interval, [timer, task]).start()


def send_data_to_local_broker():
    random_points = people_points_random_generate()

    print(f'generated points {random_points}')

    body = {
        'iot_device_id': iot_device_id,
        'random_points': random_points
    }

    try:
        print('sending data to local broker ...')
        response = requests.post(local_broker_url, data=json.dumps(body))
        print(f'status: {response.status_code} text: {response.text}')
    except:
        print('error in local broker connection ...')


set_interval(emit_signal_interval, send_data_to_local_broker)
