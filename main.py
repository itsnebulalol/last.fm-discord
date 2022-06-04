import time
from api import LastFmUser
import rpc
import json

try:
    with open("config.json", "r") as f:
        data = json.load(f)
except:
    jsondata = {
        "username": "itsnebulalol",
    }

    try:
        with open("config.json", "w") as f:
            json.dump(jsondata, f)
    except:
        print("An error occured trying to make the config file.")
        exit(1)

    print("config.json file not found, one was created for you. Please edit the username and rerun the script.")
    exit(1)

def get_config(key):
    return data[key]

username = get_config("username")

rpc_state = True
def toggle_rpc(item):
    global rpc_state
    rpc_state = not item.checked

def main():
    print("Starting RPC")
    while True:
        if rpc_state is True:
            user.now_playing()
        else:
            rpc.disconnect()
            time.sleep(2)

print("Last.fm username: " + username)
user = LastFmUser(username, 2)

if __name__ == "__main__":
    main()