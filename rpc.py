from pypresence import Presence
import datetime
import time

client_id = '982286050858795008'
presence = Presence(client_id)
already_enabled = False
already_disabled = True
start_time = None
last_track = None

def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def enable_rpc():
    global already_enabled,already_disabled
    if already_enabled == False:
        presence.connect()
        print('Connected with Discord')
        already_enabled = True
        already_disabled = False


def update_status(track, album, time_remaining):
    global start_time, last_track
    if last_track == track:
        pass
    else:
        print("Now Playing: " + track)
        start_time = datetime.datetime.now().timestamp()
        last_track = track
        trackList = track.split('-')
        time_remaining = str(time_remaining)[0:3]
        if time_remaining != '0':
            if album != 'None':
                presence.update(details=trackList[1], state=album, end=float(time_remaining) + start_time,
                    large_image='icon', large_text='Last.fm')
            else:
                presence.update(details=trackList[1], state=trackList[0], end=float(time_remaining) + start_time,
                    large_image='icon', large_text='Last.fm')
        else:
            if album != 'None':
                presence.update(details=trackList[1], state=album,
                    large_image='icon', large_text='Last.fm')
            else:
                presence.update(details=trackList[1], state=trackList[0],
                    large_image='icon', large_text='Last.fm')

        printProgressBar(0, float(time_remaining) + start_time, prefix = 'Progress:', suffix = 'Complete', length = 50)
        for i in range(1, float(time_remaining) + start_time + 1):
            time.sleep(1)
            # Update Progress Bar
            printProgressBar(i + 1, float(time_remaining) + start_time, prefix = 'Progress:', suffix = 'Complete', length = 50)

def disable_rpc():
    global already_enabled
    global already_disabled
    if already_disabled == False:
        presence.clear()
        presence.close()
        print('Disconnected from Discord due to inactivity on Last.fm')
        already_disabled = True
        already_enabled = False

def disconnect():
    global already_enabled
    global already_disabled
    if already_disabled == False:
        presence.clear()
        presence.close()
        print('Disconnected from Discord')
        already_disabled = True
        already_enabled = False

