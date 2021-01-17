import cv2
from scipy.spatial.distance import pdist
import numpy as np
from .Ransac import Ransac

class Match_Features():

    descriptors = None
    keypoints = None
    distances = None
    gPoint1 = None
    gPoint2 = None
    cRectangle = None


    def __init__(self,keypoints,descriptors,distances):
        self.keypoints = keypoints
        self.descriptors = descriptors
        self.distances = distances
        self.Match()

    def Match(self):
        bf = cv2.BFMatcher(self.distances)
        matches = bf.knnMatch(self.descriptors,self.descriptors,k = 10)
        ratio = 0.5
        mkp1, mkp2 = [], []

        for m in matches:
            j = 1

            while (m[j].distance < ratio * m[j + 1].distance):
                j = j + 1

            for k in range(1, j):
                temp = m[k]

                if pdist(np.array([self.keypoints[temp.queryIdx].pt,
                                   self.keypoints[temp.trainIdx].pt])) > 10:
                    mkp1.append(self.keypoints[temp.queryIdx])
                    mkp2.append(self.keypoints[temp.trainIdx])

        # ransaclı
        self.gPoint1, self.gPoint2, self.cRectangle = Ransac(mkp1, mkp2)
