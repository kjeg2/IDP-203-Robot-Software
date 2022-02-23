# You should replace these 3 lines with the output in calibration step
import numpy as np
import cv2
import sys
import imutils

DIM=(1806, 1440)
K=np.array([[991.3067219749147, 0.0, 952.3468881786204], [0.0, 987.6168623207227, 807.627165812705], [0.0, 0.0, 1.0]])
D=np.array([[0.11129621201819383], [-2.5030370340096795], [11.712262842325035], [-16.614535465983327]])
def undistort(img_path):
    img = cv2.imread(img_path)
    img = imutils.resize(img, width=600)
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    cv2.imshow("undistorted", undistorted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    for p in sys.argv[1:]:
        undistort(p)

undistort('1.jpg')