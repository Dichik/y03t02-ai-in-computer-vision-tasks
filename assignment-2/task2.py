"""
Task #2

Зробити розпізнавання використовуючи будь-яке відео з обличчям людини,
тривалiстю не менше 30 секунд. Можно використати камеру ноутбука

"""

import cv2
import numpy as np

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cv2.startWindowThread()

cap = cv2.VideoCapture("../images/people_walk.mp4")
while True:
    ret, frame = cap.read()
    try:
        frame = cv2.resize(frame, (800, 560))
    except:
        continue
    gray_filter = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8))
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    for (xa, ya, xb, yb) in boxes:
        cv2.rectangle(frame, (xa, ya), (xb, yb), (0, 255, 255), 1)

    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
