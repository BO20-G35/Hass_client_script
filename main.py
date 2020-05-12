import requests
import json
import socket
import sys
import time

if len(sys.argv) != 2:
    print("Missing url to hass os")
    sys.exit(1)

url = str(sys.argv[1])

data = {'username': 'admin', 
        'password': 'SIN{0452d68b490312580451c60caedcd1f1}',
        'client_id': 'https://home-assistant.io/android',
        }


headers = {
"Host": "10.0.0.137:8123",
"Connection": "keep-alive",
"Content-Length": "87",
"Origin": "http://10.0.0.137:8123",
"User-Agent": "Mozilla/5.0 (Linux; Android 9; Android SDK built for x86 Build/PSR1.180720.093; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36",
"Content-Type": "text/plain;charset=UTF-8",
"Accept": "*/*",
"Referer": "http://10.0.0.137:8123/auth/authorize?response_type=code&client_id=https://home-assistant.io/android&redirect_uri=homeassistant://auth-callback",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-US",
"X-Requested-With": "io.homeassistant.companion.android.debug"
}


post = requests.post(url, data=json.dumps(data), headers=headers)
print(post.status_code)
