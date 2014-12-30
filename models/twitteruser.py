# Accepts User hash and extracts useful info
# for easy use
class TwitterUser(object):
    def __init__(data):
        self.data = data

    self.username = self.data['screen_name']

    self.display_name = self.data['name']

    self.id = self.data['id']


# TODO: pull this info from the bot itself
#       for now, manually set.
bot_info = {
    'screen_name': 'intwentyfifteen',
    'name': 'Best Intention',
    'id': 2921127146
}

BOT_USER = TwitterUser(bot_info)
