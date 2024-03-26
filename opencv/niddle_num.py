import cv2

image = cv2.imread(r"E:\ro\niddle.png")
im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary_image = cv2.threshold(im_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
binary_image_ = cv2.bitwise_not(binary_image)  # 取反很重要，连通域是白色部分的
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_image_)
print("Number of connected components:", num_labels - 1)  # 13个连通域
# stats：每一连通域的信息，表示每个连通区域的外接矩形（起始点的x、y、宽和高)和面积
# 找到符合条件的连通域
for i in range(0, num_labels):
    if 2000 < stats[i][4] < 8000:
        x = stats[i][0]
        y = stats[i][1]
        w = stats[i][2]
        h = stats[i][3]
        cv2.rectangle(image, (stats[i][0], stats[i][1]), ((x+w), (y+h)), (0, 255, 0), 2)

cv2.imshow("ww", image)
cv2.waitKey(0)
cv2.destroyAllWindows()