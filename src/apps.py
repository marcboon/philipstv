#!/usr/bin/env python3
import sys
from pprint import pprint
from philipstv.titan import Titan

tv = Titan.discover(1)
if not tv:
	print('TV not found')
	sys.exit()

print(f"Found {tv[0]['brand']} {tv[0]['model']}")	

t = Titan.load().connect()
apps = t.installed_apps()
t.close()

pprint(apps)
