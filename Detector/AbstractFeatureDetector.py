from abc import ABCMeta, abstractmethod

class AbstractDetector(metaclass=ABCMeta):

    @abstractmethod
    def detectFeature(self):
        pass

    @abstractmethod
    def detector(self):
        pass
