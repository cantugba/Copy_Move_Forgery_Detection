from Detector.AbstractFeatureDetector import AbstractDetector
import cv2
from Detector.MatchFeature.Match import Match_Features
from DrawFunctions.Rectangle import DrawRectangle
from DrawFunctions.Line import DrawLine

class AbsDetector:
    key_points = None
    descriptors = None
    color = None
    image = None
    distance = None

    def __init__(self, image, key_points, descriptors, distance, color):
        self.image = image
        self.key_points = key_points
        self.descriptors = descriptors
        self.distance = distance
        self.color = color
        self.detector()

    def detector(self):
        match = Match_Features(self.key_points,self.descriptors,self.distance)
        draw = DrawRectangle(self.image, match.gPoint1, match.gPoint2, self.color, match.cRectangle)
        #draw = DrawLine(self.image,keypoints1 = points1, keypoints2 = points2,color=self.color)
        self.image = draw.image