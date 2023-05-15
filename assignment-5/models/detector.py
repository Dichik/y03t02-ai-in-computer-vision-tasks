from imageai.Detection import ObjectDetection

model_path = "./models/yolo-tiny.h5"
intput_path = "./input/test_input.jpg"
output_path = "./output/newimage.jp"

detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()