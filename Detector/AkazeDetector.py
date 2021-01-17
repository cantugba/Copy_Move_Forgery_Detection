from Detector.AbstractDetector import AbstractDetector
import cv2
from Detector.MatchFeature.Match import Match_Features
from DrawFunctions.Rectangle import DrawRectangle
from DrawFunctions.Line import DrawLine


class AkazeDetector(AbstractDetector):
    # red
    image = None
    key_points = None
    descriptors = None
    color = (255, 0, 0)
    distance = cv2.NORM_HAMMING
    def __init__(self, image):
        self.image = image
        self.detectFeature()
        self.detector()

    def detectFeature(self):
        sift = cv2.AKAZE_create()
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.key_points, self.descriptors = sift.detectAndCompute(gray, None)

    def detector(self):
        match = Match_Features(self.key_points,self.descriptors,self.distance)
        draw = DrawRectangle(self.image, match.gPoint1, match.gPoint2, self.color, match.cRectangle)
        #draw = DrawLine(self.image,keypoints1 = points1, keypoints2 = points2,color=self.color)
        self.image = draw.image

