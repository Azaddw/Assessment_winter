import cv2 as cv
import numpy as np

image = cv.imread(r"E:\ro\gama.png")
img = cv.imread(r"E:\ro\gama.jpg")
def gama_adjust(image, gama=1.0):
    invgama = 1/gama
    adjusted_map = np.array(np.power(image/255, invgama)*255, dtype=np.uint8)
    return adjusted_map

image_gama = gama_adjust(image, gama=3.0)
img_gama = gama_adjust(img, gama=2.0)
cv.imshow("ww", cv.hconcat([image_gama, image]))
cv.imshow("www", cv.hconcat([img, img_gama]))
cv.waitKey(0)
cv.destroyAllWindows()