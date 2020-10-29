import random
from threading import Timer


local_broker_url = 'http://localhost:5000'

room_width = 10
room_heigth = 10

people_range_min = 0
people_range_max = 10

emit_signal_interval = 2


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
    print(people_points_random_generate())


setInterval(emit_signal_interval, emit_signal_from_random_people)
