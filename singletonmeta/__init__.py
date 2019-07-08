from threading import Lock


__version__ = '1.0'


class ThreadSafeSingletonMeta(type):

    __instances = {}
    __lock = Lock()

    def __call__(cls, *args, **kwargs):
        with ThreadSafeSingletonMeta.__lock:
            if cls not in cls.__instances:
                cls.__instances[cls] = super(ThreadSafeSingletonMeta, cls).__call__(*args, **kwargs)
            return cls.__instances[cls]


class SingletonMeta(type):

    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]
