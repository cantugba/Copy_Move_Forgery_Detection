from DrawFunctions.AbstractShape import AbstractShape
import cv2
from PIL import Image, ImageDraw
import numpy as np

class DrawRectangle(AbstractShape):

    image = None
    keypoints1 = None
    keypoints2 = None
    color = None
    cRectangle = None
    def __init__(self, image, keypoints1, keypoints2, color,cRectangle):
        self.image = image
        self.keypoints1 = keypoints1
        self.keypoints2 = keypoints2
        self.color = color
        self.cRectangle = cRectangle # counts of rectangle
        self.draw()


    def draw(self):
        newimage = self.image.copy()

        if (self.cRectangle == 0):
            k1x, k2x = np.max(self.keypoints1, axis=0), np.max(self.keypoints2, axis=0)
            k1n, k2n = np.min(self.keypoints1, axis=0), np.min(self.keypoints2, axis=0)
            cv2.rectangle(newimage, (int(k2x[0]) + 10, int(k2n[1]) - 10), (int(k2n[0]) - 10, int(k2x[1]) + 10), self.color, 3)
            cv2.rectangle(newimage, (int(k1x[0]) + 10, int(k1n[1]) - 10), (int(k1n[0]) - 10, int(k1x[1]) + 10), self.color, 3)
            self.image = newimage
        elif (self.cRectangle == 3):
            list, z = np.zeros(len(self.keypoints1)), 0
            z2, z3, z4 = np.array([[0, 0]]), np.array([[0, 0]]), np.array([[0, 0]])
            for k1, k2 in zip(self.keypoints1, self.keypoints2):
                if len(self.keypoints1) > 1:
                    p = (k1[0] - k2[0]) / (k1[1] - k2[1])
                    list[z] = int(p)
                    z = z + 1
            for k1, k2 in zip(self.keypoints1, self.keypoints2):
                if len(self.keypoints1) > 1:
                    p = (k1[0] - k2[0]) / (k1[1] - k2[1])
                    p = int(p)
                    if p == max(list):
                        newrow = [k1[0], k1[1]]
                        z2 = np.vstack([z2, newrow])
                    elif p < 0:
                        newrow = [k1[0], k1[1]]
                        z3 = np.vstack([z3, newrow])
                        newrow = [k2[0], k2[1]]
                        z4 = np.vstack([z4, newrow])

            k1x, k11x, k2x = np.max(z3, axis=0), np.max(z2, axis=0), np.max(z4, axis=0)
            z2[0], z3[0], z4[0] = k11x, k1x, k2x
            k11n, k1n, k2n = np.min(z2, axis=0), np.min(z3, axis=0), np.min(z4, axis=0)

            cv2.rectangle(newimage, (int(k2x[0]) + 10, int(k2n[1]) - 10), (int(k2n[0]) - 10, int(k2x[1]) + 10), self.color, 3)
            cv2.rectangle(newimage, (int(k11x[0]) + 10, int(k11n[1]) - 10), (int(k11n[0]) - 10, int(k11x[1]) + 10), self.color, 3)
            cv2.rectangle(newimage, (int(k1x[0]) + 10, int(k1n[1]) - 10), (int(k1n[0]) - 10, int(k1x[1]) + 10), self.color, 3)
        self.image = newimage
