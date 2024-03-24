import cv2 as cv
import numpy as np

dawn = cv.imread(r"E:\ro\niddle.png")
dawn1 = cv.resize(dawn, (640, 480))
dawn2 = cv.Canny(dawn1, 10, 500)
cv.imshow('da', dawn2)
cv.waitKey(0)
cv.destroyAllWindows()