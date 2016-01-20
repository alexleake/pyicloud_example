#!/usr/bin/env python

import os

from pyicloud import PyiCloudService
from geopy.geocoders import Nominatim

# example of credentials file
example_credentials = "APPLE_ID='foo@bar.com'\nAPPLE_PASSWORD=1234"

# check for the credentials file
if os.path.isfile('./credentials.py'):
    from credentials import APPLE_ID, APPLE_PASSWORD
else:
    print "credentials.py file missing, please create one. ie:\n{cred}".format(cred=example_credentials)
    raise SystemExit

# log into the api
api = PyiCloudService(APPLE_ID, APPLE_PASSWORD)

# takes the first device by default
device = api.devices
device_gps = api.iphone.location()

# we need coordinates to match the spec for geopy https://pypi.python.org/pypi/geopy
coordinates = ("{lat}, {long}").format(long=device_gps['longitude'], lat=device_gps['latitude'])

# see their doc https://pypi.python.org/pypi/geopy - this does a reverse lookup on lat / long
geolocator = Nominatim()
location = geolocator.reverse(coordinates)

# print address
print(location.address)
