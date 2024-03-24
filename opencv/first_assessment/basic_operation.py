import cv2 as cv


image = cv.imread(r"E:\ro\basic.png")

# 获取形态学的卷积核..cv2.MORPH_RECT（矩形）、cv2.MORPH_ELLIPSE（椭圆）或cv2.MORPH_CROSS（十字形）
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (10, 10))
# 腐蚀
dst = cv.erode(image, kernel, iterations=2)
# 膨胀
dilate = cv.dilate(image, kernel, iterations=2)
# 开运算
open_ = cv.morphologyEx(image, cv.MORPH_OPEN, kernel)
# 闭运算
close_ = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
cv.imshow('sds', cv.hconcat([open_, close_]))
cv.waitKey(0)
cv.destroyAllWindows()