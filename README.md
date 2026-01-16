# VC Relay Bot (Advanced)

Private VC relay (bridge) bot.
Control group VC → Target group VC with volume control.

## Commands (Control Group)
/connect <target_group_id>
/volume <0-300>
/stop

## Requirements
- Python 3.9+
- ffmpeg
- User account (Pyrogram session)

## Run
sudo apt install ffmpeg -y
pip install -r requirements.txt
python main.py
