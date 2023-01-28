import requests
import time
import threading

access_token = "2-293819-1214327995-7PkaI2hSx6Pny"
headers = {
    "Authorization": f"OAuth {access_token}",
}

url = "https://api-v2.soundcloud.com/users/1214327995?client_id=wuM9g7pMB4mU13fW6SuRfQeJNRYNIX9O&app_version=1674570068&app_locale=en"


username='fsdufsd88'

# function to send a PUT request
def change_username(username):
    data = {"permalink": username}

    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 200:
        print(time.time(), ":", f"Username changed to {username} successfully.")
    else:
        print(time.time(), ":", f"Failed to change username to {username}. Error: {response.json()}")
        print(f"Error Code:{response.status_code}")
        print(f"Error Message:{response.content}")

# set the desired rate of requests per second
rate = 100

# set the number of requests to send
num_requests = 100

# create a list of threads
threads = []

# create and start a thread for each request
for i in range(num_requests):
    t = threading.Thread(target=change_username, args=(username,))
    t.start()
    threads.append(t)

# wait for all threads to finish
for t in threads:
    t.join()

access_token = '2-293819-1214327995-7PkaI2hSx6Pny'
username = 'hafsdfsdfsd9ii'
