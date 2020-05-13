from pathlib import Path
import json
import subprocess
import cgi
import logging
import time

from fastapi import FastAPI, BackgroundTasks, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

#from win10toast import ToastNotifier
#import queue
#import threading

app = FastAPI()
#notifications = queue.Queue()
#worker = None
#stop_event = threading.Event()


def notify(title, description=""):
    powershell_special_chars = str.maketrans({'"': '`"', '`': '``'})
    title = title.translate(powershell_special_chars)
    command = f'New-BurntToastNotification -Text "{title}"'
    
    if description:
        description = description.translate(powershell_special_chars)
        command = f'New-BurntToastNotification -Text ("{title}", "{description}")'
    
    subprocess.run([
        'powershell.exe',
        command,
    ])    


#def process_notification():
#    while not stop_event.is_set():
#        title, description, data = notifications.get()
#        print(f'Worker thread: processing {title}')
#        #toaster = ToastNotifier()
#        #toaster.show_toast(title + " ", description + " ", threaded=False)
#        notify(title, description)
#        print(f'Worker thread: done!')


def new_notification(title, description="", data=""):
    print(title, description, data)
    #notifications.put_nowait((title, description, data))
    notify(title, description)


#@app.on_event("startup")
#async def startup_event():
#    worker = threading.Thread(target=process_notification)
#    worker.start()


@app.on_event("shutdown")
def shutdown_event():
#    stop_event.set()
    new_notification('Notification Server Stopped')
#    worker.join()


class NotificationData(BaseModel):
    title: str
    description: str = ""
    data: str = ""


@app.post("/json")
async def json_endpoint(*,
        n: NotificationData, 
        background_tasks: BackgroundTasks = None
    ):
    new_notification(n.title, n.description, n.data)
    return {"status": "ok"}


@app.post("/formdata", response_class=HTMLResponse)
async def formdata_endpoint(*, 
        title: str = Form(...), 
        description: str = Form(default=''), 
        data: str = Form(default=''), 
        background_tasks: BackgroundTasks = None
    ): 
    new_notification(title, description, data)
    return "<html><body><h1>Notification sent!</h1></body></html>"


@app.get("/form", response_class=HTMLResponse)
async def form_endpoint(title: str="", description: str="", data: str=""):
    title = cgi.escape(title)
    description = cgi.escape(description)
    data = cgi.escape(data)
    return f"""
    <html><form action="/formdata" method="POST">
    <label for="title">Title:</label><br/>
    <input type="text" value="{title}" name="title" id="title"/><br/><br/>
    <label for="description">Description:</label><br/>
    <input type="text" value="{description}" name="description" id="description"/><br/><br/>
    <label for="data">Data:</label><br/>
    <input type="text" value="{data}" name="data" id="data"/><br/><br/>
    <input type="submit">
    </form></html>
    """