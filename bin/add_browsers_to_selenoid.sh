#!/usr/bin/env bash
# owner @i.balagurov
# the script for update selenoid configuration

# add selenoid docker image for specific browser version
docker pull selenoid/chrome:78.0
docker pull selenoid/chrome:77.0
