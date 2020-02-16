#!/usr/bin/env bash
# owner @i.balagurov
# the script for install ggr

mkdir ./grid-router/quota
htpasswd -bc ./grid-router/users.htpasswd test test-password

# binary version
./ggr-ui_darwin_amd64 -quota-dir grid-router/quota/

echo "should be available on http://localhost:8888/status"
