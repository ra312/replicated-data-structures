import abc

class AbstractTree(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def entry(self): return

    @abc.abstractmethod
    def left(self): return

    @abc.abstractmethod
    def right(self): return