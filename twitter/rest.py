from twython import Twython
from config.common import twitter_cred

class Tweeta(object):
    def __init__(self):
        self.twitter = Twython(*twitter_cred)

    def update_status(self, text):
        # TODO: Include reply_id to thread conversations
        params = {'status': text}
        self.twitter.update_status(**params)

    def send_dm(self, text, user):
        params = {'text': text, 'user_id': user.id, 'screen_name': user.username}
        self.twitter.send_direct_message(**params)

    def follow_back(self, follow):
        if follow.sender_not_self():
            user = follow.sender()
            params = {'user_id': user.id, 'screen_name': user.username}
            self.twitter.create_friendship(**params)
