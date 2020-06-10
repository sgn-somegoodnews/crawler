import tweepy

_secrets = None

def read_credentials():
  f = open("secrets/twitter-api", "r")
  lines = f.read().split('\n')
  response = dict()
  for line in lines:
    if (len(line.strip()) == 0):
      continue
    cols = line.split('=')
    response[cols[0].strip()] = cols[1].strip()
  return response

def find_tweets(query, count):
  global _secrets
  if (_secrets == None):
    _secrets = read_credentials()
  consumer_key = _secrets['api_key']
  consumer_secret = _secrets['api_key_secret']
  access_token = _secrets['access_token']
  access_token_secret = _secrets['access_token_secret']

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth,wait_on_rate_limit=True)

  tweets = []
  for tweet in api.search(q=query, count=count):
    tweets.append((tweet.created_at, tweet.id, tweet.text))
  return tweets

a = find_tweets('#sgn', 10)
print(a[0])