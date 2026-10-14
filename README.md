# LiveStream

A chat-room prototype built with Python’s `asyncio.Queue`. The focus is message delivery when one reader falls behind.

Each member gets a queue capped at 100 messages. When it fills, the oldest message is dropped so newer messages can still arrive. Members can join and leave rooms, and banned users are removed from every room. Posts must contain 1–500 characters.

## Run it locally

Python 3.10 or newer is enough; there are no external dependencies.

```sh
git clone https://github.com/priyamukkapati/LiveStream.git
cd LiveStream
python3 app.py
python3 -m unittest discover -s tests -v
```

The example joins a host and viewer to a room and delivers a welcome message. The test sends 105 messages to check the queue limit and drop-oldest behavior, then checks that a banned viewer cannot publish.

## What the name covers

This repository handles chat inside one process. It does not stream video or connect clients over WebSockets. Membership and messages disappear when the process stops, and moderation is a local method call without access control.

A useful next step is a WebSocket adapter with a fast reader and a deliberately slow reader, so the queue policy can be demonstrated across actual connections.
