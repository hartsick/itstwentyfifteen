from twython import Twython
from config.common import twitter_cred

class Tweeta(object):
    def __init__(self):
        self.twitter = Twython(*twitter_cred)

    def update_status(self, text):
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

    def retweet(self, status):
        if status.sender_not_self():
            print "Retweeting: {0}".format(status.id_str)
            params = {'id': status.id_str}
            self.twitter.retweet(**params)

    def reply_to_status(self, status):
        print "reply received"
        if status.sender_not_self():
            status_type = status.check_type()
            print status_type
            if status_type:
                text = ""
                if status_type is 'resolution':
                    text = "let's do this. we believe in you!!"
                elif status_type is 'help':
                    text = "send me your new years resolution in the format 'in 2015, I' and I'll retweet it for all to see! we're in this together."
                elif status_type is 'complete':
                    text = "GOOD JOB!! :D"

                response = "@{0} {1}".format(status.sender().username, text)

                params = {'status': response, 'in_reply_to_status_id': status.id}
                print "Responding with: {0}".format(response)
                self.twitter.update_status(**params)
