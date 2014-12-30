from twitteruser import TwitterUser

class DirectMessage(TwitterObject):
    self.text = self.json['text']
    self.event_type = 'direct_message'

    def id(self):
        pass

    def origin_account(self):
        pass

    def target_account(self):
        pass

    def target(self):
        pass

    def made_by_self(self):
        pass

    def in_reply_to(self):
        pass

    def sender(self):
        sender_hash = self.json['sender']
        sender = TwitterUser(sender_hash)

        return sender

    def recipient(self):
        recipient_hash = self.json['recipient']
        recipient = TwitterUser(recipient_hash)

        return recipient

    def entities(self):
        pass
