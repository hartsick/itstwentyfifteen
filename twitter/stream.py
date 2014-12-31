from twython import TwythonStreamer
from models.directmessage import DirectMessage
from models.follow import Follow
from rest import Tweeta

class StreamListener(TwythonStreamer):
    '''
        As event is received from stream, instantiates a new object of that type and calls the appropriate handler. Handlers must be implemented by subclass. Similar to Tweepy's StreamListener.
    '''

    def on_success(self, data):
        if data.get('direct_message'):
            dm = DirectMessage(data)
            self.on_direct_message(dm)

        elif data.get('event') and data['event'] == 'follow':
            follow = Follow(data)
            self.on_follow(follow)

        print "{0} data received:".format(self.__class__.__name__)
        print data

    def on_error(self, status_code):
        print "{0} error: {1}".format(self.__class__.__name__, status_code)


class UserStreamer(StreamListener):
    '''
        Defines event handlers for the User stream
    '''

    def on_direct_message(self, dm):
        response = dm.compose_response()
        if response:
            Tweeta().send_dm(*response)

    def on_follow(self, follow):
        Tweeta().follow_back(follow)


class PublicStreamer(StreamListener):
    '''
        Defines event handlers for the Public stream.
    '''
    pass
