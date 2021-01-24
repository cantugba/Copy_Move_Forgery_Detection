import cv2

from DrawFunctions.AbstractShape import AbstractShape


class DrawLine(AbstractShape):
    image = None
    key_points1 = None
    key_points2 = None
    color = None

    def __init__(self, image, keypoints1, keypoints2, color):
        self.image = image
        self.key_points1 = keypoints1
        self.key_points2 = keypoints2
        self.color = color
        self.draw()

    def draw(self, **kwargs):
        forgery = self.image.copy()
        for keypoint1, keypoint2 in zip(self.key_points1, self.key_points2):
            if len(self.key_points1) > 1:
                cv2.line(forgery, (int(keypoint1[0]), int(keypoint1[1])), (int(keypoint2[0]), int(keypoint2[1])), self.color, 1)

        self.image = forgery
