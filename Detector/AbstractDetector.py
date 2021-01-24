from abc import ABCMeta, abstractmethod
from DrawFunctions.Line import DrawLine
from DrawFunctions.Rectangle import DrawRectangle
from Detector.MatchFeature.Match import MatchFeatures

class AbstractDetector(metaclass=ABCMeta):
    key_points = None
    descriptors = None
    color = None
    image = None
    distance = None
    MatchFeatures = None
    Draw = None
    def __init__(self, image):
        self.image = image
        self.MatchFeatures = MatchFeatures(self.key_points, self.descriptors, self.distance)  # match points
        self.Draw = DrawRectangle(self.image, self.MatchFeatures.gPoint1, self.MatchFeatures.gPoint2, self.color, self.MatchFeatures.cRectangle)  # draw matches
        #self.Draw = DrawLine(self.image,  self.MatchFeatures.gPoint1,  self.MatchFeatures.gPoint2, self.color)
        self.image = self.Draw.image

    # detect keypoints and descriptors
    @abstractmethod
    def detectFeature(self):
        pass