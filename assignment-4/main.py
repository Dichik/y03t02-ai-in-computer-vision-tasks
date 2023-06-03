from utils import get_image_paths

class_names = ['Dmytro_Omelian']
image_paths = get_image_paths("dataset", class_names)
print(image_paths)