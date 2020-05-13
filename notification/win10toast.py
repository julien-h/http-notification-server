import threading, queue
import win10toast


notifications = queue.Queue()
worker = None
stop_event = threading.Event()


def start():
    worker = threading.Thread(target=process_notification)
    worker.start()


def stop():
    stop_event.set()
    worker.join()


def notify(title, description="", data=""):
    notifications.put_nowait((title, description, data))


def process_notification():
    while not stop_event.is_set():
        title, description, data = notifications.get()
        print(f'Worker thread: processing {title}')
        toaster = win10toast.ToastNotifier()
        toaster.show_toast(title + " ", description + " ", threaded=False)
