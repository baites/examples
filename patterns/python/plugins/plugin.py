"""Define a plugin as python abc class."""

import abc
import logging
import time

class Plugin(abc.ABC):
    """Implement plugin abstract class."""

    def __init__(self):
        """Class constructor."""
        classname = self.__class__.__name__
        self.logger = logging.getLogger(classname)
        self.logger.info('Initializing plugin')

    def __call__(self):
        """Make it callable to wrap around loggin info."""
        self.logger.info('Running plugin ...')
        timer = time.time()
        payload = self.run()
        self.logger.info('Run in %0.2f sec.' % (time.time() - timer))
        return payload

    @abc.abstractmethod
    def run(self):
        """Run plugin."""
