#!/usr/bin/env bash
# owner @i.balagurov
# the script for install ggr

mkdir ./grid-router/quota
htpasswd -bc ./grid-router/users.htpasswd test test-password

# binary version
./ggr_darwin_amd64 -quotaDir grid-router/quota/ -users grid-router/users.htpasswd  -listen :4445

# docker version
# docker pull aerokube/ggr:latest-release

#docker run -d --name \
#    ggr -v /grid-router/:/grid-router:ro \
#    --net host aerokube/ggr:latest-release

echo "should be available on http://localhost:4445/ping"
