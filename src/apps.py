#!/usr/bin/env python3

from philipstv.titan import Titan

t = Titan.load().connect()
apps = t.installed_apps()
t.close()
print(apps)
