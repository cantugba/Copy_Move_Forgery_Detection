from Detector.AbstractDetector import AbstractDetector
import cv2
from Detector.MatchFeature.Match import Match_Features
from DrawFunctions.Rectangle import DrawRectangle
from DrawFunctions.Line import DrawLine
from Detector.Detector import AbsDetector

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
        detector = AbsDetector(self.image,self.key_points,self.descriptors,self.distance,self.color)
        self.image = detector.image

