import cv2


face_cascade = cv2.CascadeClassifier(
    f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml")  # What does it mean? research it deeper
smile_cascade = cv2.CascadeClassifier(f"{cv2.data.haarcascades}haarcascade_smile.xml")
eye_cascade = cv2.CascadeClassifier(f"{cv2.data.haarcascades}haarcascade_eye.xml")
