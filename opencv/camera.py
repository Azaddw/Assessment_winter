import cv2

cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 640, 480)

cap = cv2.VideoCapture(0)
while True:
    # 读一帧数据，返回标记和这一组数据 True表读到了，False表示没读到
    ret, frame = cap.read()

    # 可以根据ret做个判断
    if not ret:
        break
        # 没读到数据，直接退出

    # 显示图片
    cv2.imshow('video', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()