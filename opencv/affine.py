import cv2 as cv
import numpy as np

dawn = cv.imread(r"E:\ro\mark.jpg")
# 预操作与找到角点
dawn1 = cv.resize(dawn, (640, 480))
kernel = cv.getStructuringElement(cv.MORPH_RECT, (7, 3))
gray = cv.cvtColor(dawn1, cv.COLOR_BGR2GRAY)
maxie, er = cv.threshold(gray, 140, 255, cv.THRESH_BINARY)
dilate = cv.erode(er, kernel, iterations=4)
dst = cv.dilate(dilate, kernel, iterations=5)
corners = cv.goodFeaturesToTrack(dst, 5, 0.01, 32)
corner_coordinates = corners[:, 0, :]
pot1 = corner_coordinates[0]
pot2 = corner_coordinates[1]
pot3 = corner_coordinates[2]
pot4 = corner_coordinates[4]

src = np.float32([pot1, pot2, pot3, pot4])

dst = np.float32([[378, 420], [204, 133], [204, 420], [378, 150]])
M = cv.getPerspectiveTransform(src, dst)
img2 = cv.warpPerspective(dawn1, M, dsize=(640, 480))
x, y = 200, 120
w = 190
h = 300
cropped_image = img2[y:y+h, x:x+w]
cv.imshow("wda", cropped_image)
cv.waitKey(0)
cv.destroyAllWindows()