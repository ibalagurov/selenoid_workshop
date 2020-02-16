#!/usr/bin/env bash
# owner @i.balagurov
# the script for installation selenoid on MacOS

curl -s https://aerokube.com/cm/bash | bash \
&& ./cm selenoid start --vnc
