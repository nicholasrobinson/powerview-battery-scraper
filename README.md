# PowerView Battery Scraper

## Motivation

My Hunter Douglas Powerview blinds occasionally report "timedOut" with "batteryStatus": 0. This script iterates through all blinds reporting this condition until it is resolved.

## Example configuration.yaml

```
shell_command:
  refresh_powerview_battery_status: "/config/scripts/powerview_battery_scraper.py"
```

## Example automations.yaml

```
- id: '1649633031590'
  alias: Refresh PowerView Battery Status
  description: ''
  trigger:
  - platform: time_pattern
    minutes: '0'
  condition: []
  action:
  - service: shell_command.refresh_powerview_battery_status
  mode: single
```