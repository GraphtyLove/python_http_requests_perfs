# Http call performence
This repo demonstrate how to reduce processing time of HTTP call in python.

As the `requests` module won't allow full performances, I used the [httpx module](https://www.python-httpx.org/).

This material is highly inspired on [this video](https://www.youtube.com/watch?v=qAh5dDODJ5k). I encourage your to see it for more explainations!

## Installation
To run this code you will need the `httpx` and `requests` module.

In your projects, your should choose one of them.

You can install it with:

`pip install httpx`

## Code
You can find the here in [main.py](./main.py) with some comments.

## Perf report
Those are the result of GET requests made on `https://quotable.io/random` with a Macbook Pro 16" i9 processor on 08/08/2022.

The results could change depending on the API but the gap should be more or less the same.

### requests.get for loop
- **50 requests** = `24 sec`
- **150 requests** = `54 sec`

### Httpx.get for loop
- **50 requests** = `24 sec`
- **150 requests** = `54 sec`

### requests.Session.get SYNC for loop
- **50 requests** = `6 sec`
- **150 requests** = `19 sec`

### Httpx.client.get SYNC for loop
- **50 requests** = `6 sec`
- **150 requests** = `19 sec`

### Httpx.client.get ASYNC for loop
- **50 requests** = `6 sec`
- **150 requests** = `19 sec`

### Httpx.client.get ASYNC tasks
- **50 requests** = `6 sec`
- **150 requests** = `1.6 sec`
- **1000 requests** = `9 sec`