import cv2

from Detector.AbstractDetector import AbstractDetector


# copy-move forgery detection with surf
class SurfDetector(AbstractDetector):
    # Green
    image = None
    key_points = None
    descriptors = None
    color = (0, 255, 0)
    distance = cv2.NORM_L2

    def __init__(self, image):
        self.image = image
        self.detectFeature()
        super().__init__(self.image)

    # feature detect(descriptors and keypoints)
    def detectFeature(self):
        sift = cv2.SIFT_create()  # burayı surf create yap
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.key_points, self.descriptors = sift.detectAndCompute(gray, None)
