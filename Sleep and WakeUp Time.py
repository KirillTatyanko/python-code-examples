import json
import os


def read_sleep_and_wakeup_time(json_file):
    try:
        with open(json_file, 'r') as read_file:
            data = json.load(read_file)
            return data
    except FileNotFoundError:
        return []
    except EOFError as error:
        print(error)
        return []


def set_sleep_and_wakeup_time(event, date, time):
    data_to_write = {
        'event': event,
        'date': date,
        'time': time
    }
    if not os.path.exists('data.json'):
        with open('data.json', 'a+') as file:
            json.dump([data_to_write], file)
    else:
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        data.append(data_to_write)
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)
