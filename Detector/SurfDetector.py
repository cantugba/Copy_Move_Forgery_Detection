from Detector.AbstractDetector import AbstractDetector
import cv2
from Detector.MatchFeature.Match import Match_Feature
from DrawFunctions.Rectangle import DrawRectangle


class SurfDetector(AbstractDetector):
    # Green
    image = None
    key_points = None
    descriptors = None
    color = (0, 255, 0)

    def __init__(self, image):
        self.image = image
        self.detectFeature()
        self.detector()

    def detectFeature(self):
        sift = cv2.SURF_create() #burayı surf create yap
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.key_points, self.descriptors = sift.detectAndCompute(gray, None)

    def detector(self):
        points1, points2,cRectangle = Match_Feature(self.key_points,self.descriptors)
        draw = DrawRectangle(self.image, points1, points2, self.color, cRectangle)
        #draw = DrawLine(self.image,keypoints1 = points1, keypoints2 = points2,color=self.color)
        self.image = draw.image
