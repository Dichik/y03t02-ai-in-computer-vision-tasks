from imageai.Detection import ObjectDetection

model_path = "./models/yolo-tiny.h5"
intput_path = "./input/test_input.jpg"
output_path = "./output/newimage.jpg"

detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()

detector.setModelPath(model_path)
detector.loadModel()
detection = detector.detectObjectFromImage(
    input_image = intput_path,
    output_image_path = output_path
)

for eachItem in detection:
    print(f"{eachItem['name']}:{eachItem['percentage_probability']}")
