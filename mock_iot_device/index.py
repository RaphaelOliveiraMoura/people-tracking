import random
import sys
import requests
import time
from datetime import datetime
from threading import Timer

local_broker_url = 'http://localhost:5000'

iot_device_id = sys.argv[1]

print(f'device {iot_device_id} started')

room_width = 10
room_heigth = 10

people_range_min = 0
people_range_max = 10

emit_signal_interval = 20

thing_speak_write_key = 'OZ8NWYT5WRLPW36V'
thing_speak_base_url = 'https://api.thingspeak.com/update'


def person_point_random_generate():
    random_width = random.randrange(0, room_width + 1)
    random_heigth = random.randrange(0, room_heigth + 1)
    return [random_width, random_heigth]


def people_points_random_generate():
    people_length = random.randint(people_range_min, people_range_max)
    return [person_point_random_generate() for _ in range(people_length)]


def setInterval(timer, task):
    isStop = task()
    if not isStop:
        Timer(timer, setInterval, [timer, task]).start()


def emit_signal_from_random_people():
    random_points = people_points_random_generate()

    print(f'generated points {random_points}')

    for random_point in random_points:
        params = {
            "api_key": thing_speak_write_key,
            "field1": iot_device_id,
            "field2": random_point[0],
            "field3": random_point[1],
            "field4": datetime.now(),
        }

        print(f'sending {random_point} data...')

        r = requests.get(thing_speak_base_url, params=params)

        print(f'status: {r.status_code} text: {r.text}')

        time.sleep(10)


setInterval(emit_signal_interval, emit_signal_from_random_people)
