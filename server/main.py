from fastapi import FastAPI
from pathlib import Path
from collections import deque
import json

app = FastAPI()
notifications_path = Path('./notifications.json')


def load_notifications():
    try:
        with notifications_path.open('r', encoding='utf8') as f:
            return json.load(f)
    except Exception as e:
        print(e)
        return []

def save_notifications(notifications):
    with notifications_path.open('w', encoding='utf8') as f:
        json.dump(notifications, f, ensure_ascii=False)


@app.get("/new")
def new_notification(title: str, description: str = "", data: str = ""):
    notifications = load_notifications()
    notifications.append({'title':title, 'description':description, 'data':data})
    save_notifications(notifications)
    print(notifications)
    return {"status": "ok"}


@app.get("/consume")
def consume_notification():
    notifications = load_notifications()
    if notifications:
        item = notifications.pop(0)
        save_notifications(notifications)
        return {'notification': item}
    else:
        return {'notification': "none"}
