#!/usr/bin/env bash
# owner @i.balagurov
# the script for update selenoid configuration

# setting simaltenious max browsers sessions and specifing configuration file
./cm selenoid update --args "-limit 6" --browsers-json browsers.json
