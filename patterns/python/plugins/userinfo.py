"""Implement a user information plugin."""

from plugin import Plugin

class UserInfo(Plugin):
    def __init__(self, srvuser, srvpasswd):
        """Class constructor."""
        super().__init__()
        self._srvuser = srvuser
        self._srvpasswd = srvpasswd

    def run(self):
        return {
            'jfaker': {
                'fake_name': 'John Faker',
                'fake_office': 'SW-E123A'
            }
        }

def create(**config):
    """Create plugin."""
    return UserInfo(**config)
