# Last.fm Discord Rich Presence
### Description
🎵 Show your Last.fm listening status on Discord!

**Preview:**

![Image](https://cdn.discordapp.com/attachments/967489166680133762/982434451642544149/CleanShot_2022-06-03_at_20.03.332x.png)

## Dependencies
- pypresence
- pylast
- pystray

## Setup

### Windows, MacOS or Linux (Using Python)
- Download and install Python (during the instalation, check the option to add Python to the PATH if applicable).
- Download the [source code](https://github.com/itsnebulalol/last.fm-discord/archive/master.zip).
- Edit the username key in the config.json file:
```json
{
    "username": "your last.fm username here"
}
```
- Open a terminal and install dependencies by typing the following command:

`pip install -r requirements.txt`
- Run the .py file at the same terminal using:

`python main.py`