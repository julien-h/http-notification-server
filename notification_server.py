import logging, cgi

from fastapi import FastAPI, BackgroundTasks, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from notification import win10toast as notifier


app = FastAPI()


def new_notification(title, description="", data=""):
    maybe = lambda x: "\n" + x if x else ""
    logging.info(f'Notification: {title}{maybe(description)}{maybe(data)}')
    notifier.notify(title, description)


@app.on_event("startup")
def startup_event():
    notifier.start()


@app.on_event("shutdown")
def shutdown_event():
    notifier.notify('Notification Server Stopped')
    notifier.stop()


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


@app.get("/", response_class=HTMLResponse)
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
