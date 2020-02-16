#!/usr/bin/env bash
# owner @i.balagurov
# the script for installation selenoid on MacOS

echo "installation selenoid + 2 latest versions of opera / chrome / firefox"
curl -s https://aerokube.com/cm/bash | bash \
&& ./cm selenoid start --vnc
echo "should be available on http://localhost:4444/status"
echo "logs should be available on http://localhost:4444/logs"

echo "installation selenoid ui"
./cm selenoid-ui start
echo "should be available on http://localhost:8080/"
echo "videos should be available on http://localhost:8080/#/videos"
