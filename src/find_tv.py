#!/usr/bin/env python3
"""
Find TitanOS TV's on the local network
"""
from philipstv.titan import Titan

# Scan local network for Philips/TitanOS TVs
tvs = Titan.discover()
if tvs:
	for tv in tvs:
		# Show info
		print(f"{tv['brand']} {tv['model']} at {tv['ip']}")
else:
	print("No TVs found")
	