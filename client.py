#!/usr/bin/env python3
import requests
import logging

host = '127.0.0.1:8000'
notify_response = None


def send_notification(title, description="", data=""):
    global notify_response
    notify_response = requests.post(f'http://{host}/json', json={
        "title": title,
        "description": description,
        "data": data
    })
    if notify_response.status_code != 200:
        logging.error(f'notify("{title}") failed')


if __name__ == '__main__':
    send_notification('Hello!', 'Notification sent from the python client.')