from twitteruser import TwitterUser
from twitterobject import TwitterObject

class DirectMessage(TwitterObject):
    '''
        Class for a received Direct Message from the Twitter API.
        Provides easy access to commonly used attributes.
    '''
    def __init__(self, data):
        super(DirectMessage, self).__init__(data)

        # remove root if exists
        if data.get('direct_message'):
            self.data = data['direct_message']

        self.id = self.data['id']
        self.text = self.data['text']
        self.mentions = self.data['entities']['user_mentions']

    def sender_not_self(self):
        '''Boolean, Returns true if sender of DM is not the app's Twitter bot'''
        sender = self.sender()

        return sender.is_not_bot()

    def sender(self):
        '''Returns a TwitterUser object for the DM's sender'''
        sender_hash = self.data['sender']
        sender = TwitterUser(sender_hash)

        return sender

    def recipient(self):
        '''Returns a TwitterUser object for the DM's receipient'''
        recipient_hash = self.data['recipient']
        recipient = TwitterUser(recipient_hash)

        return recipient

    def text_without_mentions(self):
        '''Returns a string copy of the original DM text with any usernames redacted'''
        edited_text = self.text
        for user in self.mentions:
            print user
            display_name = user
            edited_text.replace("@{0}".format(display_name), "[...]")

        return edited_text

    def compose_response(self):
        '''Generate a response to this DM'''
        response = None
        # don't respond to yourself
        if self.sender_not_self():
            response_text = self.text_without_mentions()
            respond_to_user = self.sender()
            response = [response_text, respond_to_user]

        return response
