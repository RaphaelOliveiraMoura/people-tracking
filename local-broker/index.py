import json
import requests
import time
import database.sqlite
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

host_name = "localhost"
server_port = 3435

thing_speak_write_key = 'OZ8NWYT5WRLPW36V'
thing_speak_base_url = 'https://api.thingspeak.com/update'


def send_data_to_sqlite(people_points):
    database.sqlite.insert_random_points(people_points)


def send_data_to_thingspeak(people_points):
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

        time.sleep(10)


class Application(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        dict_post_data = json.loads(post_data)

        def map_people_points(people_point):
            return {
                'date': str(datetime.now()),
                'iot_device_id': dict_post_data['iot_device_id'],
                'x': people_point[0],
                'y': people_point[1],
            }

        people_points = list(
            map(map_people_points, dict_post_data['random_points']))

        print(people_points)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'status': 'ok'}).encode())

        send_data_to_sqlite(people_points)
        send_data_to_thingspeak(people_points)


database.sqlite.init()
web_server = HTTPServer((host_name, server_port), Application)

print(f'Server started http://{host_name}:{server_port} ...')

try:
    web_server.serve_forever()
except:
    database.sqlite.close_connection()
    web_server.server_close()

    print("Application stopped.")
