import cv2 as cv
import numpy as np

img = cv.imread(r"E:\ro\gama.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
thread = 70

# 方法1
img[img > thread] = 255
img[img <= thread] = 0

# 方法2
# w, h = img.shape
# for i in range(w):
#     for j in range(h):
#         if img[i][j] > thread:
#             img[i][j] = 255
#         else:
#             img[i][j] = 0


cv.imshow("aa", img)
cv.waitKey(0)
cv.destroyAllWindows()
