import cv2
from math import sqrt
import numpy as np



def Ransac(mkp1, mkp2):
    p1 = np.float32([kp1.pt for kp1 in mkp1])
    p2 = np.float32([kp2.pt for kp2 in mkp2])

    homography, status = cv2.findHomography(p1, p2, cv2.RANSAC, 5.0)

    inliers1 = []
    inliers2 = []
    count, rec = 0, 0
    inliers_thresold = 2.5  # Eşitlik kontrolü ile değişkenleri belirlemek için mesafe eşiği

    # Birinci anahtar noktanın projeksiyonundan ikinci kilit noktaya olan mesafe eşikten azsa, homografi modeline uyar.
    # inliers için yeni bir eşleşme veriseti oluşturulur eşleşmeleri çizdirmek için gerekli

    good_matches = []
    for i, m in enumerate(mkp1):

        col = np.ones((3, 1), dtype=np.float64)
        col[0:2, 0] = m.pt
        col = np.dot(homography, col)
        col /= col[2, 0]

        distance = sqrt(pow(col[0, 0] - mkp2[i].pt[0], 2) + \
                        pow(col[1, 0] - mkp2[i].pt[1], 2))

        if distance < inliers_thresold:
            count = count + 1

    if count * 2.5 < len(mkp1):
        inliers_thresold = 339
        rec = 3

    for i, m in enumerate(mkp1):

        col = np.ones((3, 1), dtype=np.float64)
        col[0:2, 0] = m.pt
        col = np.dot(homography, col)
        col /= col[2, 0]

        distance = sqrt(pow(col[0, 0] - mkp2[i].pt[0], 2) + \
                        pow(col[1, 0] - mkp2[i].pt[1], 2))

        if distance < inliers_thresold:
            good_matches.append(cv2.DMatch(len(inliers1), len(inliers2), 0))
            inliers1.append(mkp1[i])
            inliers2.append(mkp2[i])

    print('# eslesme:                            \t', len(mkp1))
    print('# Inliers yani verilen homografiye uyan eşleşmeler:                            \t', len(inliers1))

    gPoints1 = np.float32([kp1.pt for kp1 in inliers1])
    gPoints2 = np.float32([kp2.pt for kp2 in inliers2])

    return gPoints1, gPoints2, rec
