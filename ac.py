import requests
import json
import threading
import time



def check_username(username, semaphore):
    response = requests.get(f'https://api-auth.soundcloud.com/web-auth/identifier?q={username}&client_id=wuM9g7pMB4mU13fW6SuRfQeJNRYNIX9O')
    data = response.json()
    if data["status"] == "available":
        import hai
        print(time.time(), ":", username, "was claimed.")
        exit()
    else:
        print(time.time(), ":", username, "is not available.")
    semaphore.release()

def threaded_check(username, num_threads):
    semaphore = threading.Semaphore(num_threads)
    while True:
        semaphore.acquire()
        thread = threading.Thread(target=check_username, args=(username, semaphore))
        thread.start()

username = "autoclaimtester999"
num_threads = 7
threaded_check(username, num_threads)
