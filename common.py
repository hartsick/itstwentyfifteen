import os

twitter_cred = {
  'consumer_key':          os.environ.get('MASTER_BOT_CONSUMER_KEY'),
  'consumer_secret':       os.environ.get('MASTER_BOT_CONSUMER_SECRET'),
  'access_token':          os.environ.get('NEWYEARS_ACCESS_TOKEN'),
  'access_token_secret':   os.environ.get('NEWYEARS_ACCESS_TOKEN_SECRET')
}
