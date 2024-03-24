import cv2

image = cv2.imread(r"C:\Users\Xuxinyang\Pictures\bizhi\facy.png")

img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

img_hsv[0] = img_hsv[0] + 20
img_hsv[1] = img_hsv[1] - 20

cv2.imshow("compare", cv2.hconcat([img_hsv, image]))
cv2.waitKey(0)
cv2.destroyAllWindows()