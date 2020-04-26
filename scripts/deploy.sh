#!/bin/bash -xe

if [ ! -f secrets/sgn-test-firestore-access.json ]; then
    echo "Please create file secrets/sgn-test-firestore-access.json before deploying."
    exit 1
fi

gcloud app deploy
gcloud app deploy cron.yaml
