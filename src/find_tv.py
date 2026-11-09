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
		print(f"TV found at {tv['ip']}: {tv['brand']} {tv['model']}")
else:
	print("No TVs found")
	