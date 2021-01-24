import cv2
import numpy as np
from scipy.spatial.distance import pdist

from .Ransac import Ransac


class MatchFeatures:

    descriptors = None
    key_points = None
    distances = None
    gPoint1 = None
    gPoint2 = None
    cRectangle = None

    def __init__(self, key_points, descriptors, distances):
        self.key_points = key_points
        self.descriptors = descriptors
        self.distances = distances
        self.Match()

    def Match(self):
        bf = cv2.BFMatcher(self.distances)
        matches = bf.knnMatch(self.descriptors, self.descriptors, k=10)
        ratio = 0.5
        mkp1, mkp2 = [], []

        for m in matches:
            j = 1

            while m[j].distance < ratio * m[j + 1].distance:
                j = j + 1

            for k in range(1, j):
                temp = m[k]

                if pdist(np.array([self.key_points[temp.queryIdx].pt,
                                   self.key_points[temp.trainIdx].pt])) > 10:
                    mkp1.append(self.key_points[temp.queryIdx])
                    mkp2.append(self.key_points[temp.trainIdx])

        # remove the false matches
        self.gPoint1, self.gPoint2, self.cRectangle = Ransac(mkp1, mkp2)