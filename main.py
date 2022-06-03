import time
from api import LastFmUser
import rpc

username = "itsnebulalol"

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