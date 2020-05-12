#!/usr/bin/env python3

import time
from urllib.request import urlopen
import json
import subprocess
import logging


def windows_notification(title, descr):
    from win10toast import ToastNotifier
    toaster = ToastNotifier()
    toaster.show_toast(title, descr, duration=10, threaded=False)


def escape(string):
    return string.translate(str.maketrans({
        "'": r"\'",
        "`": r"``",
        '"': r'\`"',
    }))


def desktop_notification(title, descr):
        import inspect
        import subprocess
        source_code = inspect.getsource(windows_notification)
        lines = source_code.splitlines()
        inner_lines = [line.strip() for line in lines[1:]]
        one_liner = ';'.join(inner_lines)
        one_liner = one_liner.replace(
            'title', 
            f"'{escape(title)} '")
        one_liner = one_liner.replace(
            'descr', 
            f"'{escape(descr)} '")
        subprocess.run([
                'powershell.exe',
                f'python -c "{one_liner}"'])


# -------------------------------------------------------


if __name__=='__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: notifier.py 127.0.0.1:9998')
        sys.exit(0)

    host = sys.argv[1]
    url = f'http://{host}/consume'

    print(f'Starting notifier, endpoint: {url}')
    desktop_notification('Notifier started', url)

    while True:
        try:
            time.sleep(1)
            response = urlopen(url, timeout=1)
            data = json.load(response)
            notif = data['notification']
            if isinstance(notif, dict):
                print(notif)
                desktop_notification(notif['title'], notif['description'])
        except KeyboardInterrupt as e:
            break
        except Exception as e:
            logging.exception('')
