from twython import TwythonStreamer

class UserStreamer(TwythonStreamer):
    def __init__(self, *args, **kwargs):
        TwythonStreamer.__init__(self, *args, **kwargs)

    def on_success(self, data):
        # accept submissions via direct message
        if data.get('direct_message'):
            # instantiate new direct message
            # pass dm to handler
            pass

        # listen for follows & follow back
        elif data.get('event') and data['event'] == 'follow':
            # instantiate follow event
            # pass event to handler
            pass

        print "UserStream data received:"
        print data

    def on_error(self, status_code, data):
        print "UserStream error: {0}".format(status_code)


class PublicStreamer(TwythonStreamer):
    def __init__(self, *args, **kwargs):
        TwythonStreamer.__init__(self, *args, **kwargs)

    def on_success(self, data):
        print "PublicStream data received:"
        print data

    def on_error(self, status_code, data):
        print "PublicStream error: {0}".format(status_code)
