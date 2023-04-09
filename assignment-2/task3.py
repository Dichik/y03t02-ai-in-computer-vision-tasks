"""
Task #3

Обробити вiдеофал, так щоб вiн видiляв пiшоходiв i, по можливостi, їхнi обличчя.
Файл можна взяти з youtube i вирiзати ролик тривалiстю не менше 30 секунд.

"""

import cv2


scaling_factor = 0.2
import cv2
import numpy as np

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cv2.startWindowThread()

cap = cv2.VideoCapture("../images/people_walk.mp4")
while True:
    ret, frame = cap.read()
    # try:
    #     frame = cv2.resize(frame, (800, 560))
    # except:
    #     continue
    gray_filter = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8))
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    for (xa, ya, xb, yb) in boxes:
        cv2.rectangle(frame, (xa, ya), (xb, yb), (0, 255, 255), 1)

    cv2.imshow("Video", frame)
    if 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


