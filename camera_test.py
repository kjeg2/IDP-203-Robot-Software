import json
import requests

r = requests.get(url= 'http://localhost:8081/stream/video.mjpeg', stream=True)

if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    if line:
        print(json.loads(line))