
from concurrent.futures import ThreadPoolExecutor
from functools import wraps
import time

def ftimeout(timeout):
    """Implement function timeout decorator."""
    def decorator(callback):
        @wraps(callback)
        def wrapper(*args, **kargs):
            with ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(callback, *args, **kargs)
                return future.result(timeout=timeout)
        return wrapper
    return decorator

@ftimeout(timeout=2)
def sleep(secs):
    time.sleep(secs)

sleep(secs=4)
