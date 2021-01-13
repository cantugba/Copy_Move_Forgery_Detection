from scipy.spatial.distance import pdist
import cv2
import numpy as np
from .Ransac import Ransac


def Match_Feature(keypoints,descriptors):

        bf = cv2.BFMatcher(cv2.NORM_L2)
        matches = bf.knnMatch(descriptors,descriptors,k = 10)

        ratio = 0.7
        mkp1,mkp2 = [], []

        for m in matches:
            j = 1
            while(m[j].distance < ratio * m[j + 1].distance):
                j = j + 1

            for k in range(1, j):
                temp = m[k]

                if pdist(np.array([keypoints[temp.queryIdx].pt,
                                   keypoints[temp.trainIdx].pt])) > 10:
                    mkp1.append(keypoints[temp.queryIdx])
                    mkp2.append(keypoints[temp.trainIdx])

        # p1 = np.float32([kp1.pt for kp1 in mkp1])
        #
        # p2 = np.float32([kp2.pt for kp2 in mkp2])
        # return p1,p2
        # ransaclı
        gp1, gp2, rec = Ransac(mkp1, mkp2)
        return gp1, gp2,rec

