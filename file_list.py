#!/usr/bin/env python

import os

from pyicloud import PyiCloudService

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

# list available files
print api.files.dir()
