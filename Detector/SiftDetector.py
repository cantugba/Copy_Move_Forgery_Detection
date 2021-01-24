import cv2

from Detector.AbstractDetector import AbstractDetector


# copy-move forgery detection with sift
class SiftDetector(AbstractDetector):
    # blue
    image = None
    key_points = None
    descriptors = None
    color = (0, 0, 255)
    distance = cv2.NORM_L2

    def __init__(self, image):
        self.image = image
        self.detectFeature()
        super().__init__(self.image)

    # detect keypoints and descriptors
    def detectFeature(self):
        sift = cv2.SIFT_create()
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.key_points, self.descriptors = sift.detectAndCompute(gray, None)
