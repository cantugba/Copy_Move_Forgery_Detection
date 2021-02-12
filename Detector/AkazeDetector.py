import cv2

from Detector.AbstractDetector import AbstractDetector


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
        super().__init__(self.image)

    # detect keypoints and descriptors
    def detectFeature(self):
        sift = cv2.AKAZE_create()
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.key_points, self.descriptors = sift.detectAndCompute(gray, None)
        print("akaze",len(self.descriptors[1]))
