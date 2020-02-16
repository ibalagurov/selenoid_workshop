#!/usr/bin/env bash
# owner @i.balagurov
# the script for installation selenoid on MacOS

echo "installation selenoid + 2 versions of opera / chrome / firefox"
curl -s https://aerokube.com/cm/bash | bash \
&& ./cm selenoid start --vnc

echo "installation selenoid ui"
./cm selenoid-ui start
