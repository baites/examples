"""Implement a user information plugin."""

from plugin import Plugin

class HostInfo(Plugin):
    def __init__(self, srvuser, srvpasswd):
        """Class constructor."""
        super().__init__()
        self._srvuser = srvuser
        self._srvpasswd = srvpasswd

    def run(self):
        return {
            'jfaker-desktop-sw-e123a': {
                'fake_owner': 'jfaker',
                'fake_cpu': 'Intel(R) Core(TM) i3 CPU M 330 @ 2.13GHz',
                'fake_mem': '16 MiB'
            }
        }

def create(**config):
    """Create plugin."""
    return HostInfo(**config)
