from streamlistener import StreamListener
from rest import Tweeta

class UserStreamer(StreamListener):
    '''
        Defines event handlers for the User stream
    '''

    def on_direct_message(self, dm):
        # check for "help"
            # respond with directions
        pass

    def on_follow(self, follow):
        Tweeta().follow_back(follow)

    def on_reply(self, status):
        if status.sender_not_self() and status.is_reply_to_bot():
            text = status.stripped_text()

            if 'in 2015' or 'i fucking did it' in text:
                Tweeta().retweet(status)

            # respond appropriately
            Tweeta().reply_to_status(status)

class PublicStreamer(StreamListener):
    '''
        Defines event handlers for the Public stream.
    '''
    pass
