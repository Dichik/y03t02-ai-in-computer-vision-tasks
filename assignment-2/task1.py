"""
Task #1

Використовуючи будь-яку фотографію з декількома людьми, виявити на ньому
обличчя, очi, усмiшку. Порахувати кiлькiсть осiб на фото

"""

import cv2
from config import Config
from cascades import face_cascade, eye_cascade, smile_cascade


def detect_face_objects():
    image_path = '../images/people_smiling.jpg'
    # image_path = '../images/smile_person.png'

    frame = cv2.imread(image_path)

    gray_filter = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_rects = face_cascade.detectMultiScale(
        gray_filter,
        scaleFactor=Config.scaling_factor,
        minNeighbors=Config.min_neighbors
    )  # RESEARCH what exatctly is going on here

    print(f"Found {len(face_rects)} faces!")
    for (x, y, w, h) in face_rects:
        print(f"------")
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        face_grey = gray_filter[y:y + h, x:x + w]  # RESEARCH why do we have grey here?
        face_color = frame[y:y + h, x:x + w]

        smile = smile_cascade.detectMultiScale(face_grey)
        print(f"Found {len(smile)} smiles!")
        eye = eye_cascade.detectMultiScale(face_grey)
        print(f"Found {len(eye)} eyes!")

        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(face_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 1)
        for (ex, ey, ew, eh) in eye:
            cv2.rectangle(face_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 1)

    cv2.imshow("Faces", frame)
    cv2.waitKey(0)


if __name__ == "__main__":
    detect_face_objects()
