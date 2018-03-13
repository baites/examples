
from concurrent.futures import ThreadPoolExecutor
from functools import wraps
import time

def mtimeout(attribute):
    """Implement function timeout decorator."""
    def decorator(callback):
        @wraps(callback)
        def wrapper(self, *args, **kargs):
            timeout = getattr(self, attribute)
            with ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(callback, self, *args, **kargs)
                return future.result(timeout=timeout)
        return wrapper
    return decorator

class ObjectType:
    def __init__(self, timeout):
        self._timeout = timeout

    @mtimeout(attribute='_timeout')
    def sleep(self, secs):
        time.sleep(secs)

o = ObjectType(timeout=2)
o.sleep(4)
