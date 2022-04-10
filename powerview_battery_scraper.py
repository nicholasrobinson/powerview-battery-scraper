#!/usr/bin/env python3

import requests
import base64

POWERVIEW_API = 'http://192.168.1.16/api/shades'
UPDATE_BATTERY = {
    'updateBatteryLevel': 'true'
}

print('Querying shades...')
shades_request = requests.get(POWERVIEW_API)
shades = shades_request.json()['shadeData']
print('Shades detected:', len(shades))
shades_needing_update = [x for x in shades if x['batteryStatus'] == 0]
print('Shades needing update:', len(shades_needing_update))
for shade in shades:
    if shade['batteryStatus'] == 0:
        battery_updated = False
        attempts = 0
        while not battery_updated:
            attempts += 1
            if attempts > 1:
                print('Retry attempt #', attempts)
            else:
                print('Updating battery for shade:', base64.b64decode(shade['name']))
            battery_request = requests.get(
                POWERVIEW_API + '/' + str(shade['id']), 
                params=UPDATE_BATTERY
            )
            battery_updated = not battery_request.json()['shade']['timedOut']

