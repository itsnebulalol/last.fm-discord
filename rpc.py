from pypresence import Presence
import datetime
import time

client_id = '982286050858795008'
presence = Presence(client_id)
already_enabled = False
already_disabled = True
start_time = None
last_track = None

def enable_rpc():
    global already_enabled,already_disabled
    if already_enabled == False:
        presence.connect()
        print('Connected with Discord')
        already_enabled = True
        already_disabled = False


def update_status(track, album, time_remaining, url):
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
                if url != 'None':
                    presence.update(details=trackList[1], state=album, end=float(time_remaining) + start_time,
                        large_image='icon', large_text='Now Playing powered by last.fm', 
                        buttons=[{"label": "Go to Song", "url": url}, {"label": "Nebula's Discord", "url": "https://discord.com/invite/XpYSa9NztA"}])
                else:
                    presence.update(details=trackList[1], state=album, end=float(time_remaining) + start_time,
                        large_image='icon', large_text='Now Playing powered by last.fm', 
                        buttons=[{"label": "Nebula's Discord", "url": "https://discord.com/invite/XpYSa9NztA"}])
            else:
                if url != 'None':
                    presence.update(details=trackList[1], state=trackList[0], end=float(time_remaining) + start_time,
                        large_image='icon', large_text='Now Playing powered by last.fm', 
                        buttons=[{"label": "Go to Song", "url": url}, {"label": "Nebula's Discord", "url": "https://discord.com/invite/XpYSa9NztA"}])
                else:
                    presence.update(details=trackList[1], state=trackList[0], end=float(time_remaining) + start_time,
                        large_image='icon', large_text='Now Playing powered by last.fm', 
                        buttons=[{"label": "Nebula's Discord", "url": "https://discord.com/invite/XpYSa9NztA"}])
        else:
            if album != 'None':
                if url != 'None':
                    presence.update(details=trackList[1], state=album,
                        large_image='icon', large_text='Now Playing powered by last.fm',
                        buttons=[{"label": "Go to Song", "url": url}, {"label": "Nebula's Discord", "url": "https://discord.com/invite/XpYSa9NztA"}])
                else:
                    presence.update(details=trackList[1], state=album,
                        large_image='icon', large_text='Now Playing powered by last.fm',
                        buttons=[{"label": "Nebula's Discord", "url": "https://discord.com/invite/XpYSa9NztA"}])
            else:
                if url != 'None':
                    presence.update(details=trackList[1], state=trackList[0],
                        large_image='icon', large_text='Now Playing powered by last.fm',
                        buttons=[{"label": "Go to Song", "url": url}, {"label": "Nebula's Discord", "url": "https://discord.com/invite/XpYSa9NztA"}])
                else:
                    presence.update(details=trackList[1], state=trackList[0],
                        large_image='icon', large_text='Now Playing powered by last.fm',
                        buttons=[{"label": "Nebula's Discord", "url": "https://discord.com/invite/XpYSa9NztA"}])

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

