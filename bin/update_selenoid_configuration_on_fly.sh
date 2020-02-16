#!/usr/bin/env bash
# owner @i.balagurov
# the script for update selenoid configuration

# send signal to selenoid for updating configuration without reloading server
# (will be used configuration in elenoid default folder)
docker kill -s HUP selenoid
