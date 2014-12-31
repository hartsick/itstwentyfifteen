from streamlistener import StreamListener
from rest import Tweeta

class UserStreamer(StreamListener):
    '''
        Defines event handlers for the User stream
    '''

    def on_direct_message(self, dm):
        text = dm.text_without_mentions()
        if text:
            Tweeta().update_status(text)

    def on_follow(self, follow):
        Tweeta().follow_back(follow)


class PublicStreamer(StreamListener):
    '''
        Defines event handlers for the Public stream.
    '''
    pass
