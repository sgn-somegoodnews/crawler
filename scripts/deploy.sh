#!/bin/bash -xe

gcloud app deploy
gcloud app deploy cron.yaml
