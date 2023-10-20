#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for _ in range(10000):
    sleep(random.random())
    ip_address = ".".join(str(random.randint(1, 255)) for _ in range(4))
    http_status = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    request_size = random.randint(1, 1024)
    timestamp = datetime.datetime.now()

    log_entry = f"{ip_address} - [{timestamp}] \"GET /projects/260 HTTP/1.1\" {http_status} {request_size}\n"
    
    sys.stdout.write(log_entry)
    sys.stdout.flush()
