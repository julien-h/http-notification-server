# Notification server and client

```
.
├── client
│   └── notifier.py
└── server
    ├── main.py
    └── run.sh
```

This repository holds the code for my HTTP-based notification server and the python client used to display notification on the desktop.

The companion blog post is available here: https://julienharbulot.com/notification-server.html

## How to use

Make sure that docker is installed and running. Start the notification server. Then start the python client.

```bash
./server/run.sh
cd client
./notifier.py
```

## Platform specific code

The current `notifier.py` implementation is for Windows's WSL. It should work on python windows' too, but code can be made simpler (see the blog post).

Pull requests with notifiers implementations for linux and OSX are welcome.