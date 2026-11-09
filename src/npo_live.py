#!/usr/bin/env python3
"""
- If not paired already, find TV on local network and pair it
- Connect with the TV's Titan OS control channel (MQTT :8883)
- Launch the NPO Start app
- Navigate to 'Overslaan'
- Confirm
- Open the side bar
- Navigate to 'Live'
- Confirm
"""
import time, sys
from philipstv.titan import Titan

# Set flag if running in Juno on iPhone, to use dialogs for interactive input
try:
	import juno.dialogs
	iPHONE = True
except ImportError:
	iPHONE = False

# Pre-paired user for testing
USER = "300078d2-c11d-4b36-ae20-43554e0189c0"


def alert(title):
	try:
		from juno import dialogs
		return dialogs.alert(title)

	except ImportError:
		return print(title)

def prompt(title):
	try:
		from juno import dialogs
		return dialogs.input_alert(title)

	except ImportError:
		return input(title)

def pair():
	tvs = Titan.discover()
	if tvs:
		ip = tvs[0]['ip']
		if ip is None:
			alert("No TV found")
			sys.exit()

	else:
		alert("No TV found")
		sys.exit()

	t = Titan(ip).connect()
	t.pair_start()
	pin = prompt("PIN shown on TV: ").strip()
	t.pair_finish(pin, USER)
	return t


def main():
	# try to connect, pair first if needed
	t = Titan.load(False) or pair()
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
