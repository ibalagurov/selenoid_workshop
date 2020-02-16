#!/usr/bin/env bash
# owner @i.balagurov
# the script for selenoid s3 untegration
# insatructions https://aerokube.com/selenoid/latest/#_uploading_files_to_s3

secret_key=""
access_key=""

./selenoid -s3-endpoint https://fra1.digitaloceanspaces.com/ \
-s3-region fra-1 \
-s3-bucket-name selenoid-workshop \
-s3-access-key ${access_key} \
-s3-secret-key ${secret_key} \
-conf ~/.aerokube/selenoid/browsers.json -limit 6

echo "should be available on http://localhost:4444/status"
