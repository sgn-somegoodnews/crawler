# crawler

Crawler code to find news for the SGN app in Python 3.7/GAE.

This will fetch APIs/crawl webpages under a cron to populate our Firebase Firestore database with some good news for the apps to consume.

# Setup

In order to setup, install python 3.7 and run

```bash
# setup virtual env
python3 -m venv env
source env/bin/activate

# install requirements
pip install  -r requirements.txt
```

To run locally, run

```bash
python lib/main.py
```

To deploy to the App Engine server, first download the service-accounts.json secret file from Firebase and put on the following path:

```bash
secrets/sgn-test-firestore-access.json
```

```bash
gcloud app deploy
```

After properly configuring your gcloud CLI.

