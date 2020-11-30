import json
import requests
import time
from database import sqlite
from datetime import datetime
from utils.set_interval import set_interval

thing_speak_write_key = 'OZ8NWYT5WRLPW36V'
thing_speak_base_url = 'https://api.thingspeak.com/update'

emit_signal_interval = 20

total_time_calculation = 60
min_time_calculation = 15


def send_data_to_thingspeak():
    people_points = sqlite.get_unread_points()

    for people_point in people_points:
        params = {
            "api_key": thing_speak_write_key,
            "field1": people_point['iot_device_id'],
            "field2": people_point['x'],
            "field3": people_point['y'],
            "field4": people_point['date'],
        }

        print(f'sending {people_point} data to thing speak ...')

        response = requests.get(thing_speak_base_url, params=params)

        print(f'status: {response.status_code} text: {response.text}')

        slice_time = total_time_calculation / len(people_points)
        time_to_sleep = slice_time if slice_time >= min_time_calculation else min_time_calculation

        time.sleep(time_to_sleep)


sqlite.init()
set_interval(emit_signal_interval, send_data_to_thingspeak)
