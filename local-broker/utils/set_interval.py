from threading import Timer


def set_interval(timer, task):
    is_stop = task()
    if not is_stop:
        Timer(timer, set_interval, [timer, task]).start()
