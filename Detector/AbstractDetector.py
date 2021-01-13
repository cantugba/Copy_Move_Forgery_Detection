from abc import ABCMeta, abstractmethod

from Detector.MatchFeature.Match import Match_Feature
from DrawFunctions.Line import DrawLine
from DrawFunctions.Rectangle import DrawRectangle


class AbstractDetector(metaclass=ABCMeta):

    @abstractmethod
    def detectFeature(self):
        pass

    @abstractmethod
    def detector(self):
        pass
