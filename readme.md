# Notification server

A simple http-based notification server in Python.

See: http://julienharbulot.com/notification-server.html

## Install

There are two components:
1. The server 
2. The desktop notification library

To install the server requirements:

```
pip install fastapi uvicorn
```

If you're on windows, you can also install the following notification library and you're good to go:

```
pip install win10toast
```

For alternative notification clients, see below.

## Run

Run this command in the repo's directory to start the server:

```
uvicorn notification_server:app
```

You can run the client script to make sure everything works. You'll need the python `requests` library for the python implementation:

```
pip install requests
python client.py
```

Or you can use the bash client (which requires `curl`):

```
./client.sh
```

## Alternative notification clients

To see available implementations for the notification client, head to the `/notification` directory.

So far, I have implemented:
- `win10toast.py` which is based on the [win10toast](https://pypi.org/project/win10toast/) library;
- `burnttoast.py` which requires `powershell.exe` and the [BurntToast](https://github.com/Windos/BurntToast) module; 
    Imho, this implementation is better than win10toast because the notifications remain in Windows' notification center until manually removed.
- Pull requests with implementations for other platforms are welcome.

To switch implementation, edit the `import` statement in `notification_server.py`.

For win10toast:

```
from notification import win10toast as notifier
```

For the BurntToast implementation:

```
from notification import burnttoast as notifier
```

## Author & licence

MIT License.

Author: Julien Harbulot