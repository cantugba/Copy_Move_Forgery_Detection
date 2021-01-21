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
        match = MatchFeatures(self.key_points, self.descriptors, self.distance)  # match points
        draw = DrawRectangle(self.image, match.gPoint1, match.gPoint2, self.color, match.cRectangle)  # draw matches
        # draw = DrawLine(self.image,  match.gPoint1,  match.gPoint2,self.color)
        self.image = draw.image

    # detect keypoints and descriptors
    @abstractmethod
    def detectFeature(self):
        pass