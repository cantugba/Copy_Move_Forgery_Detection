from DrawFunctions.AbstractShape import AbstractShape
import cv2


class DrawLine(AbstractShape):
    image = None
    keypoints1 = None
    keypoints2 = None
    color = None

    def __init__(self, image, keypoints1, keypoints2, color):
        self.image = image
        self.keypoints1 = keypoints1
        self.keypoints2 = keypoints2
        self.color = color
        self.draw()

    def draw(self):
        forgery = self.image.copy()
        for keypoint1, keypoint2 in zip(self.keypoints1, self.keypoints2):
            if len(self.keypoints1) > 1:
                cv2.line(forgery, (int(keypoint1[0]), int(keypoint1[1])), (int(keypoint2[0]), int(keypoint2[1])), self.color, 1)

        self.image = forgery