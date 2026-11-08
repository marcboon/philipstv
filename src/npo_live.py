#!/usr/bin/env python3
"""
Pass TV's IP address on commandline

- Connect with the TV's Titan OS control channel (MQTT :8883)
- Launch the NPO Start app
- Navigate to 'Overslaan'
- Confirm
- Open the side bar
- Navigate to 'Live'
- Confirm
"""

import time, sys
from juno import dialogs
from philipstv.titan import Titan


def pair():
	ip = dialogs.input_alert("IP address of TV").strip()
	t = Titan(ip).connect()
	t.pair_start()
	pin = dialogs.input_alert("PIN shown on TV").strip()
	t.pair_finish(pin)
	return t


def main():
	# try to connect, pair first if needed
	t = Titan.load() or pair()
	t.connect()
	# launch NPO Start app
	app = next(a for a in t.installed_apps() if a["code"] == "npo_start")
	t.launch(app["code"], app["url"])
	# wait for app loading
	time.sleep(15)
	# navigate to 'Overslaan' and confirm
	t.key("CursorRight")
	time.sleep(0.5)
	t.key("Confirm")
	time.sleep(2)
	# open side bar
	t.key("CursorLeft")
	# navigate to 'Live' (5 items down) and confirm
	for n in range(5):
		time.sleep(0.5)
		t.key("CursorDown")
	time.sleep(0.5)
	t.key("Confirm")
	# done!
	t.close()


if __name__ == "__main__":
	main()
