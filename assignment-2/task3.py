"""
Task #3

Обробити вiдеофайл, так щоб вiн видiляв пiшоходiв i, по можливостi, їхнi обличчя.
Файл можна взяти з youtube i вирiзати ролик тривалiстю не менше 30 секунд.

"""

import cv2
import numpy as np
from cascades import face_cascade
from config import Config


def detect_people():
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    cap = cv2.VideoCapture("../images/people_walk.mp4")
    while True:
        ret, img = cap.read()

        if img is None:
            print(f"Video is done. Thanks :)")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        boxes, weights = hog.detectMultiScale(gray, winStride=(8, 8))  # FIXME it can work much better
        print(f"Number of boxes: {len(boxes)}")

        boxes = np.array([[x, y, x + w, y + w] for (x, y, w, h) in boxes])
        for (xb, yb, wb, hb) in boxes:
            cv2.rectangle(img, (xb, yb), (wb, hb), (0, 255, 0), 1)

            person_grey = gray[yb:yb + hb, xb:xb + wb]
            # cv2.imshow("Person", person_grey)
            # cv2.waitKey(0)

            # face_rects = face_cascade.detectMultiScale(
            #     person_grey,
            #     scaleFactor=Config.scaling_factor,
            #     minNeighbors=Config.min_neighbors
            # )
            # print(f"Faces detected: {len(face_rects)}")
            # for (fx, fy, fw, fh) in face_rects:
            #     cv2.rectangle(img, (fx, fy), (fx + fw, fy + fh), (0, 0, 255), 1)

        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_people()
