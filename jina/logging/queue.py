import atexit
import multiprocessing

__sse_queue__ = multiprocessing.Queue()  #: the global sse log queue
__profile_queue__ = multiprocessing.Queue()  #: the global profile log queue
__log_queue__ = multiprocessing.Queue()  #: the global log queue

def clear_queue():
    """Clear the log queue and profile queue when the program exit

    This is only used when server-side event (SSE) logging is turned on.
    """
    from . import default_logger
    default_logger.info('releasing the log queue')
    while not __sse_queue__.empty():
        __sse_queue__.get_nowait()

    while not __profile_queue__.empty():
        __profile_queue__.get_nowait()


atexit.register(clear_queue)  #: clear the log queue when exit
