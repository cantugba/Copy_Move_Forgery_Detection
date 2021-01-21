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
    match = None
    draw = None
    def __init__(self,image):
        self.image = image
        self.match = MatchFeatures(self.key_points, self.descriptors, self.distance)  # match points
        self.draw = DrawRectangle(self.image, self.match.gPoint1, self.match.gPoint2, self.color, self.match.cRectangle)  # draw matches
        # draw = DrawLine(self.image,  match.gPoint1,  match.gPoint2,self.color)
        self.image = self.draw.image

    # detect keypoints and descriptors
    @abstractmethod
    def detectFeature(self):
        pass