#!/usr/bin/env bash
# owner @i.balagurov
# the script for update selenoid configuration

# setting simaltenious max browsers sessions and specifing configuration file
docker kill -s HUP selenoid
